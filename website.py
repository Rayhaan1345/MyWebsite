import streamlit as st
import streamlit.components.v1 as components


components.iframe("https://media.licdn.com/dms/image/D4D03AQHW_lM3y3JYQA/profile-displayphoto-shrink_200_200/0/1712669123007?e=2147483647&v=beta&t=6-kK-ZzT_34_yoDvCQ_I-TSWpFUNvcCp-FgGM5NWepI", height=250)

import streamlit as st

# Set page configuration
# Function to display an icon with a label
def display_icon_with_label(icon_path, label):
    st.image(icon_path, width=40)
    st.write(label)

# Define the icons and their labels
tech_stack = [
    ("icons/typescript.png", "TypeScript"),
    ("icons/flutter.png", "Flutter"),
    ("icons/javascript.png", "JavaScript"),
    ("icons/docker.png", "Docker"),
    ("icons/firebase.png", "Firebase"),
    ("icons/vscode.png", "VS Code"),
    ("icons/react.png", "React"),
    ("icons/java.png", "Java"),
    ("icons/golang.png", "Golang"),
    ("icons/redis.png", "Redis"),
    ("icons/sc.png", "SC"),
    ("icons/arduino.png", "Arduino"),
    ("icons/dart.png", "Dart"),
    ("icons/github.png", "GitHub"),
    ("icons/python.png", "Python"),
    ("icons/postgresql.png", "PostgreSQL"),
    ("icons/yarn.png", "Yarn"),
    ("icons/raspberrypi.png", "Raspberry Pi"),
    ("icons/git.png", "Git"),
    ("icons/tailwindcss.png", "TailwindCSS"),
    ("icons/cplusplus.png", "C++"),
    ("icons/graphql.png", "GraphQL"),
    ("icons/googlecloud.png", "Google Cloud")
]

# Create a layout with multiple columns
num_columns = 4  # Number of columns to display
columns = st.columns(num_columns)

# Iterate over the tech stack and place icons and labels in columns
for index, (icon_path, label) in enumerate(tech_stack):
    col_index = index % num_columns
    with columns[col_index]:
        display_icon_with_label(icon_path, label)


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
st.link_button("View my report", "https://drive.google.com/file/d/1zrdhEaEcZr6TzN8UQHBsRLb4PaENmrNy/view?usp=sharing")
#hobby
st.header("📷 🦜My hobbies")
st.markdown("I love wildlife (birds mainly) photography🦜, nature conservation 🌲❤️🐅")

st.markdown("Along with 🏊🏻swimming, trying to achieve high typing speeds⌨️ and... RESEARCH!")
pics = st.link_button("click here to view my bird photos", "https://drive.google.com/drive/folders/15-nUWy8NdMhdSlY7IRLeR7gxSU9bHLJy")
if pics:
    st.image('pic6.jpeg', 'This is my favorite picture')
#SKILL
st.header("💼 My proficiencies ")
st.image("python.png")
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


