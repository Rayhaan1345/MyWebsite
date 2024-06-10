import streamlit as st
import streamlit.components.v1 as components

components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)

##Page config
st.set_page_config(
    page_title="Rayhaan Khan",
    page_icon=st.image('pictureofme.png')
)

##ABOUT
st.title("Rayhaan Khan")
st.header(":violet[About Me ]")
brown = "https://www.brown.edu/"
st.markdown("Hi!, Thank you for visiting my website! I have recently been offered a place as Research Intern at Brown University for Cancer Biology. I am Studying in Grade 10 in Podar International (CIE), Seawoods, Navi Mumbai, India. I love to delve deeper into concepts regarding Mathematics, AI, Deep Learning and especially Cancer Biology." )

##WORK
st.header("🧪 My work ")
st.markdown("I love making ML models be it regression, vision. I have a knack for making quirky projects, like an electric fence I am working on which is decked out with proximity sensors, alarms, light sensors and it will be powered by solar panels and car batteries.  ")
st.info(':red[**41/45 points 9th grade, Weighted: 9.7/10 GPA**]')

#Publications
st.header('🖨️⌨️ Publications')
st.markdown("While doing my internship at M42, under Dr. Shadab Khan, I built a deep learning model for identifying diabetes patients early and help them to get out of the diabetes spectrum. Here is my detailed report on how I built the model, how it can be implemented, etc. And Also a detailed codebook is also available with the report on Kaggle!")
st.link_button("View my report", "https://drive.google.com/file/d/1NK5K5XpwEViTBirFrtdx0z29iKdMGhTT/view?usp=sharing")
#hobby
st.header("📷 🦜My hobbies")
st.markdown("I love wildlife (birds mainly) photography🦜, nature conservation 🌲❤️🐅")

st.markdown("Along with 🏊🏻swimming, trying to achieve high typing speeds⌨️ and... RESEARCH!")
st.link_button("View my work", "https://drive.google.com/drive/folders/15-nUWy8NdMhdSlY7IRLeR7gxSU9bHLJy?usp=sharing")
#SKILL
st.header("💼 My proficiencies ")
st.info("🐍 Python")
st.info("VS Code")
st.info("🔬 Research")
st.info("🧮 Advanced Mathematics")
st.info("🖥️ 💻 Computer Hardware")

## Certifications
st.header(" 🎓Certifications " )
edx = 'https://courses.edx.org/certificates/b23e278c0b6d4735b83562769e9b1c71'
st.markdown(":red[[HarvardX CS50's Introduction To Programming With Python (Verified edX)](%s)]" % edx)
st.markdown("Fast.ai, Practical Deep Learning For Coders")
st.markdown(":blue[HarvardX CS50's Introduction To Programming With Scratch]")

## Other projects
st.header(" 🤖 Some of my projects: ")
st.success("Diabetes Predictor with Interactive Report")
st.markdown("Visit: https://research-report-diabetes.streamlit.app/")
st.success("Weather Fun App!, the end of clunky weather apps!")
st.markdown("Visit: https://weatherisfun.streamlit.app/")

## userful links

st.subheader("Some Useful links: ")
st.markdown("LinkedIn: https://www.linkedin.com/in/rrkhanrayhaan/")

st.header("☎️ Ways to contact")
me = st.checkbox("Email Adress: ")
if me:
    st.info("rayhaankhan1345@gmail.com [preferred]")

