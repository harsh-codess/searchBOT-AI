import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

## Arxiv and wikipedia Tools
arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

search=DuckDuckGoSearchRun(name="Search")


# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .credit-footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 5px 10px;
        border-radius: 10px;
        font-size: 12px;
        color: #666;
        border: 1px solid #ddd;
    }
    .search-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .stChatMessage {
        border-radius: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title with better styling
st.markdown('<h1 class="main-header">🔎 LangChain - Chat with Search</h1>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="search-container">
        <p style="text-align: center; color: #666;">
            🤖 AI-powered search assistant with access to arXiv, Wikipedia, and web search<br>
            Ask me anything and I'll search for the most relevant information!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Enhanced sidebar
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input("🔑 Enter your Groq API Key:", type="password", help="Your Groq API key for accessing the LLM")
    
    st.markdown("---")
    st.markdown("### 🔍 Search Sources")
    st.markdown("""
    - 📚 **arXiv**: Academic papers
    - 📖 **Wikipedia**: General knowledge
    - 🌐 **Web Search**: Real-time information
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info("💡 Try asking about recent events, scientific papers, or general knowledge topics!")

# ...existing code...

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:=st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.error("Please enter your Groq API key in the sidebar or set GROQ_API_KEY environment variable.")
        st.stop()

    llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)
    tools=[search,arxiv,wiki]

    search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)

# Add footer with your name
st.markdown("""
<div class="credit-footer">
    Made with ❤️ by Harsh Gidwani
</div>
""", unsafe_allow_html=True)

