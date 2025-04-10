from osint_recon.linkedin_scraper import scrape_linkedin
from osint_recon.whois_lookup import whois_lookup
from osint_recon.email_breach_check import check_email_breach
from phishing_sender.email_sender import send_phishing_email
from credential_harvester.app import run_harvester
from social_bot.bot import run_social_bot
from dashboard.app import run_dashboard

if __name__ == '__main__':
    print("Starting Social Engineering Framework...")
    run_dashboard()
