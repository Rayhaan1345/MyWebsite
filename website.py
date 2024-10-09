import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_icon="pictureofme.png", page_title="Rayhaan Khan")

st.title("Rayhaan Khan")

components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)

lnc = 'https://www.linkedin.com/in/rrkhanrayhaan/'
Github = 'https://www.github.com/rayhaan1345'
kaggle = 'https://www.kaggle.com/rayhaank'


st.warning("Blog: !! Under construction !!")
st.link_button("Blog", "")
st.markdown("[Linkedin](%s)" % lnc)
st.write("[Github](%s)" % Github)
st.write("[Kaggle](%s)" % kaggle)


##ABOUT
st.header(":violet[About Me ]")
brown = "https://www.brown.edu/"
st.markdown("Hi!, Thank you for visiting my website! I was an intern at M42 Health Abu Dhabi and have recently been offered a place as Research Intern at Brown University for Cancer therapeutic methods with AI. I am Studying in Grade 10 in Podar International (CIE), Seawoods, Navi Mumbai, India. I love to delve deeper into concepts regarding Mathematics, AI, especially Deep Learning and Cancer Biology." )
st.markdown("If you're looking for collaborators for Robotics/ML projects, please feel free to get in touch!")
##WORK
st.header("🧪 Research ")
st.markdown("I love making ML models be it regression or vision. I have built many projects- but the cornerstone of them being the diabetes predictor model trained and deployed during my internship at M42 Health.")
st.info(':red[**41/45 points 9th grade (Cambridge International), Weighted: 9.7/10 GPA**]')

#Publications
st.header('🖨️⌨️ Publications')
m42 = "https://m42.ae/"
st.markdown("During my internship at [M42](%s) - under Dr. Shadab, I built a deep learning model for identifying diabetes patients early and help them to get out of the diabetes spectrum. My detailed report on how I built the model, how it can be implemented, etc. along detailed codebook is also available with the report on Kaggle!" % m42)
st.link_button("View my report", "https://drive.google.com/file/d/1zrdhEaEcZr6TzN8UQHBsRLb4PaENmrNy/view?usp=sharing")

st.header("💼 My proficiencies ")
st.info("🐍 Python")
st.info("🧑‍💻 VS Code")
st.info("🤖 Arduino")
st.info("🔬 Research")
st.info("📊 Probability & statistics | 🧮 Advanced Math")

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


st.header(" ☎️ Contact:")
me = st.checkbox("Email Adress: ")
if me:
    st.info("rayhaankhan1345@gmail.com")
   


