# Create a program that asks the user for their age and tells them what they are eligible for.



# After determining the category:

# Children → "Enjoy your childhood!"
# Teenagers → "Study hard and enjoy learning!"
# Adults → "You are eligible to vote."
# Senior Citizens → "Enjoy your retirement!"
# ========================================
#         AGE ELIGIBILITY CHECKER
# ========================================
# Age: 10

# Category: Child
# Message : Enjoy your childhood!

# ========================================
# Rules
# Age less than 13 → Child
# Age 13–17 → Teenager
# Age 18–59 → Adult
# Age 60 or above → Senior Citizen
# age = int(input("Enter Your Age : "))
# print("="*40)
# print("AGE ELIGIBILITY CHECKER".center(40))
# print("="*40)
# print(f"Age : {age}")
# print()

# if age<=0:
#     print("Invalid age entered.")
# elif age<13:
#     category = "Child"
# elif age>=13 and age<=17:
#     category = "Teenager"
# elif age>=18 and age<=59:
#     category = "Adult"
# else:
#     category = "Senior Citizen"


# print(f"Category : {category}")

# if category=="Child":
#     print(f"Message : Enjoy your childhood!")
# elif category=="Teenager":
#     print(f"Message : Study hard and enjoy learning!")
# elif category=="Adult":
#     print(f"Message : You are eligible to vote.")
# else:
#     print(f"Message : Enjoy your retirement!")
# print("="*40)

#more professional version
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")

else:
    if age < 13:
        category = "Child"
        message = "Enjoy your childhood!"
        voting_status = "Too young to vote"

    elif age < 18:
        category = "Teenager"
        message = "Study hard and enjoy learning!"
        voting_status = "Too young to vote"

    elif age < 60:
        category = "Adult"
        message = "You are eligible to vote."
        voting_status = "Eligible voter"

    else:
        category = "Senior Citizen"
        message = "Enjoy your retirement!"
        voting_status = "Senior voter"

    print("=" * 40)
    print(f"Age           : {age}")
    print(f"Category      : {category}")
    print(f"Message       : {message}")
    print(f"Voting Status : {voting_status}")
    print("=" * 40)