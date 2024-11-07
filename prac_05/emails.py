"""
Estimate 18 minutes
Actual 23 minutes
"""


def main():
    """Get emails and store names in a dictionary."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        correction = input(f"Is your name {name}? (Y/n) ").upper()
        if correction != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract potential name from provided email address."""
    stripped_email = email.split('@')[0]
    parts = stripped_email.split('.')
    name = " ".join(parts).title()
    return name


main()
