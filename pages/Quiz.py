import streamlit as st
import random  #NEW

def harry_potter_quiz():
    st.title("⚡ The Hogwarts House Sorting Quiz ⚡")
    st.write(
        "Welcome to your Sorting Hat experience! Answer the following questions "
        "to discover which Hogwarts house you belong in: Gryffindor, Ravenclaw, Hufflepuff, or Slytherin."
    )

    # Keep track of scores
    houses = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

    # Question 1: Multiple Choice
    q1 = st.radio(
        "1. Which trait do you value the most?",
        ["Bravery", "Wisdom", "Loyalty", "Ambition"]
    )
    if q1 == "Bravery":
        houses["Gryffindor"] += 1
    elif q1 == "Wisdom":
        houses["Ravenclaw"] += 1
    elif q1 == "Loyalty":
        houses["Hufflepuff"] += 1
    else:
        houses["Slytherin"] += 1

    # Question 2: Multi-select
    q2 = st.multiselect(
        "2. Pick the magical creatures you like (choose all that apply):",
        ["Phoenix", "Owl", "House Elf", "Basilisk"]
    )
    if "Phoenix" in q2:
        houses["Gryffindor"] += 1
    if "Owl" in q2:
        houses["Ravenclaw"] += 1
    if "House Elf" in q2:
        houses["Hufflepuff"] += 1
    if "Basilisk" in q2:
        houses["Slytherin"] += 1

    # Question 3: Number input
    q3 = st.number_input(
        "3. On a scale of 1–10, how much do you enjoy teamwork?",
        min_value=1, max_value=10, step=1
    )  #NEW
    if q3 >= 8:
        houses["Hufflepuff"] += 1
    elif q3 <= 3:
        houses["Slytherin"] += 1
    else:
        houses["Gryffindor"] += 1

    # Question 4: Slider
    q4 = st.slider(
        "4. Pick your preferred study hour:",
        min_value=0, max_value=24, step=1
    )  #NEW
    if 6 <= q4 <= 11:
        houses["Ravenclaw"] += 1
    elif 12 <= q4 <= 17:
        houses["Hufflepuff"] += 1
    elif 18 <= q4 <= 23:
        houses["Slytherin"] += 1
    else:
        houses["Gryffindor"] += 1

    # Question 5: Text choice (instead of images)
    q5 = st.selectbox(
        "5. Which place feels most like home?",
        ["Gryffindor Tower", "Ravenclaw Tower", "Hufflepuff Basement", "Slytherin Dungeon"]
    )  #NEW
    if "Gryffindor" in q5:
        houses["Gryffindor"] += 1
    elif "Ravenclaw" in q5:
        houses["Ravenclaw"] += 1
    elif "Hufflepuff" in q5:
        houses["Hufflepuff"] += 1
    else:
        houses["Slytherin"] += 1

    # Results
    if st.button("Sort Me!"):
        result = max(houses, key=houses.get)
        st.success(f"🎉 The Sorting Hat has spoken... You are in **{result}**!")
        st.balloons()  # fun extra effect

if __name__ == "__main__":
    harry_potter_quiz()

