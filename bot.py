def chat():
    print("👋 Hi! I'm your College Admission Help Bot.")
    print("Ask me anything related to college admissions.\n(Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! Best of luck with your admission.")
            break

        elif "deadline" in user_input:
            print("Bot: Deadlines are usually in June or July.")

        elif "document" in user_input:
            print("Bot: You need mark sheets, ID proof, photos, and certificates.")

        elif "course" in user_input:
            print("Bot: You can choose Science, Commerce, or Arts streams.")

        elif "fees" in user_input:
            print("Bot: Fees vary based on the college.")

        elif "thank" in user_input:
            print("Bot: You're welcome!")

        else:
            print("Bot: Sorry, I can answer only admission-related questions.")

if __name__ == "__main__":
    chat()
