import streamlit as st
import json
from tools import exp_ct, edu_ct, article_ct
import requests as q
from bs4 import BeautifulSoup

content = json.load(open("content.json"))
header = content["Header"]
experience = content["Experiences"]
education = content["Education"]
articles = content["Featured articles"]

st.set_page_config(page_title=header["Name"], page_icon=header["Icon"], layout="centered")

CSS_file = "style.css"
st.markdown(f'<style>{open(CSS_file).read()}</style>', unsafe_allow_html=True)


#### Header

# Composition of name-role and image respectively
ratio = [7.2, 2.8]

title, image = st.columns(ratio, gap="medium", vertical_alignment="center")

with title:
    st.title(header["Name"])
    st.write(header["Role"])

    st.markdown(f"""
                    <div class="links">
                        <a href="{header['Github']}" target="_blank"><i class="fa fa-github"></i>  Github</a>
                        <a href="{header['LinkedIn']}" target="_blank"><i class="fa fa-linkedin-square"></i>  LinkedIn</a>
                        <a href="{header['Medium']}" target="_blank"><i class="fa fa-medium"></i>  Medium</a>
                        <a href="{header['Resume']}" target="_blank" class="active"><i class="fa fa-file"></i>  Resume</a>
                    </div>
                """, unsafe_allow_html=True)

with image:
    st.image("media/image.png", use_column_width="auto")

st.markdown(f"""
                <p class="contact"><a href="#e0369f68" class=contact> Get in touch </a></p>
            """, unsafe_allow_html=True)


st.write(header["Description"])

Experience, Education, Projects, Article, Skills = st.tabs(["Experience", "Education", "Projects", "Featured Articles", "Skills"])

with Experience:
    for key in experience:
        infos = experience[key]
        exp_ct(infos["Logo"], infos["Company"],infos["Role"], infos["Duration"],
               infos["Place"], infos["Description"], infos["Keywords"])
        st.write("")

with Education:
    for key in education:
        infos = education[key]
        edu_ct(infos["Logo"], infos["School"],infos["Degree"], infos["Duration"],
               infos["Place"], infos["Relevant courses"])
        st.write("")

with Article:
    username = articles["Username"]
    main_page = BeautifulSoup(q.get("https://medium.com/@nour.oulad.moussa/").content, 'lxml')
    feed = main_page.find_all("div", class_="ab cm")
    for i, article in enumerate(feed[1:]):
        link = article.find_all("a")[2]["href"]
        title = article.find("h2").text
        description = article.find("h3").text
        thumbnail = article.find_all("img")[2]["src"]
        date = article.find_all("span")[1].text
        article_ct(link, title, description, thumbnail, date)

st.write("### :mailbox_with_no_mail: Get in touch with me")

contact_form = """
<form action="https://formspree.io/f/manwqlgp" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Full name" required>
    <input type="email" name="email" placeholder="Email address" required>
    <input type="text" name="subject" placeholder="Subject" required>
    <textarea name="message" placeholder="Feel free to express yourself !"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)