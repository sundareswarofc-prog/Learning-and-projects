from dotenv import load_dotenv

load_dotenv()


from openai import OpenAI

client = OpenAI()

messages = []

def chat(question):

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.responses.create(
        model="gpt-6-luna",
        instructions="You are a helpful assistant.",
        input=messages
    )

    answer = response.output_text

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer


print(chat("My name is Arun"))
print(chat("What is my name?"))


############# the above example is manually storing the History ############

# openAI provides methods to store the History using conversation ID

conversations=client.conversations.create()
# conversations_2=client.conversations.create()

print("Conversation ID 1:", conversations.id)
# print("Conversation ID 2:", conversations_2.id)

def conversation_history(input):

       response=client.responses.create(
       model="gpt-6-luna",
       conversation=conversations.id,
       input=input
       )

       return response.output_text


print(conversation_history("My name is Mark"))
print(conversation_history("What is my name?"))

### here we are using the same conversation ID, so it remembers the history 


