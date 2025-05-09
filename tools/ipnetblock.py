import requests

def get_ip_netblock(ip):
    url = f"https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey=[api here]&ip={ip}"
    response = requests.get(url)
    results = response.json()

    if 'result' in results and 'inetnums' in results['result']:
        inetnums = results['result']['inetnums']
        print("\n")
        print(f"{'=' * 200}")
        print(f"NETBLOCK INFO FOR IP : {results['search']}")
        print(f"{'=' * 200}")
        print(f"Total records found: {results['result']['count']}\n")

        for index, inetnum in enumerate(inetnums, start=1):
            print(f"Record {index}:")
            print(f"  Range: {inetnum['inetnum']}")
            print(f"  AS Number: {inetnum['as']['asn'] if inetnum['as'] else 'N/A'}")
            print(f"  Organization: {inetnum['org']['name'] if inetnum['org'] else 'N/A'}")
            print(f"  Description: {', '.join(inetnum['description']) if inetnum['description'] else 'N/A'}")
            print(f"  Country: {inetnum['country']}")

            # Admin Contact
            print(f"  Admin Contact:")
            if inetnum.get('adminContact') and len(inetnum['adminContact']) > 0:
                admin_contact = inetnum['adminContact'][0]
                print(f"    Name: {admin_contact.get('person', 'N/A')}")
                print(f"    Email: {admin_contact.get('email', 'N/A')}")
                print(f"    Phone: {admin_contact.get('phone', 'N/A')}")
            else:
                print("    No admin contact available.")

            # Tech Contact
            print(f"  Tech Contact:")
            if inetnum.get('techContact') and len(inetnum['techContact']) > 0:
                tech_contact = inetnum['techContact'][0]
                print(f"    Name: {tech_contact.get('person', 'N/A')}")
                print(f"    Email: {tech_contact.get('email', 'N/A')}")
                print(f"    Phone: {tech_contact.get('phone', 'N/A')}")
            else:
                print("    No tech contact available.")

            print(f"{'-' * 200}")

    else:
        print("No results found for this IP address.")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to look up: ")
    get_ip_netblock(ip_address)
