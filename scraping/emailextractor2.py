import requests
from bs4 import BeautifulSoup
import re

def extract_emails_from_webpage(webpage_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(webpage_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get the text content of the webpage
        text_content = soup.get_text()
        
        # Regular expression pattern for matching email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Find all email addresses in the text content
        emails = re.findall(email_pattern, text_content)
        
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []

# Example usage
webpage_url = 'https://www.neo.space/blog/things-to-consider-for-creating-professional-email-address-examples-ideas'  # Replace with the actual webpage URL
emails = extract_emails_from_webpage(webpage_url)

print(emails)
print("Found emails:")
for email in emails:
    print(email)
