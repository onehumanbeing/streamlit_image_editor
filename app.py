import anthropic
from openai import OpenAI
import streamlit as st

openai_api_key = st.secrets["openai_api_key"]
gpt_base_url = st.secrets["gpt_base_url"] if "gpt_base_url" in st.secrets else 'https://api.openai.com/v1'
client = OpenAI(api_key=openai_api_key, base_url=gpt_base_url)
st.title("💬 DALL-E 2 Image Editor")
origin_file = st.file_uploader("Origin file", type=("png"))
mask_file = st.file_uploader("Mask file", type=("png"))
prompt = st.text_input("Prompt", "After 100 days of fitness, I am thinner and have more muscles.")

if origin_file and mask_file and prompt and prompt != "":
    # st.image(origin_file, caption="Origin image", use_column_width=True)
    # st.image(mask_file, caption="Mask image", use_column_width=True)
    st.write("Editing image...")
    response = client.images.edit(
        model="dall-e-2",
        image=origin_file,
        mask=mask_file,
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    st.image(image_url, caption="Edited image", use_column_width=True)