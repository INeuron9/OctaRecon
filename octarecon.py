import subprocess  # for nslookup, whois
import re  # for nslookup
import requests  # for geoip, ipnetblock, subdomain, emails
import json  # for detectcms
from datetime import datetime  # for timing

# Importing your custom tools
from tools.detectcms import get_cms  # for detect cms
from tools.nslookup import get_ip_from_domain  # for nslookup
from tools.geoip import get_ip_location  # for geoip
from tools.ipnetblock import get_ip_netblock  # for geoip
from tools.subdomain import get_subdomains  # for subdomains
from tools.whois import get_whois  # for whois
from tools.sslinfo import get_ssl_info  # for sslinfo
from tools.emails import get_emails  # for emails

if __name__ == "__main__":
    start_time = datetime.now()  # Record the start time

    domain = input("Input the domain: ")
    ip = get_ip_from_domain(domain)  # calling nslookup
    get_ip_location(ip)  # calling geoip
    get_ip_netblock(ip)  # calling ipnetblock
    get_cms(domain)  # calling detectcms
    get_subdomains(domain)  # calling subdomain
    get_whois(domain)  # calling whois
    get_ssl_info(domain)  # calling sslinfo
    get_emails(domain)  # calling emails

    end_time = datetime.now()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"TIME TAKEN : {execution_time}")
