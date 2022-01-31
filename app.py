import streamlit as st
import pandas as pd


st.title("What are the CIIs of Singapore?")
st.subheader("Clicking on the refresh button will reset the session")

answers = ['Government', 'Transport (Land, Aviation, Maritime)', 'Healthcare',
           'Security and Emergency Services', 'Banking and Finance', 'Energy',
           'Water', 'Infocomm', 'Media']

if 'correct' not in st.session_state:
    st.session_state.correct = []

st.markdown("### Make a guess:")
form = st.form("input", True)
guess = form.text_input(label= "", placeholder = "Input at least 4 characters")
form.form_submit_button("Submit")
    
if len(st.session_state.correct) == len(answers):
    message = 'Congratulations! You have gotten all the CIIs.'
elif guess:
    if len(guess) < 4:
        message = 'Your guess is too short. Type at least 4 characters.'
    else:
        message = 'The guess is incorrect. Please try again'
        for answer in answers:
            if guess.lower() in answer.lower():
                if answer in st.session_state.correct:
                    message = f'You have already guessed {answer}. Please try again.'
                else:
                    st.session_state.correct.append(answer)
                    if len(st.session_state.correct) == len(answers):
                        message = 'Congratulations! You have gotten all the CIIs.'
                    else:
                        message = 'That is correct. Can you guess the other CIIs?'
                break            
else:
    message=''

st.markdown(f"### {message}")

if st.session_state.correct:
    data1, data2, data3 = st.session_state.correct[:3], st.session_state.correct[3:6], st.session_state.correct[6:] 

    hide_dataframe_row_index = """
            <style>
            th {display: none;}
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

    df = pd.DataFrame(data1).T
    
    if data2:
        while len(data2) <3:
            data2.append('')
        temp = pd.DataFrame(data2).T
        df = df.append(temp)
    
    if data3:
        while len(data3) <3:
            data3.append('')
        temp = pd.DataFrame(data3).T
        df = df.append(temp)
    

    df.columns = [' '*n for n in range(len(data1))]
    st.dataframe(df)
   