from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from src.prompt import system_prompt
from src.helper import download_embeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#set the environment variables for Pinecone and OpenAI API keys
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY

embeddings = download_embeddings()
#load exisiting index 
index_name = "medicalchabot"
docserach = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,  
)  

retriever = docserach.as_retriever(search_type="similarity", search_kwargs={"k": 3})

chatModel = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    temperature=0,
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)


prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Context:\n{context}\n\nQuestion:\n{input}")
])


question_answering_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)



@app.route("/")
def index():
    return render_template("chat.html")    

@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])


    # update in-memory history
    CHAT_HISTORY.append(HumanMessage(content=msg))
    CHAT_HISTORY.append(AIMessage(content=answer))

    # keep only last N messages so context doesn't explode
    CHAT_HISTORY = CHAT_HISTORY[-12:]  # last 6 turns

    return str(answer)

@app.route("/reset", methods=["POST"])
def reset():
    global CHAT_HISTORY
    CHAT_HISTORY = []
    return jsonify({"status": "success", "message": "Chat history cleared."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug = True)
