name = input("Enter Your Name: ")
email = input("Enter your Email: ")

with open("data.txt", "a") as f:
    f.write(f"\nName: {name}\n")
    f.write(f"Email: {email}\n")

print("Thank you for your response.")