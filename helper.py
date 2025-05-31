
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_groq import ChatGroq
 

api_key = "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"
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment.")
 
# Initialize Groq model
llm = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192",
    api_key=api_key
)
 
def suggest_shoes(occasion):
    # Prompt to generate brand name
    brand_prompt = PromptTemplate(
        input_variables=["occasion"],
        template="Suggest a stylish shoe brand name perfect for a {occasion}. Return ONLY the name."
    )
    brand_chain = LLMChain(llm=llm, prompt=brand_prompt, output_key="brand")
 
    # Prompt to generate shoe recommendations
    shoes_prompt = PromptTemplate(
        input_variables=["brand"],
        template="List 5 stylish shoe options sold by the brand {brand}. Only return a comma-separated list."
    )
    shoes_chain = LLMChain(llm=llm, prompt=shoes_prompt, output_key="shoes")
 
    # Sequential chain: brand first, then shoes
    chain = SequentialChain(
        chains=[brand_chain, shoes_chain],
        input_variables=["occasion"],
        output_variables=["brand", "shoes"]
    )
 
    return chain({"occasion": occasion})