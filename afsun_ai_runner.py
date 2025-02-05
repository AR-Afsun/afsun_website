from langchain_ollama import OllamaLLM

def run_llama_answer(promt_value):
    model  = OllamaLLM(model="llama3.2")
    result = model.invoke(promt_value)
    return result

