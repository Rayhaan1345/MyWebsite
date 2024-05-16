import streamlit as st
import streamlit.components.v1 as components

components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)


##ABOUT
st.title("Rayhaan Khan")
st.header(":violet[About Me ]")
brown = "https://www.brown.edu/"
st.markdown("Hi!, Thank you for visiting my website! I'm a Research Intern at [Brown University](%s), Studying in Grade 10 in Podar International (CIE), Seawoods, Navi Mumbai, India. I love to delve deeper into concepts regarding Mathematics, AI, Deep Learning and especially Cancer Biology." % brown)

##WORK
st.header("🧪 My work ")
st.markdown("As mentioned previously, I'm a Research Intern at [Brown University](%s). The main goal of my internship is finding new methods for cancer removal without surgery, and how to stop cancer growth as early as possible. In addition, I am also undergoing advanced knowledge gaining through the Brown Pre-College Program. Apart from this, I am a sophomore at Podar International School (Cambridge), Nerul, Navi Mumbai, India ")
st.info(':red[**41/45 points 9th grade, Weighted: 9.7/10 GPA**]')
#hobby
st.header("📷 🦜My hobbies")
st.markdown("I love wildlife (birds mainly) photography🦜, nature conservation 🌲❤️🐅")
option = st.selectbox("Check out some of my work!")
if option:
    st.markdown("fjd")
st.markdown("Along with 🏊🏻swimming, trying to achieve high typing speeds⌨️ and... RESEARCH!")
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
st.info("Weather Fun App!, the end of clunky weather apps!")
st.markdown("Visit: https://weatherisfun.streamlit.app/")

st.info("CT Scan classifying custom model implementation")
st.markdown("Visit: https://huggingface.co/spaces/RayhaanK/lungorbrain")

## userful links

st.subheader("Some Useful links: ")
st.markdown("LinkedIn: https://www.linkedin.com/in/rrkhanrayhaan/")

st.header("☎️ Ways to contact")
me = st.checkbox("Email Adress: ")
if me:
    st.info("rayhaankhan1345@gmail.com [preferred]")
    st.info("rkhan57@brown.edu")
