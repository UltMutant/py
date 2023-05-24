email = input("enter your email:").strip()
name=email[:email.index("@")]
domain=email[email.index('@')+1:]
print(name)
print(domain)