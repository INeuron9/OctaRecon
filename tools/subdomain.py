import requests

def get_subdomains(domain_name):
    # API endpoint for subdomains
    api_key = 'api_here'  # Your API key
    url = f"https://subdomains.whoisxmlapi.com/api/v1?apiKey={api_key}&domainName={domain_name}"

    try:
        # Make a request to the WhoisXML API
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            result = response.json()  # Get the JSON response

            # Check if 'records' key exists and contains subdomain data
            if 'result' in result and 'records' in result['result'] and result['result']['records']:
                print("\n")
                print(f"{'=' * 200}")
                print(f"SUBDOMAIN FOR : {domain_name}")
                print(f"{'=' * 200}")
                for record in result['result']['records']:
                    print(record['domain'])  # Print the subdomain
                print(f"{'-' * 200}")
            else:
                print(f"No subdomains found for {domain_name}. Full response: {result}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = 'at_UnBYSk7tKVGGGXlaPfxl4lNIJaAds'  # Your API key
    domain_name = input("Enter the domain name to look up: ").strip()
    get_subdomains(domain_name)
