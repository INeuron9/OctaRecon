import requests

def get_ssl_info(domain_name):
    api_key = "at_UnBYSk7tKVGGGXlaPfxl4lNIJaAds"  # Replace with your actual API key
    url = "https://ssl-certificates.whoisxmlapi.com/api/v1"
    params = {
        'apiKey': api_key,
        'domainName': domain_name
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        ssl_info = response.json()

        # Displaying the information
        print("\n")
        print(f"{'=' * 200}")
        print("SSL INFO FOR : ",domain_name)
        print(f"{'=' * 200}")
        print(f"Domain: {ssl_info.get('domain', 'N/A')}")
        print(f"IP Address: {ssl_info.get('ip', 'N/A')}")
        print(f"Port: {ssl_info.get('port', 'N/A')}")

        for cert in ssl_info.get('certificates', []):
            print(f"\nCertificate Validity:")
            print(f"  Valid From: {cert.get('validFrom', 'N/A')}")
            print(f"  Valid To: {cert.get('validTo', 'N/A')}")
            
            issuer = cert.get('issuer', {})
            print(f"  Issuer: {issuer.get('commonName', 'N/A')} ({issuer.get('organization', 'N/A')})")
            
            subject = cert.get('subject', {})
            print(f"  Subject: {subject.get('commonName', 'N/A')} ({subject.get('organization', 'N/A')})")
            
            print(f"  Serial Number: {cert.get('serialNumber', 'N/A')}")
            print(f"  Signature Algorithm: {cert.get('signatureAlgorithm', 'N/A')}")
            print(f"  Validation Type: {cert.get('validationType', 'N/A')}")
            public_key = cert.get('publicKey', {}).get('pem', 'N/A')
            print(f"  Public Key (RSA):\n{public_key}")  # Displaying full public key
            print(f"{'-' * 200}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain_name = input("Enter the domain name (e.g., bbc.com): ")
    
    get_ssl_info(domain_name)
