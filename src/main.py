import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

#load_dotenv()

#model = ChatOpenAI(
#    model = "gpt-4o-mini",
#    temperature = 0.7,
#   )


from recommender_engine import Recommender
from recommender_engine import load_df, create_product_key
path = "data/raw"

user_prompt = input("please enter the good you wish")

df = load_df(path)
df = create_product_key(df)

rec = Recommender(df)
rec.fit()
result = rec.recommend(user_prompt)
print(result)
