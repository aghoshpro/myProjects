from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Select models install locally

model = OllamaLLM(model="bakllava") # deepseek-r1:1.5b, llama3.2

template = """
Question: {question}

Answer: {context}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

## USING FUNCTION CALLS

def whatsUp():
    print("\n#############################################################")
    print("### Welcome to AI ChatBot Powered By Ollama and Langchain ###")
    print("#############################################################\n")
    context = ""
    while True:
        inputQuery = input("\n😉You -> ")
        if inputQuery.lower() == "bye" or inputQuery.lower() == "quit":
            break
        response = chain.invoke({"context":context, "question": inputQuery})
        print("🤖Ai -> ", response)
        context += f"\nUser: {inputQuery}\nAI: {response}\n"

if __name__ == "__main__":
    whatsUp()