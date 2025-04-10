import argparse
from osint_recon.linkedin_scraper import scrape_linkedin
from osint_recon.whois_lookup import whois_lookup
from osint_recon.email_breach_check import check_email_breach
from phishing_sender.email_sender import send_phishing_email
from credential_harvester.app import run_harvester
from social_bot.bot import run_social_bot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--osint', help='Target name for LinkedIn scrape')
    parser.add_argument('--domain', help='Perform WHOIS on domain')
    parser.add_argument('--email', help='Check email breach info')
    parser.add_argument('--phish', help='Send phishing email to address')
    parser.add_argument('--harvest', action='store_true', help='Run credential harvester')
    parser.add_argument('--bot', action='store_true', help='Run social bot')
    args = parser.parse_args()

    if args.osint:
        scrape_linkedin(args.osint)
    if args.domain:
        print(whois_lookup(args.domain))
    if args.email:
        print(check_email_breach(args.email))
    if args.phish:
        send_phishing_email(args.phish, "Security Notice", "<h1>Action Required</h1>")
    if args.harvest:
        run_harvester()
    if args.bot:
        run_social_bot()

if __name__ == '__main__':
    main()
