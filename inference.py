import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client if API key is available
client = None
if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    print("⚠️  Warning: OPENAI_API_KEY not set. Using mock response for testing.")

def run():
    try:
        # Validate environment
        if not API_BASE_URL:
            raise ValueError("API_BASE_URL environment variable is required")
        if not MODEL_NAME:
            raise ValueError("MODEL_NAME environment variable is required")
        
        # Reset environment and get initial state
        state_response = requests.get(f"{API_BASE_URL}/reset", timeout=5)
        state_response.raise_for_status()
        state = state_response.json()

        print("\n[TICKET] Support Ticket Generated:")
        print(f"  ID: {state['ticket']['id']}")
        print(f"  Customer: {state['ticket']['customer_name']}")
        print(f"  Phone: {state['ticket']['customer_phone']}")
        print(f"  Issue: {state['ticket']['issue']}")
        print(f"  Priority: {state['ticket']['priority']}")
        print(f"  Sentiment: {state['ticket']['customer_sentiment']}\n")

        # Get AI response
        action = None
        if client:
            try:
                # Try OpenAI API if available
                print("[AI] Generating response with OpenAI...")
                prompt = f"""
                You are a customer support agent.
                Ticket: {state['ticket']}

                Respond with ONLY valid JSON (no extra text):
                {{
                    "response": "your response here",
                    "category": "billing|technical|other",
                    "escalate": true/false
                }}
                """

                completion = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[{"role": "user", "content": prompt}]
                )

                action_text = completion.choices[0].message.content.strip()
                action = json.loads(action_text)
                print("[OK] OpenAI Response Generated\n")
            except Exception as e:
                print(f"[WARN] OpenAI Error: {str(e)[:80]}...")
                print("[TEST] Falling back to mock response...\n")
                action = None
        
        if action is None:
            # Use mock response for testing
            print("[TEST] Using mock response...\n")
            action = {
                "response": "Thank you for contacting us. We understand your issue and will help resolve it promptly.",
                "category": "billing" if "refund" in state['ticket']['issue'].lower() else "technical",
                "escalate": state['ticket']['priority'] == "high"
            }

        print(f"[RESPONSE] Agent Response:")
        print(f"  Message: {action['response'][:60]}...")
        print(f"  Category: {action['category']}")
        print(f"  Escalate: {action['escalate']}\n")

        # Execute action in environment
        result_response = requests.post(f"{API_BASE_URL}/step", json=action, timeout=5)
        result_response.raise_for_status()
        result = result_response.json()

        print("[RESULTS] Action Results:")
        print(f"  Final Score: {result['score']:.2f}/1.0")
        print(f"  Resolved: {result['resolved']}")
        print(f"  Steps: {result['step_count']}\n")
        
        if result['score'] > 0.8:
            print("[SUCCESS] Great job! The issue was resolved effectively!\n")
        elif result['score'] > 0.5:
            print("[GOOD] Good response! The issue was partially resolved.\n")
        else:
            print("[INFO] Response recorded. The issue needs more attention.\n")
        
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API Error: {e}\n")
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON Parse Error: {e}\n")
    except ValueError as e:
        print(f"[ERROR] Configuration Error: {e}\n")
    except Exception as e:
        print(f"[ERROR] Unexpected Error: {e}\n")


if __name__ == "__main__":
    run()