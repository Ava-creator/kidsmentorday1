# Import necessary libraries
import streamlit as st
import pandas as pd
import random
from datetime import datetime

"""
🎈 My Daily Python Adventures! 🎈
=================================

Let's learn Python by doing our daily activities!
"""

# 1. VARIABLES - Making My Lunch Box 🍱
st.header("1. Making My Lunch Box 🍱")
st.write("Let's pack a lunch using variables!")

lunch_box = {
    'sandwich': 'cheese',
    'fruit': 'apple',
    'snack': 'cookies',
    'drink': 'juice'
}

# Interactive lunch packing
st.code("""
# My Lunch Box Items
sandwich = 'cheese'
fruit = 'apple'
snack = 'cookies'
drink = 'juice'

print(f"Today I packed: {sandwich} sandwich, {fruit}, {snack}, and {drink}!")
""")

if st.button("Pack My Lunch! 🎒"):
    st.success(f"Today I packed: {lunch_box['sandwich']} sandwich, {lunch_box['fruit']}, {lunch_box['snack']}, and {lunch_box['drink']}!")

# 2. LISTS - My Toy Box 🧸
st.header("2. Organizing My Toy Box 🧸")

toys = ['teddy', 'blocks', 'car', 'doll', 'ball']
st.code("""
# My Toy List
toys = ['teddy', 'blocks', 'car', 'doll', 'ball']

# Let's count my toys
print(f"I have {len(toys)} toys!")
""")

if st.button("Count My Toys! 🔢"):
    st.write(f"I have {len(toys)} toys!")
    for i, toy in enumerate(toys, 1):
        st.write(f"{i}. {toy}")

# 3. IF STATEMENTS - Weather Dress-Up 🌤
st.header("3. What Should I Wear Today? 🌤")

st.code("""
# Weather Dress-Up Game
weather = st.selectbox('How is the weather?', 
    ['sunny', 'rainy', 'cold', 'hot'])

if weather == 'sunny':
    clothes = '👕 t-shirt and 👖 shorts'
elif weather == 'rainy':
    clothes = '🧥 raincoat and 👢 boots'
elif weather == 'cold':
    clothes = '🧥 warm jacket and 🧣 scarf'
else:
    clothes = '👕 light clothes and 🧢 hat'
""")

weather = st.selectbox('How is the weather?', ['sunny', 'rainy', 'cold', 'hot'])
if st.button("Help Me Dress! 👔"):
    if weather == 'sunny':
        st.write("You should wear: 👕 t-shirt and 👖 shorts")
    elif weather == 'rainy':
        st.write("You should wear: 🧥 raincoat and 👢 boots")
    elif weather == 'cold':
        st.write("You should wear: 🧥 warm jacket and 🧣 scarf")
    else:
        st.write("You should wear: 👕 light clothes and 🧢 hat")

# 4. LOOPS - Daily Chores Counter ✨
st.header("4. My Daily Chores ✨")

st.code("""
# Daily Chores Checker
chores = ['make bed', 'brush teeth', 'feed pet', 
          'clean room', 'homework']

for chore in chores:
    print(f"✓ Did you {chore}?")
""")

chores = ['make bed', 'brush teeth', 'feed pet', 'clean room', 'homework']
if st.button("Check My Chores! ✅"):
    chores_done = 0
    for chore in chores:
        if random.choice([True, False]):
            st.write(f"✅ {chore} - Done!")
            chores_done += 1
        else:
            st.write(f"❌ {chore} - Not yet!")
    st.write(f"You completed {chores_done} out of {len(chores)} chores!")

# 5. FUNCTIONS - Pocket Money Calculator 💰
st.header("5. My Pocket Money Calculator 💰")

st.code("""
# Pocket Money Calculator
def calculate_savings(pocket_money, weeks):
    return pocket_money * weeks

weekly_money = 5  # $5 per week
weeks = 4  # saving for 4 weeks
total = calculate_savings(weekly_money, weeks)
print(f"If I save ${weekly_money} for {weeks} weeks, I'll have ${total}!")
""")

weekly_money = st.number_input("Weekly pocket money ($):", 1, 20, 5)
weeks = st.number_input("Number of weeks to save:", 1, 52, 4)

if st.button("Calculate My Savings! 💰"):
    total = weekly_money * weeks
    st.success(f"If you save ${weekly_money} for {weeks} weeks, you'll have ${total}!")

# 6. DICTIONARIES - My Schedule Planner 📅
st.header("6. My Daily Schedule 📅")

st.code("""
# My Schedule Dictionary
schedule = {
    'morning': 'school',
    'afternoon': 'play',
    'evening': 'homework',
    'night': 'sleep'
}

time = 'morning'
print(f"During {time}, I {schedule[time]}!")
""")

schedule = {
    'morning': 'school',
    'afternoon': 'play',
    'evening': 'homework',
    'night': 'sleep'
}

time_of_day = st.selectbox("What time is it?", list(schedule.keys()))
if st.button("Check My Schedule! 🕒"):
    st.write(f"During {time_of_day}, you should: {schedule[time_of_day]}!")

# 7. SIMPLE MATH - Snack Sharing Calculator 🍪
st.header("7. Sharing Snacks Calculator 🍪")

st.code("""
# Snack Sharing Calculator
def share_snacks(snacks, friends):
    return snacks // friends, snacks % friends

total_cookies = 10
total_friends = 3
each_gets, leftover = share_snacks(total_cookies, total_friends)
print(f"Each friend gets {each_gets} cookies, with {leftover} left over!")
""")

cookies = st.number_input("How many cookies do you have?", 1, 100, 10)
friends = st.number_input("How many friends?", 1, 10, 3)

if st.button("Share Cookies! 🍪"):
    each_gets = cookies // friends
    leftover = cookies % friends
    st.success(f"Each friend gets {each_gets} cookies!")
    if leftover:
        st.info(f"There are {leftover} cookies left over!")

st.markdown("""
---
### 🌟 Remember:
1. Variables are like boxes where we store things
2. Lists are like toy boxes holding many items
3. If statements help us make decisions
4. Loops help us do things many times
5. Functions are like our favorite recipes
6. Dictionaries are like matching games

Keep practicing and have fun! 🎈
""")