import streamlit as st
import json
from streamlit_lottie import st_lottie
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"









def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_computer = load_lottiefile("lottiefiles/lottie.json")
lottie_chart = load_lottiefile("lottiefiles/8517-charts.json")
lottie_process_auto = load_lottiefile("lottiefiles/automate2.json")
lottie_machine_learn = load_lottiefile("lottiefiles/ai.json")


#Initial Information
NAME = "ENGR. Jan Carlo LL. Cabatuan"
PROFESSION = "Electronics Engineer"
EMAIL = "jarlocasureco3@gmail.com"
CONTACT = "09770539733"
DESCRIPTION = """I am an Electronics Engineer with 7 years
 of experience as a data analyst at an electric distribution
  company in the Philippines. Throughout my career, 
  I have developed strong skills in network troubleshooting, 
  computer and printer troubleshooting. 
  Additionally, I am proficient in coding with Python to create data 
  visualizations and set them up on web-based apps using Streamlit."""

SKILLS = [
"- 🏆 Network troubleshooting and Analysis (VMwire, Customized Nodes via Python Automation)",
"- 🏆 Computer and printer troubleshooting (Windows File System, Linux Distro File System)",
"- 🏆 Python programming for data visualization (Plotly, Dash, Seaborn)",
"- 🏆 Streamlit web application development (Active Operational Analysis)",
"- 🏆 MySQL database management",
"- 🏆 Machine Learning using LangChain"
]

EXPERIENCE = [
"[2016 - Present]:📈🖥️🎛️📱 FULLSTACK ENGINEER, Camarines Sur 3 Electric Cooperative, INC.",
"- 💼 Analyzed data to identify patterns and trends in electricity consumption.",
"- 💼 Conducted network troubleshooting to resolve connectivity issues.",
"- 💼 Provided technical support for computer and printer troubleshooting.",
"- 💼 Collaborated with cross-functional teams to develop data-driven solutions."
]


st.set_page_config(page_title="Digital CV",layout="wide")


#Injecting CSS styling
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st_lottie(lottie_computer,speed=2,loop=True,quality="high")
with col2:
    st.title(NAME)
    st.write(PROFESSION)
    st.markdown(f'<p style="color: orange;">{EMAIL}</p>', unsafe_allow_html=True)
    st.write(CONTACT)

st.markdown("---")
st.write(DESCRIPTION)

st.write("\n")
st.subheader("EXPERIENCE")
for item in EXPERIENCE:
    st.write(item)

st.write("\n")
st.subheader("HARD SKILLS")
for i in SKILLS:
    st.write(i)

st.markdown("---")

col_data_analysis, col_analysis_desc = st.columns(2)
with col_data_analysis:
    st_lottie(lottie_chart,speed=2,loop=True,quality="high",height=500,width=1000)
with col_analysis_desc:
    st.subheader("Data Analysis Projects:")
    st.write("Click the link below!\n")
    st.markdown('[🌐Data Ploting the 2022 Philippine Population🌐](https://python-data-analysis.onrender.com)')
st.write("\n")

col_aimac_des, col_aimac = st.columns(2)
with col_aimac_des:
    st_lottie(lottie_machine_learn, speed=2, loop=True, quality="high",height=500,width=1000)
with col_aimac:
    st.subheader("Machine Learning Projects:")
    st.write("Click the link below!\n")
    st.markdown("🌐Coming Soon!🌐")
st.write("\n")

col_procauto, col_procauto_des = st.columns(2)
with col_procauto:
    st_lottie(lottie_process_auto,speed=2,loop=True,quality="high",height=500,width=1000)
with col_procauto_des:
    st.subheader("Python Process Automation Projects:")
    st.write("Click the link below!\n")
    st.markdown("🌐Coming Soon!🌐")