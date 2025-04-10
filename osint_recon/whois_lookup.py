import whois

def whois_lookup(domain):
    print(f"[+] Performing WHOIS lookup on: {domain}")
    try:
        info = whois.whois(domain)
        return {
            "domain": domain,
            "registrar": info.registrar,
            "creation_date": str(info.creation_date),
            "expiration_date": str(info.expiration_date)
        }
    except Exception as e:
        return {"error": str(e)}
