# import streamlit as st

# st.title("🌱 Growth Mindset Goal Tracker")
# st.write("Welcome to the Growth Mindset Goal Tracker! Let's get started.")

# goal = st.text_input("What’s one goal you want to achieve today?")
# if goal:
#     st.write(f"Great! Your goal is: **{goal}**. Keep working on it!")

import streamlit as st
import random

st.set_page_config(page_title="🌱 Growth Mindset Goal Tracker")

st.title("🌱 Growth Mindset Goal Tracker")
st.write("Welcome to the Growth Mindset Goal Tracker! Let's get started.")

# Goal Setting
st.header("Set Your Goals")
goal = st.text_input("What’s one goal you want to achieve today?")
if goal:
    st.write(f"Great! Your goal is: **{goal}**. Keep working on it!")
progress = st.slider("How much you completed your Path towards your goal?", 1, 100)
# st.progress(progress)
if progress == 100 :
  st.write(" Congratulaions, you achieved yor goal! ")
  st.balloons()
else:
    st.write(f"You are only {100 - progress}% far from your goal, keep going! ")

# Motivational Quote
st.header("Daily Motivation")
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt"
]
random_quote = random.choice(quotes)
st.write(random_quote)

# Reflection Section
st.header("Reflect on Your Progress")
reflection = st.text_area("What did you learn today? What challenges did you face?")
if reflection:
    st.write("Thank you for sharing! Reflection is key to growth.")

# Rating
rating = st.slider("Rate your day(1 = Bad, 10 = Great)", 1, 10)
st.button("Submit")