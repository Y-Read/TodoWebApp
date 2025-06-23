import streamlit as st
import functions

todoList = functions.get_todolist()

def add_todo():
    todo = st.session_state["new_todo"]
    todoList.append(todo + "\n")
    functions.write_todolist(todoList)

st.title("My Todo App")
st.text("To increase productivity and "
        "remember what's important")

for index, todo in enumerate(todoList):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todoList.pop(index)
        functions.write_todolist(todoList)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="New todo:", on_change=add_todo, key = "new_todo")