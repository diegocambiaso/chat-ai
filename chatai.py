#!/usr/bin/env python
# coding=utf8
#
# Copyright (C) 2023, Diego Cambiaso
# GNU General Public License v3.0

'''
This script is for educational purposes and will let you run a simple Chat GPT implementation.
'''

# (*) You need to create a free account to get your API Key.

import openai

openai.api_key = (
    "##-aK9dnLrB3k6RhmJBXA1hT3BlbkFJ5BhA0bHE1jiA1wJHeYtk"  # please, change the API KEY (*)
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
        print("Error during input data or OpenAI API is not available at this moment")
        print('Please try again or write "Exit"')
        continue
