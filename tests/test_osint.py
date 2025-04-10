from osint_recon.linkedin_scraper import scrape_linkedin
from osint_recon.whois_lookup import whois_lookup
from osint_recon.email_breach_check import check_email_breach

def test_scrape_linkedin():
    result = scrape_linkedin("John Doe")
    assert "name" in result

def test_whois_lookup():
    data = whois_lookup("example.com")
    assert "domain" in data

def test_breach_check():
    data = check_email_breach("test@example.com")
    assert isinstance(data["breaches"], list)
