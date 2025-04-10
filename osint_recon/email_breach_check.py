def check_email_breach(email):
    print(f"[+] Checking breach info for: {email}")
    # Simulated breach info
    breached_sites = ["LinkedIn", "Adobe", "MySpace"]
    return {
        "email": email,
        "breaches": breached_sites
    }
