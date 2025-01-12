import streamlit as st
import random

# Title of the app
st.title("Guess the Number Game!")

# Instructions for the game
st.write("I am thinking of a number between 1 and 20. Can you guess it?")

# Generate a random number between 1 and 20 (this will stay the same during the session)
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 20)

# Let the player input their guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=20, step=1)
st.success(f" the number is {st.session_state.random_number }")
# Check the guess when the player clicks the button
if st.button("Check my guess!"):
    if guess == st.session_state.random_number:

        st.success(f"Yay! You guessed it right! The number was {st.session_state.random_number}.")
        st.session_state.random_number = random.randint(1, 20)  # Reset for a new game
    elif guess < st.session_state.random_number:
        st.warning("Oops! Too low. Try again!")
    else:
        st.warning("Oops! Too high. Try again!")

# Show a hint to help the player
if st.checkbox("Need a hint?"):
    if st.session_state.random_number % 2 == 0:
        st.write("Hint: The number is even.")
    else:
        st.write("Hint: The number is odd.")
