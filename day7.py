print("Welcome to the ISKCON and Vedic Fan Questionnaire!")

favorite_verse = favorite_kirtan = favorite_teaching = favorite_festival = "No favorite"

if input("Do you like reading the Bhagavad Gita? (yes/no): ").lower() == 'yes':
    favorite_verse = input("What is your favorite verse from the Bhagavad Gita? ")

if input("Do you enjoy participating in kirtan? (yes/no): ").lower() == 'yes':
    favorite_kirtan = input("What is your favorite kirtan song or melody? ")
    if input("Do you admire Srila Prabhupada's teachings? (yes/no): ").lower() == 'yes':
        favorite_teaching = input("What is your favorite teaching of Srila Prabhupada? ")
        if input("Do you enjoy ISKCON festivals? (yes/no): ").lower() == 'yes':
            favorite_festival = input("What is your favorite ISKCON festival? ")

print("\nThank you for participating in the ISKCON and Vedic Fan Questionnaire!")
print(f"Favorite Verse: {favorite_verse}")
print(f"Favorite Kirtan: {favorite_kirtan}")
print(f"Favorite Teaching: {favorite_teaching}")
print(f"Favorite Festival: {favorite_festival}")
