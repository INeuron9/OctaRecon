import subprocess
import re

def get_ip_from_domain(domain):
    # Run the nslookup command
    result = subprocess.run(['nslookup', domain], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Use regex to find the IP address that follows the "Name:" line
        match = re.search(r'Name:\s+' + re.escape(domain) + r'\s*Address:\s+(\d+\.\d+\.\d+\.\d+)', result.stdout)
        if match:
            print("\n")
            print(f"{'=' * 200}")
            print("IP FOR DOMAIN : ",domain)
            print(f"{'=' * 200}")
            print("ip : ",match.group(1))
            print(f"{'-' * 200}")
            return match.group(1)  # Extracted IP address
    return None  # Return None if not found

