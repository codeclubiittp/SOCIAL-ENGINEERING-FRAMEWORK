def generate_prompt(target_email):
    return f"""
Hi {target_email.split('@')[0].capitalize()},

We noticed suspicious activity associated with your account.
To avoid service disruption, please confirm your identity using the secure portal below:

http://your-server.com/login

Thank you,
Security Team
"""
