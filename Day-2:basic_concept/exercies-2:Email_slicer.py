# Tags: string, split, input, print
# Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example:
# Input: mary.jane@gmail.com
# Output: Hey Mary, I see your email is registered with Google. That's cool!.
# Input: peter.pan@myfantasy.com
# Output: Hey Peter, looks like you've got your own custom setup at myfantasy.com. Impressive!.

#sothea@gmail.com
user = input("Email: ")

popular_domain= {
    "gmail":"Google",
    "apple":"Apple inc",
    "yahoo":"Yahoo inc",
    "fantasy":"fantasy.inc"
}
if user !='': 
    if '@' in user and '.' in user: 
        username, domain = user.split("@")
        domainEmail, com = domain.split(".")
        
        for i in popular_domain:
            if domainEmail==i:
                print(popular_domain[domainEmail])
                break
            else : 
                print(f"This new domain {domainEmail}")
        
    else: 
        print("Invalid email!")
else: 
    print("ivalid input")