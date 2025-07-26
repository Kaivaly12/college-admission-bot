# bot.py

def college_admission_bot():
    print("🤖 Welcome to the College Admission Bot!")
    while True:
        query = input("You: ").lower()
        if "admission" in query:
            print("Bot: Admissions are open until 31st August 2025.")
        elif "courses" in query:
            print("Bot: We offer BTech, BBA, MBA, and MSc programs.")
        elif "fees" in query:
            print("Bot: The fee structure varies by course. Please visit our website.")
        elif "bye" in query or "exit" in query:
            print("Bot: Thank you! Have a great day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Try asking about admissions or courses.")

college_admission_bot()
