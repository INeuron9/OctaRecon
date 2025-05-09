import requests
import json
from datetime import datetime

# Function to scan the given domain using WhatCMS API
def get_cms(domain):
    # Your WhatCMS API key (replace with your actual API key)
    API_KEY = 'put api here'
    # Build the request URL
    api_url = f"https://whatcms.org/API/Tech?key={API_KEY}&url={domain}"
    
    # Send the request to WhatCMS API
    try:
        response = requests.get(api_url)
        
        # Check for a successful response
        if response.status_code == 200:
            data = response.json()
            
            # Handle successful result
            if data['result']['code'] == 200:
                print("\n")
                print(f"{'=' * 200}")
                print("DETECTED TECHNOLOGIES FOR : ",domain)
                print(f"{'=' * 200}")

                # Loop through each detected technology and display info
                for tech in data['results']:
                    print(f"Technology: {tech['name']}")
                    print(f"Version: {tech['version'] if tech['version'] else 'N/A'}")
                    print(f"Categories: {', '.join(tech['categories'])}")
                    print(f"More Info: {'https:' + tech['url']}\n")
                
                # Convert and display the 'last_checked' timestamp
                timestamp = int(data['last_checked'])
                last_checked_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Last Checked: {last_checked_date} UTC")
                print(f"{'-' * 200}")
            else:
                print(f"Error: {data['result']['msg']} (Code: {data['result']['code']})")
        else:
            print(f"Failed to connect to WhatCMS API. HTTP Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during API request: {e}")

# Main function to run the script
def main():
    # Get domain input from the user
    domain = input("Enter the domain name to scan (e.g., example.com): ").strip()
    
    # Validate user input
    if domain:
        get_cms(domain)
    else:
        print("Invalid domain name. Please enter a valid domain.")

# Run the script
if __name__ == "__main__":
    main()
