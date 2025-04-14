from .prompts import generate_prompt
import time

def run_social_bot():
    print("[+] Social engineering bot activated.")
    targets = ["alice@example.com", "bob@example.com"]

    for target in targets:
        message = generate_prompt(target)
        print(f"\n[+] Generated message for {target}:\n")
        print(message)
        time.sleep(1)
