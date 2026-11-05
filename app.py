from google import genai

from settings import gemini_api_key

def get_connection():

    client = genai.Client(
        api_key=gemini_api_key
    )
    return client

def get_chat_response (prompt):
    client = get_connection()

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )
    print(interaction.output_text)

def main():
    print("="*50)
    print("Welcome to the Gemini API Chatbot!")
    print("="*50, "\n")
    
    while True:
        prompt = input("Gemini: ")
        get_chat_response (prompt)
        print()
        print("=" * 50)
        print()
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice !='y':
            print("Exiting the chatbot. Goodbye!")
            break


if __name__ == "__main__":
    main()