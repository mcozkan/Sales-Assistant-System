
import os
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
#from langchain_google_genai import ChatGoogleGenerativeAI
#from sqlmodel import SQLModel

from recommender_engine import Recommender, load_df, create_product_key


load_dotenv()


# Preparing Recommender
path = "data/raw"

df = load_df(path)
df = create_product_key(df)

rec = Recommender(df)
rec.fit()

# In order to use it as a tool:
@tool
def recommend_product(product_name : str, top_n : int = 5) -> str:
    """
    Given a cosmetic product name, returns similar Sephora products
    based on ingredient similarity using TF-IDF and cosine similarity.
    """
    result = rec.recommend(product_name, top_n = top_n)

    if isinstance(result, str):
        return result

    return result.to_string(index=False)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=os.getenv("OPENAI_API_KEY")
)
llm_tools = llm.bind_tools([recommend_product   ])

# Agent loop
def run_agent(user_query: str):
    system_prompt = """
You are a helpful Sephora product recommendation assistant.

Your job:
- Understand the user's product request.
- If the user asks for similar products, use the recommend_product tool.
- Do not invent products.
- Only explain products returned by the tool.
- If no product is found, ask the user to try another product name.
- Keep answers clear and concise.
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_query)
    ]

    response = llm_tools.invoke(messages)

    # the LLM may call the functions
    if response.tool_calls:
        tool_call = response.tool_calls[0]

        if tool_call["name"] == "recommend_product":
            args = tool_call["args"]

            tool_result = recommend_product.invoke(args)

            final_prompt = f"""
User asked:
{user_query}

Recommendation tool returned:
{tool_result}

Explain these recommendations to the user in Turkish.
Do not invent extra products.
"""

            final_response = llm.invoke(final_prompt)
            return final_response.content

    return response.content


if __name__ == "__main__":
    user_query = input("Nasıl bir ürün önerisi istiyorsun? ")

    answer = run_agent(user_query)

    print("\nAssistant:")
    print(answer)