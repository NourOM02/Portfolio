import streamlit as st

def list_keywords(keywords, type):
    if type == "experience":
        token = "Keywords"
    elif type == "education":
        token = "Relevant courses"
    html = f"""     
                    <p>
                            <strong> {token}: </strong><br />
                            {"•".join([f"<span class='{'keyword' + ' first' if i==0 else 'keyword'}'>" + keywords[i].replace(" ", "&nbsp") + "</span>" for i in range(len(keywords))])}
                    </p>
                """

    return html

def exp_ct(logo_path, company, role, duration, place, description, keywords):
    
    with st.container():
        col1, col2 = st.columns([1, 10])

        with col1:
            st.image(logo_path, use_column_width="auto")

        with col2:
            st.write(f"**{company}**, *{role}*  \n **_{duration}_**, {place}")
            st.write(f"{description}")

        
            st.markdown(list_keywords(keywords, "experience"), unsafe_allow_html=True)

def edu_ct(logo_path, school, degree, duration, place, relevant_courses):
    
    with st.container():
        col1, col2 = st.columns([1, 10])

        with col1:
            st.image(logo_path, use_column_width="auto")

        with col2:
            st.write(f"**{school}**, *{degree}*  \n **_{duration}_**, {place}")
        
            st.markdown(list_keywords(relevant_courses, "education"), unsafe_allow_html=True)

def article_ct(link, title, description, thumbnail, date):
    with st.container(border=True):
        content, image = st.columns([7, 3])
        with content:
            st.markdown(f"""<a href="https://www.medium.com{link}" target="_blank" class="article-title" style="display: block; text-decoration:none; color: inherit;">
                                <h5>{title}</h5>
                                <p>{description}</p>
                                <p class="date">{date}</p>
                            </a>
                        """, unsafe_allow_html=True)
        with image:
            st.image(thumbnail, use_column_width="auto")
            