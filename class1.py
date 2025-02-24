import streamlit as st
import pandas as pd
import os
from io import BytesIO



# App title
st.title("To-Do List App")

# Initialize tasks list
tasks = []

# Function to add tasks
def add_task(task):
    tasks.append(task)

# Function to remove tasks
def remove_task(task):
    tasks.remove(task)

# Input form for adding tasks
with st.form("add_task_form"):
    task = st.text_input("Enter task")
    submit_button = st.form_submit_button("Add Task")

# Add task to list when submit button is clicked
if submit_button:
    add_task(task)

# Display tasks list

st.header("Tasks")  
for i, task in enumerate(tasks):
    with st.expander(f"Task {i+1}"):
        st.write(task)
        remove_button = st.button("Remove Task", key=i)
        if remove_button:
            remove_task(task)
