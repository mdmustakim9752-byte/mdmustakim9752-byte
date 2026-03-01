# Day 3: Learning Functions (def) in Python

def greet_user(user_name):
    # Ye function user ko Zoya ki taraf se welcome karega
    print(f"\nHello {user_name}! Main Zoya hu, aapki AI assistant.")
    print("System ekdum perfect chal raha hai. Aaj kya karna hai?")

# Program yahan se start hoga
print("--- System Booting ---")
name_input = input("Apna naam type karein: ")

# Yahan humne upar banaye gaye function ko 'call' kiya (bulaya)
greet_user(name_input)
