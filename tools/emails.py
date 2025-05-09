import requests

def get_emails(domain):
    api_key = "e3ca29afd42916f35bd2e154d61c400b"  # Your actual API key
    """Fetch emails for the given domain."""
    required_headers = {
        'Content-Type': 'application/json',
        'X-KEY': api_key
    }

    # First request to check total emails
    initial_response = requests.post(
        "https://api.prospeo.io/domain-search",
        json={'company': domain, 'limit': 1},  # Using 'company' key, but it's based on the domain
        headers=required_headers
    )

    if initial_response.status_code != 200:
        print(f"Error: {initial_response.status_code}, {initial_response.text}")
        return

    initial_result = initial_response.json()
    if initial_result['error']:
        print("Error in initial response:", initial_result['response'])
        return

    total_emails = initial_result['response']['meta']['total_emails']
    print("\n")
    print(f"{'=' * 200}")
    print(f"EMAILS FOUND FOR {domain} : ",total_emails)
    print(f"{'=' * 200}")

    if total_emails > 0:
        # Fetch emails
        email_response = requests.post(
            "https://api.prospeo.io/domain-search",
            json={'company': domain, 'limit': total_emails},  # Using 'company' key again
            headers=required_headers
        )

        if email_response.status_code == 200:
            result = email_response.json()
            if not result['error']:
                print(f"Domain: {result['response']['meta']['domain']}")
                print("Email List:")
                for index, email_info in enumerate(result['response']['email_list'], start=1):
                    name = f"{email_info['first_name']} {email_info['last_name']}".strip() or "N/A"
                    verification_status = email_info['verification']['status']
                    print(f"{index}. Email: {email_info['email']}, Name: {name}, Verification: {verification_status}")
                print(f"{'-' * 200}")
            else:
                print("Error fetching emails:", result['response'])
        else:
            print(f"Error: {email_response.status_code}, {email_response.text}")
    else:
        print("No emails found.")

# Main execution
if __name__ == "__main__":
    user_domain = input("Enter the domain name (e.g., intercom.com): ")
    get_emails(user_domain)
