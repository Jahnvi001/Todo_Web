import streamlit as  st
import functions

todos = functions.get_to_dos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_to_dos(todos)


st.title("Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_to_dos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")