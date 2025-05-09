import subprocess

def get_whois(domain):
    try:
        # Execute the 'whois' command with the provided domain
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("\n")
            print(f"{'=' * 200}")
            print(f"WHOIS INFO FOR : {domain}")
            print(f"{'=' * 200}")
            print(result.stdout)  # Print the WHOIS output
            print(f"{'-' * 200}")
        else:
            print(f"Failed to fetch WHOIS data for {domain}. Error:\n{result.stderr}")
    except FileNotFoundError:
        print("The 'whois' command is not installed or not found in the PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
	# Get domain name input from the user
	domain = input("Enter the domain name to lookup (e.g., example.com): ").strip()
	# Run the WHOIS command for user input
	get_whois(domain)

# Run the script
if __name__ == "__main__":
    main()
