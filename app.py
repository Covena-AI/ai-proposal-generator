import streamlit as st
from llm_utils import generate_overview, generate_product, generate_examples, edit_section

st.set_page_config(page_title="Covena AI Proposal Generator", page_icon="📄")

# Import Plus Jakarta Sans font
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def create_section(title, generate_func, input_key, output_key, height=200):
    st.header(title)
    input_text = st.text_area(f"Enter input for {title}:", height=150, key=f"{input_key}_input")
    if st.button(f"Generate {title}"):
        if generate_func == generate_overview:
            st.session_state[output_key] = generate_func(input_text)
        elif generate_func == generate_product:
            st.session_state[output_key] = generate_func(input_text, st.session_state.get('overview', ''))
        else:  # generate_examples
            st.session_state[output_key] = generate_func(input_text, st.session_state.get('overview', ''), st.session_state.get('product', ''))
        st.rerun()  # Rerun to update the UI
    
    st.session_state[output_key] = st.text_area(f"{title}:", value=st.session_state.get(output_key, ''), height=height, key=f"{output_key}_editable")
    
    # Only show edit suggestion box if there's content in the section
    if st.session_state.get(output_key):
        edit_suggestion = st.text_area(f"Suggest edits for {title}:", key=f"{output_key}_edit_suggestion")
        if st.button(f"Edit {title}", key=f"{output_key}_edit_button"):
            st.session_state[output_key] = edit_section(st.session_state[output_key], edit_suggestion)
            st.success(f"{title} updated successfully!")
            st.rerun()  # Rerun to update the UI

def main():
    st.title("Covena AI Proposal Generator")

    # Initialize session state variables if they don't exist
    for key in ['overview', 'product', 'appendix']:
        if key not in st.session_state:
            st.session_state[key] = ""

    create_section("1. Overview Section", generate_overview, "overview", "overview")
    create_section("2. Product Section", generate_product, "product", "product")
    create_section("3. Sample Case Study Interactions", generate_examples, "appendix", "appendix", height=300)

if __name__ == "__main__":
    main()