import streamlit as st

# page title
st.title("🎓 University Chatbot")

# input box
user_input = st.text_input("Ask me something about university life:")

# fix response
responses = {
    "library": "The library is open from 8am to 10pm every day.",
    "exam": "You can register for exams through the student portal.",
    "canteen": "The canteen serves affordable meals from 10am to 8pm.",
    "sports": "Our university offers basketball, badminton, and swimming facilities.",
    "hostel": "The hostel application is available in the housing office."
}

# process input
if user_input:
    found = False
    for keyword, answer in responses.items():
        if keyword.lower() in user_input.lower():
            st.write("Chatbot: " + answer)
            found = True
            break
    if not found:
        st.write("Chatbot: Sorry, I don’t know the answer to that yet.")
