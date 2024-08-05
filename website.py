import streamlit as st
import streamlit.components.v1 as components
   

st.set_page_config(layout="centered", page_icon="pictureofme.png", page_title="Rayhaan Khan")


components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)

lnc = 'https://www.linkedin.com/in/rrkhanrayhaan/'
Github = 'https://github.com/Rayhaan1345'
kaggle = "https://www.kaggle.com/rayhaank"
st.markdown("[Linkedin](%s)" % lnc)
st.write("[Github](%s)" % Github)
st.write("[Kaggle](%s)" % kaggle)



##ABOUT
st.title("Rayhaan Khan")

st.header(":violet[About Me ]")
brown = "https://www.brown.edu/"
st.markdown("Hi!, Thank you for visiting my website! I have recently been offered a place as Research Intern at Brown University for Cancer therapeutic methods with AI. I am Studying in Grade 10 in Podar International (CIE), Seawoods, Navi Mumbai, India. I love to delve deeper into concepts regarding Mathematics, AI, especially Deep Learning and Cancer Biology." )

##WORK
st.header("🧪 My work ")
st.markdown("I love making ML models be it regression, vision. I have a knack for making quirky projects, like a fence I am working on which is decked out with proximity sensors, alarms, light sensors and it will be powered by solar panels and car batteries.")
st.info(':red[**41/45 points 9th grade (Cambridge International), Weighted: 9.7/10 GPA**]')

##Experience
st.header("📂 Experience")

st.write("**AI research intern at M42 Health - Abu Dhabi**")
st.image('m42.png')

st.write("**Offered place as Research Intern @ Brown University**")
st.image('brown.jpeg')
#Publications
st.header('🖨️⌨️ Publications')
m42 = "https://m42.ae/"
st.markdown("During my internship at [M42](%s) - under Dr. Shadab, I built a deep learning model for identifying diabetes patients early and help them to get out of the diabetes spectrum. My detailed report on how I built the model, how it can be implemented, etc. along detailed codebook is also available with the report on Kaggle!" % m42)
st.link_button("View my report", "https://drive.google.com/file/d/1zrdhEaEcZr6TzN8UQHBsRLb4PaENmrNy/view?usp=sharing")
#hobby
st.header("📷 🦜My hobbies")
st.markdown("I love wildlife (birds mainly) photography🦜, nature conservation 🌲❤️🐅")
st.markdown("Along with 🏊🏻swimming, trying to achieve high typing (100 WPM) speeds and research!")


pics = st.link_button("click here to view my bird photos", "https://drive.google.com/drive/folders/15-nUWy8NdMhdSlY7IRLeR7gxSU9bHLJy")
st.image('pic6.jpeg', 'This is my favorite picture ❤️')
#SKILL
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
   


