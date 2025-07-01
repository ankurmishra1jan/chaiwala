from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

class GetLLMReturn:

    def __init__(self, model="Gemma2-9b-It", token_size=2048, temp=0.5):
        self.max_tokens = token_size
        self.temperature = temp
        self.model = model
        self.groq_model = ChatGroq(model_name=self.model, temperature=self.temperature, max_tokens=self.max_tokens)

    def get_model(self):
        return self.groq_model


if __name__ == "__main__":
    llm_model_instance = GetLLMReturn()
    model = llm_model_instance.get_model()
    response = model.invoke("hi")
    print(response)