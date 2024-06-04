import streamlit as st
import streamlit.components.v1 as components

components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)


##ABOUT
st.title("Rayhaan Khan")
st.header(":violet[About Me ]")
brown = "https://www.brown.edu/"
st.markdown("Hi!, Thank you for visiting my website! I have recently been offered a place as Research Intern at Brown University for Cancer Biology. I am Studying in Grade 10 in Podar International (CIE), Seawoods, Navi Mumbai, India. I love to delve deeper into concepts regarding Mathematics, AI, Deep Learning and especially Cancer Biology." )

##WORK
st.header("🧪 My work ")
st.markdown("I love making ML models be it regression, vision. I have a knack for making quirky projects, like an electric fence I am working on which is decked out with proximity sensors, alarms, light sensors and it will be powered by solar panels and car batteries.  ")
st.info(':red[**41/45 points 9th grade, Weighted: 9.7/10 GPA**]')
#hobby
st.header("📷 🦜My hobbies")
st.markdown("I love wildlife (birds mainly) photography🦜, nature conservation 🌲❤️🐅")

st.markdown("Along with 🏊🏻swimming, trying to achieve high typing speeds⌨️ and... RESEARCH!")
drive = 'https://drive.google.com/drive/folders/15-nUWy8NdMhdSlY7IRLeR7gxSU9bHLJy?usp=sharing'
option = st.button("See some pictures taken by me", type="primary")
if option:
    st.markdown("click [here](%s)" % drive)
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
st.success("Weather Fun App!, the end of clunky weather apps!")
st.markdown("Visit: https://weatherisfun.streamlit.app/")

st.success("CT Scan classifying custom model implementation")
st.markdown("Visit: https://huggingface.co/spaces/RayhaanK/lungorbrain")

## userful links

st.subheader("Some Useful links: ")
st.markdown("LinkedIn: https://www.linkedin.com/in/rrkhanrayhaan/")

st.header("☎️ Ways to contact")
me = st.checkbox("Email Adress: ")
if me:
    st.info("rayhaankhan1345@gmail.com [preferred]")

