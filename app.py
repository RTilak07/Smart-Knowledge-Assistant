import streamlit as st

from services.web_loader import load_website
from services.text_processing import split_text
from services.vector_store import create_vector_store, load_vector_store
from services.qa_engine import answer_question, summarize_website


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Smart Knowledge Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# CUSTOM UI STYLE
# -------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color:white;
}

header, footer {
    visibility:hidden;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    margin-top:20px;
}

.sub-title{
    text-align:center;
    font-size:18px;
    opacity:0.85;
    margin-bottom:40px;
}

.card{
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(14px);
    border-radius:20px;
    padding:30px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}

.card:hover{
    transform:translateY(-8px);
}

.section-card{
    background:rgba(255,255,255,0.12);
    backdrop-filter:blur(14px);
    border-radius:20px;
    padding:30px;
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("<div class='main-title'>🤖 Smart Knowledge Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>AI-powered website summarization & question answering</div>", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "mode" not in st.session_state:
    st.session_state.mode = None

if "vector_db" not in st.session_state:
    st.session_state.vector_db = load_vector_store()

if "summary" not in st.session_state:
    st.session_state.summary = None


# -------------------------------------------------
# LANDING PAGE
# -------------------------------------------------
if st.session_state.mode is None:

    st.markdown("<h2 style='text-align:center;'>Choose an Option</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card'>
        <h3>🌐 Process URL</h3>
        <p>Analyze and summarize any website using AI.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Use URL", key="url_btn"):
            st.session_state.mode = "url"
            st.rerun()

    with col2:
        st.markdown("""
        <div class='card'>
        <h3>📄 Upload PDF</h3>
        <p>Summarize and ask questions from PDF files.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Coming Soon", disabled=True, key="pdf_btn")



# PROCESS

if st.session_state.mode == "url":

    if st.button("⬅ Back", key="back_url"):
        st.session_state.mode = None
        st.session_state.summary = None
        st.session_state.vector_db = None
        st.rerun()

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    st.subheader("🌐 Enter Website URL")

    url = st.text_input(
        "Website URL",
        placeholder="https://www.geeksforgeeks.org/operating-systems/"
    )

    if st.button("Analyze Website"):

        if not url:
            st.warning("Please enter a valid website URL")

        else:

            with st.spinner("Analyzing website..."):

                docs = load_website(url)

                chunks = split_text(docs)

                st.session_state.vector_db = create_vector_store(chunks)

                st.session_state.summary = summarize_website(
                    st.session_state.vector_db
                )

            st.success("Website analyzed successfully!")

    st.markdown("</div>", unsafe_allow_html=True)



# SUMMARY

if st.session_state.summary:

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    st.subheader("📄 Summary")

    st.write(st.session_state.summary)

    st.markdown("</div>", unsafe_allow_html=True)



# QUESTION ANSWERING

if st.session_state.vector_db:

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    st.subheader("❓ Ask a Question")

    question = st.text_input("Your Question")

    if st.button("Get Answer"):

        if not question:
            st.warning("Please enter a question")

        else:

            with st.spinner("Generating answer..."):

                answer = answer_question(
                    st.session_state.vector_db,
                    question
                )

            st.markdown("### Answer")
            st.write(answer)

    st.markdown("</div>", unsafe_allow_html=True)


# FOOTER

st.markdown(
"<div style='text-align:center;opacity:0.7;margin-top:40px;'>© 2026 Smart Knowledge Assistant</div>",
unsafe_allow_html=True
)












