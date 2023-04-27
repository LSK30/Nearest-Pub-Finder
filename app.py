import streamlit as st
from PIL import Image
import os

from pathlib import Path


# cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# prof_pic = cur_dir / "assets" / "ricky.jpg"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "mypic.jpg"
background = cur_dir / "resources" / "images" /"cool_background.jpg"

# Description
PAGE_TITLE = "Pub Finder"
PAGE_ICON = "🗺️"
NAME = "Landa Shasi Kumar"
EMAIL = "supershasi55@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/lsk30",
    "GitHub": "https://github.com/LSK30",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1464618663641-bbdd760ae84a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8d2Vic2l0ZSUyMGJhY2tncm91bmR8ZW58MHx8MHx8&w=1000&q=80");
background-size: cover;
background-position: top center;
}
</style>
'''


side_bgimg = '''
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1464618663641-bbdd760ae84a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8d2Vic2l0ZSUyMGJhY2tncm91bmR8ZW58MHx8MHx8&w=1000&q=80");
background-size: cover;
background-position: left;
}
</style>
'''
st.sidebar.markdown(side_bgimg, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Welcome!! :red[Everyone]")
st.subheader("let's enjoy together😎😎😎😎")

# Load css, pdf and profile pic

# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Project Name - Nearest Pub 🍷 Finder in UK")


st.subheader("👉 THE GITHUB LINK OF THIS PROJECT:-")
st.subheader("https://github.com/LSK30/Nearest-Pub-Finder")
