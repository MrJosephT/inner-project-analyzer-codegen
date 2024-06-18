# from langchain.llms import OpenAI
# OpenAI.proxy = 'http://127.0.0.1:1080' # type: ignore

from langchain.chat_models import ChatOpenAI

ChatOpenAI.proxy = 'http://127.0.0.1:1080'  # type: ignore
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=2048,
                 openai_api_key="Todo")  # type: ignore
