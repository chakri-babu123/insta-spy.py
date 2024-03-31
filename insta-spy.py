import requests
from bs4 import BeautifulSoup
from termcolor import colored

def scrape_usernames(username):
    url = f"https://www.example.com/search?q={username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    usernames = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and username in href:
            usernames.append(href.split('/')[-1])
            if len(usernames) == 20:
                break
    return usernames

def check_passwords(usernames, passwords):
    for username in usernames:
        for password in passwords:
            if username == password:
                print(colored(f"{username}: {password} - Matched", 'green'))
                break
        else:
            print(colored(f"{username} - Not matched", 'red'))

def main():
    username = input("Enter username: ")
    password1 = input("Enter password 1: ")
    password2 = input("Enter password 2: ")
    password3 = input("Enter password 3: ")
    passwords = [password1, password2, password3]
    
    print("\nScraping usernames...")
    usernames = scrape_usernames(username)
    
    print("\nChecking passwords...")
    check_passwords(usernames, passwords)

if __name__ == "__main__":
    main()
