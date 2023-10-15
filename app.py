from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Comptable_Marcel_Duon_BLONDE.pdf"
profile_pic = current_dir / "assets" / "pp-rounded.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Blondé Marcel"
PAGE_ICON = ":wave:"
NAME = "Blondé Duon Marcel"
DESCRIPTION = """
Comptable expérimenté, capable de travailler dans le respect de normes prévues par l'OHADA.
"""
EMAIL = "blonde.marcel2023@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/marcel-duon/"
PROJECTS ={
    "🏆 Projet #1 - Tableau de bord global sur l'activité de TRANSIT INTERNATIONAL" : "https://app.powerbi.com/view?r=eyJrIjoiMmYzYWVhNmYtNGNmZS00Y2RlLTk3OTMtNDFjMzhmOGY1MGM0IiwidCI6IjVmZTgzY2M3LTJjNWEtNGIwNC04YmNiLTkyMWQ5ZWQzODgxYiIsImMiOjh9",
    "🏆 Projet #2 - Rapport sur les fournisseurs de TRANSIT INTERNATIONAL" : "https://app.powerbi.com/view?r=eyJrIjoiYzcxYjI3MmQtOTE5OS00Y2MxLTg4Y2UtYmYzMWRhYWRjMzFjIiwidCI6IjVmZTgzY2M3LTJjNWEtNGIwNC04YmNiLTkyMWQ5ZWQzODgxYiIsImMiOjh9",
    "🏆 Projet #3 - Suivi du budget TRANSIT INTERNATIONAL" : "https://app.powerbi.com/view?r=eyJrIjoiNWZlNjJmNWEtYzNjMy00YTM3LWJlMWMtMGQ5Njk1OWQ3NTExIiwidCI6IjVmZTgzY2M3LTJjNWEtNGIwNC04YmNiLTkyMWQ5ZWQzODgxYiIsImMiOjh9",
    "🏆 Projet #4 - Rapport sur les honoraires des medecins d'une clinique" : "https://app.powerbi.com/view?r=eyJrIjoiNzY5ZmU0MjAtZTk2YS00M2I4LTk4ZDItM2FhNGRmY2FmNGVlIiwidCI6IjVmZTgzY2M3LTJjNWEtNGIwNC04YmNiLTkyMWQ5ZWQzODgxYiIsImMiOjh9",
}





st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("Gmail : ", EMAIL)
    st.write("LinkedIn : ", LINKEDIN)


# --- SOCIAL LINKS ---
#st.write("#")
#cols = st.columns(len(LINKEDIN))
#for index, (platform, link) in enumerate(LINKEDIN.items()):
#    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Expériences & Qualifications")
st.write(
    """
- ✅ EXPERIENCE & QUALIFICATIONS #1
- ✅ EXPERIENCE & QUALIFICATIONS #2
- ✅ EXPERIENCE & QUALIFICATIONS #3
- ✅ EXPERIENCE & QUALIFICATIONS #4
    """
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
        """
- ✅ SKILLS #1
- ✅ SKILLS #2
- ✅ SKILLS #3
- ✅ SKILLS #4
    """
)



# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---

st.write("✅", "JOB 1 TITLE")
st.write("✅", "JOB 1 PERIODE")
st.write(
        """
- ✅ JOB 1 DESCRIPTION #1
- ✅ JOB 1 DESCRIPTION #2
- ✅ JOB 1 DESCRIPTION #3
- ✅ JOB 1 DESCRIPTION #4
    """
)

# --- JOB 2 ---

st.write("✅", "JOB 2 TITLE")
st.write("✅", "JOB 2 PERIODE")
st.write(
        """
- ✅ JOB 2 DESCRIPTION #1
- ✅ JOB 2 DESCRIPTION #2
- ✅ JOB 2 DESCRIPTION #3
- ✅ JOB 2 DESCRIPTION #4
    """
)

# --- JOB 3 ---

st.write("✅", "JOB 3 TITLE")
st.write("✅", "JOB 3 PERIODE")
st.write(
        """
- ✅ JOB 3 DESCRIPTION #1
- ✅ JOB 3 DESCRIPTION #2
- ✅ JOB 3 DESCRIPTION #3
- ✅ JOB 3 DESCRIPTION #4
    """
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")