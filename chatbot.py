import streamlit as st

# page title
st.title("🎓 University Chatbot")

#initialize conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# input box and ask btn
user_input = st.text_input("Ask me something about university life:")
ask_btn = st.button("Ask")

# rule-based response
responses = {
    "library": "The library is open from 8am to 10pm every day.",
    "exam": "You can register for exams through the student portal.",
    "canteen": "The canteen serves affordable meals from 10am to 8pm.",
    "sports": "Our university offers basketball, badminton, and swimming facilities.",
    "hostel": "The hostel application is available in the housing office.",
    "clubs": "We have many student clubs like coding, drama, and music.",
    "bus": "Campus buses run every 15 minutes from 7am to 10pm.",
    "wifi": "Free Wi-Fi is available in all classrooms and public areas.",
    "cafeteria": "The cafeteria offers breakfast, lunch, and dinner with vegetarian options.",
    "events": "Check the student portal for upcoming events and workshops."
}

# process user input
if ask_btn:
    if user_input.strip() == "":
        st.write("🤖 Chatbot: Please type a question first.")
    else:
        found = False
        for keyword, answer in responses.items():
            if keyword.lower() in user_input.lower():
                st.session_state.history.append(("You", user_input))
                st.session_state.history.append(("Chatbot", answer))
                found = True
                break
        if not found:
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Chatbot", "Sorry, I don’t know the answer to that yet."))

# display conversation history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**🤖 Chatbot:** {text}")
        


