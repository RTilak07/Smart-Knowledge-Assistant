from groq import Groq


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def answer_question(vector_db, question):
    if vector_db is None:
        return "Answer not found in the provided website content."

    docs = vector_db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    if not context.strip():
        return "Answer not found in the provided website content."

    prompt = f"""
You are an AI assistant helping a student.

Read the website content carefully and answer the question.

Rules:
- Use ONLY the website content
- Summarize if information is spread across paragraphs
- Do NOT say phrases like "website does not mention" or "unfortunately"
- Use simple, student-friendly language
- Keep the answer short and clear

Website Content:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()


#  WEBSITE SUMMARY
def summarize_website(vector_db):
    if vector_db is None:
        return "Summary not available."

    docs = vector_db.similarity_search("overview of the topic", k=5)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant helping a student.

Summarize the following website content.

Rules:
- Use ONLY the website content
- Explain the main idea clearly
- Use simple, student-friendly language
- 5–6 lines maximum

Website Content:
{context}

Summary:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
