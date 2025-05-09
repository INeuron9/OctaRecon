import requests

def get_ip_location(ip_address):
    url = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_UnBYSk7tKVGGGXlaPfxl4lNIJaAds&ipAddress={ip_address}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Unable to fetch data: {response.status_code}")
        return
    
    results = response.json()
    
    # Check for expected keys in the results
    if 'ip' not in results:
        print("Unexpected response format:")
        print(results)  # Print the entire response for debugging
        return
    
    # Extract the location information
    location = results.get('location', {})
    
    print("\n")
    print(f"{'=' * 200}")
    print("IP GEOLOCATION FOR : ",ip_address)
    print(f"{'=' * 200}")
    print(f"IP Address: {results['ip']}")
    print(f"Country: {location.get('country', 'N/A')}")
    print(f"Region: {location.get('region', 'N/A')}")
    print(f"City: {location.get('city', 'N/A')}")
    print(f"Latitude: {location.get('lat', 'N/A')}")
    print(f"Longitude: {location.get('lng', 'N/A')}")
    print(f"Postal Code: {location.get('postalCode', 'N/A')}")
    print(f"Time Zone: {location.get('timezone', 'N/A')}")
    print(f"ISP: {results.get('isp', 'N/A')}")
    print(f"ASN: {results.get('as', {}).get('asn', 'N/A')}")
    print(f"Organization: {results.get('as', {}).get('name', 'N/A')}")
    print(f"{'-' * 200}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to look up: ")
    get_ip_location(ip_address)
