import openai

openai.api_key = (
    "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"  # please, change de API KEY
)

print("\nWelcome to Chat AI")
print("This chat is OpenAI ChatGPT based")

while True:
    question = input("\nWrite a question: ")

    if question.upper() == "EXIT":
        print("Good bye")
        exit()

    try:
        completion = openai.Completion.create(
            engine="text-davinci-003", prompt=question, max_tokens=2048
        )

        print(completion.choices[0].text)  # type: ignore

    except:
        print("Error during inputa data or OpenAI API is not available at this moment")
        print('Please try again or write "Exit"')
        continue
