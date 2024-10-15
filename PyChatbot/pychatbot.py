import openai
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
 
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(chat_log):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_log
    )
    return response['choices'][0]['message']['content'].strip()

chat_log = []
n_remembered_posts = 2

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        chat_log.append({'role': 'user', 'content': user_input})

        if len(chat_log) > n_remembered_posts * 2:
            chat_log = chat_log[-n_remembered_posts * 2:]

        retry_count = 0
        while retry_count < 5:
            try:
                response = chat_with_gpt(chat_log)
                print("Chatbot:", response)

                chat_log.append({'role': "assistant", 'content': response})
                time.sleep(20)
                break

            except openai.error.RateLimitError:
                retry_count += 1
                wait_time = 20 * retry_count
                print(f"Chatbot: I'm currently experiencing high demand. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)

            except Exception as e:
                print(f"An error occurred: {e}")
                time.sleep(10)
                break
