from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
import time
from PIL import Image
import streamlit_option_menu as stop
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
PROFIL = ASSETS / "profile-pic.png"
CV = ASSETS / "CHABRIER_Léo_Curriculum_Vitae.pdf"
DIPLOME = ASSETS / "CHABRIER_Léo_diplôme_ESMA.png"
LOTTIE_ANIMATION = ASSETS / "hello-october.json"

class Main_Interface():
    def __init__(self):
        super().__init__()
        st.set_page_config(layout="wide")

        self.about_me_widget = AboutMe_Widgets()
        self.contacts_widget = GetInTouch_Widgets()
        self.demoreel_widget = Demoreels_Widget()
        self.projects_breakdowns = Projects_Breakdowns()
        self.coding_dev = Coding_Dev()
    
        with open(CSS_FILE) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def buttons(self):
        with st.sidebar:
            selected = stop.option_menu(
                menu_title = "Welcome !",
                options = ["About me","Get in touch","Demoreels","Projects breakdowns","Coding/Development"], # ,"Tutorials","Photography"
                icons = ["house","envelope","camera-reels-fill","list-stars","terminal-fill"], # ,"eyeglasses","camera-fill"
                menu_icon = "cast", 
                default_index = 0,
            )
        if selected == "About me":
            self.about_me_widget.create_panel()

        elif selected == "Get in touch":
            self.contacts_widget.create_panel()

        elif selected == "Demoreels":
            self.demoreel_widget.create_panel()

        elif selected == "Projects breakdowns":
            self.projects_breakdowns.create_panel()

        elif selected == "Coding/Development":
            self.coding_dev.create_panel()
        
    def opening(self, file_path):
        with open(file_path, "r") as gif:
            return json.load(gif)
        
    def run_lottie_animation(self, animation, duration):
        st_lottie(animation, key="entering_animation", height=300, loop=False )
        time.sleep(duration)

class AboutMe_Widgets():

    def create_panel(self):
        st.header('_ABOUT ME_ :', divider='red')

        NAME = "Léo Chabrier"
        DESCRIPTION = """
        I'm a junior 3D generalist freelance, with a master degree in 3D animation and visual effects delivered by ESMA,
        specialised in lookdev/lighting/rendering/compositing/fx/cfx/pipeline/scripting/RND.
        """
        EMAIL = "chabrierleo@outlook.fr"
        SOCIAL_MEDIA = {
            "Mail" : EMAIL, 
            "YouTube": "http://www.youtube.com/@LeoChabrier",
            "LinkedIn": "https://www.linkedin.com/in/l%C3%A9o-chabrier-700328210/",
            "GitHub": "https://github.com/LeoChabrier",
            "ArtStation": "https://www.artstation.com/leochabrier5",
            "Vimeo": "https://vimeo.com/user164854146",
        }
        PROJECTS = {
            "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
            "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
            "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
            "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
        }

        # --- LOAD CSS, PDF & PROFIL PIC ---
        with open(CV, "rb") as pdf_file:
            cv_byte = pdf_file.read()
        profile_pic = Image.open(PROFIL)
        diplome_pic = Image.open(DIPLOME)


        # --- HERO SECTION ---
        layout_column = st.columns([5, 7, 5])
        with layout_column[0]:
            st.image(profile_pic, width=285)
            st.title(NAME)
            st.download_button(
                label=" 📄 Please download my resume.",
                data=cv_byte,
                file_name=CV.name,
                mime="application/octet-stream",
            )
        with layout_column[1]:
            st.image(diplome_pic, width=700)

        st.write('\n')
        expander = st.expander("Details : ", expanded=True)
        with expander:
            st.caption(DESCRIPTION)

        st.write('\n')

        # Use a single loop for both social media links and "Mail"
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            if platform != "Mail":
                cols[index].write(f"[{platform}]({link})")
            else:
                cols[index].write(EMAIL)
                
        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write('\n')
        st.subheader("Experiences & Qualifications :")
        st.write(
            """
        - ✔️ Obtaining an expert diploma in design and production of 3D animation and special effects.
        - ✔️ Co-Director on "Langor" short-film.
        - ✔️ Internship on "Flipou" short-film.
        """
        )

        # --- SKILLS ---
        st.write('\n')
        
        layout_column = st.columns(2)
        with layout_column[0]:
            st.subheader("Soft Skills :")
            st.write(
                """
            - ✔️ Great team-player and displaying strong sense of initiative on tasks.
            - ✔️ Self-motivated and passioned.
            - ✔️ Strong artistic eye and attention to detail in composition, lighting, colors, compositing.
            - ✔️ Capacity to adapt skills to any visual graphic style.
            - ✔️ Great interest in photography.
            - ✔️ Strong adaptability to different pipelines and workflows.
            """
            )
        with layout_column[1]:
            st.subheader("Hard Skills :")
            st.write(
                """
            - ✔️ Ability to intervene in any department of a 3D production, from layout to post-production. 
            - ✔️ Strong knowledges of Python, abitility to automate lots of tasks.
            - ✔️ Good mastery of UI design with Qt Designer/PySide2/PyQt5/TKinter, Streamlit.
            - ✔️ AI development in Autodesk Maya, Nuke and Houdini with OpenAi API and Whisper. 
            - ✔️ Strong understanding on lots of 3D softwares, ability to resolve major technical problems.
            - ✔️ Basic knowledges of C++, HTML, CSS.
            """
            )
        

        # --- SKILLS ---
        st.write('\n')
        st.subheader("Sofwares, Languages and Rendering Engines 🤓👨‍💻 :") 
        layout_column = st.columns(2)
        with layout_column[0]:
            st.write(
                """
            - Python, Mel, Vex
            - Qt Designer, TKinter, Streamlit
            - USD
            - Blender
            - Autodesk Maya
            - Autodesk Mudbox
            - Pixologic Zbrush
            - SideFX Houdini
            - Renderman/Solaris
            - Arnold
            """
            )
        with layout_column[1]:
            st.write(
                """
            - Mantra
            - The Foundry Mari
            - Adobe 3D Substance Painter
            - Adobe Photoshop
            - Adobe InDesign
            - The Foundry Nuke
            - Blackmagic Design Davinci Resolve/Fusion
            - Natron
            - Unreal Engine 5.3
            - E-on Plant Factory
            """
            )

        st.write('\n')

        # --- WORK HISTORY ---
        st.subheader("3D animation work History :")
        st.write("---")
        # # --- Langor
        st.write("🚧", '**Co-director | "Langor" short film**')
        st.write("09/2022 - 07/2023")
        st.write(
            """
        - ► Shots lighting, rendering, compositing. 
        - ► CFX HDA building in Houdini, between Houdini simulations and Maya XGEN. 
        - ► Props/assets look developement.
        - ► Set modeling.
        - ► Development of automatic bridges between softwares.
        - ► R&D on FX/CFX, optimization constraints.
        - ► Production Pipeline development with Python, Maya, Renderman, Houdini, Substance Painter, Mari, Nuke, Blender, E-on PlanFactory.
        - ► Pre-production work on the staging, the design of certain sets, the storyboard and the animatics.
        - ► Working on the initial script.
        """
        )
        st.write("---")
        # --- Flipou
        st.write('\n')
        st.write("🚧", '**Intership | "Flipou" short film**')
        st.write("06/2022 - 07/2022")
        st.write(
            """
        - ► Helps produce special gel spread effects.
        - ► Helps on lighting/rendering and debugging some shots.
        - ► Final compositing of shots.
        """
        )
        st.write("---")
        # --- Studies
        st.write('\n')
        st.write("🚧", "**Student | ESMA**")
        st.write("2018 - 2023")
        st.write(
            """
        - ► Production of a 5-minute short film in a team of 8, over a year.
        - ► Learned to work in a team.
        - ► Learned many industry standard software for 3D animation and VFX.
        - ► Development of artistic and creative sense through various projects.
        """
        )

class GetInTouch_Widgets():
    def create_panel(self):

        if 'submitted' not in st.session_state:
            st.session_state.submitted = False

        st.header('_GET IN TOUCH_ :', divider='red')
        placeholder = st.empty()
        with placeholder.form(key = "my_form", clear_on_submit = True):
            st.text("""
                    Are you nurturing a fresh vision and looking to bring your project to fruition ?
                    I'm ready to accompany you on this journey ! Reach out to me now to discuss your ideas and breathe life into your concept.
                    You need further information ?
                    Feel free to contact me chabrierleo@outlook.fr or by completing the following form.
                """)
            st.write('\n')

            name = st.text_input("Your name : ", key="Name")
            company = st.text_input("Company Name (Optional) : ", key="Company")
            email = st.text_input("Email address : ", key="Email")
            message = st.text_area("Your message : \n\n\n\n", height=500, key="Message")
            allowed = st.checkbox("I accept the above information will be used to contact me. ", value=False)
            submitted = st.form_submit_button("Submit")
                
        if submitted and not st.session_state.submitted and (name != "") and (email != "") and (message != "") and(allowed ==True):
            st.session_state.submitted = True
            placeholder.empty()
            st.write("Your message has been sent. I'll get back to you as soon as possible!")
            self.envoyer_email(name, company, email, message, allowed)
            

            

    def envoyer_email(self, name, company, email, message, allowed):
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()
        expediteur_email = 'l.chabrier@nts.ecolescreatives.com'
        mot_de_passe_expediteur = 'EsmaNantes44'
        sujet = "Nouveau message d'un client sur le site !"
        corps = f"Nom : {name}\nEntreprise : {company}\nE-mail : {email}\nMessage : \n {message}\nRecontact autorisé : {allowed}"
        msg = MIMEMultipart()
        msg.attach(MIMEText(corps, 'plain'))
        msg['Subject'] = sujet
        msg['From'] = expediteur_email
        msg['To'] = 'chabrierleo@outlook.fr'
        server.login(expediteur_email, mot_de_passe_expediteur)
        server.sendmail(expediteur_email, 'chabrierleo@outlook.fr', msg.as_string())
        server.quit()

class Demoreels_Widget():
    def create_panel(self):
        st.header('_DEMOREELS_ :', divider='red')
        cols = st.columns(2)

        with cols[0]:
            st.caption(':red[_Lighting/Compositing Demoreel_] 🪔🕯💡🔦🏮🎥🎬')
            st.video("https://youtu.be/OKj3iOoG1vs")
            lighting_expander = st.expander("Details : ", expanded=True)
            with lighting_expander:
                st.caption("This demoreel contains lots of shots I've worked on during my formation at ESMA. Even if it's a lighting/compositing oriented reel, I've been often working on lot of others aspects.")

        with cols[1]:
            st.caption(':red[_Pipeline TD Demoreel_] 🤓👾🤖')
            st.video("https://youtu.be/oOppd268_i4")
            td_expander = st.expander("Details : ", expanded=True)
            with td_expander:
                st.caption("This demoreel contains lots of tools and applications I've been working on in different softwares like Nuke, Maya, Houdini, Unreal Engine and so on. I've mostly used Python, Qt Designer, and TKinter.")

        second_cols = st.columns(2)

        with second_cols[0]:
            st.caption(':red[_Houdini TD Demoreel_] 🌷🔥💧⚡❄🌊')
            st.title("COMING SOON")
            fx_expander = st.expander("Details : ", expanded=True)
            with fx_expander:
                st.caption("This demoreel contains Houdini pipelines i've been working on, RnD and HDA system i've done.")

        with second_cols[1]:
            st.caption(':red[_Lookdev Demoreel_] 🎨🔎')
            st.title("COMING SOON")
            lookdev_expander = st.expander("Details : ", expanded=True)
            with lookdev_expander:
                st.caption("This demoreel contains lots of assets i've been working on, from modeling to shading.")

    def load_video(self, video):
        video_file = open(video, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

class Projects_Breakdowns():
    def create_panel(self):
        st.header('_PROJECTS BREAKDOWNS_ :', divider='red')
        # Dictionary with years as keys and lists of dictionaries (name and description) as values
        projects_data = {
            "2024": [{"name": "The forgotten robot soldier", "description": "Actually in production"}],
            "2023": [{"name": "Langor short film", "description": "One year production, actually not available, ESMA propriety."}],
            "2022": [{"name": "Madmax Motorcycle", "description": "Modeling, texturing, shading, showroom and VFX integration of a vehicle. This project was useful to learn about Mari, Nuke camera tracking and match move, grading, and CG elements integration."},
                     {"name": "Self-Portrait", "description": ""},
                     {"name": "Claws of Nights", "description": ""}],
            "2021": [{"name": "The insect", "description": ""},
                     {"name": "The timelapse", "description": ""},
                     {"name": "Camera Mapping", "description": ""},
                     {"name": "Anguerran Declin's shop", "description": ""},
                     {"name": "Rolling Teapot", "description": ""}],
            "2020": [{"name": "Still Life", "description": ""},
                     {"name": "Breakfast", "description": ""},
                     {"name": "Living room", "description": ""},
                     {"name": "The film set", "description": ""},
                     {"name": "The hero's lair", "description": ""}],
            "2019": [{"name": "Christmas Project", "description": ""}]
        }

        for year, projects in projects_data.items():
            st.subheader(f'_{year}_ :', divider='red')
            column_sets = st.columns(len(projects))

            for col, project_info in zip(column_sets, projects):
                with col:
                    project_name = project_info["name"]
                    project_description = project_info["description"]

                    st.text(project_name)
                    expander = st.expander("Details : ", expanded=False)
                    with expander:
                        st.caption(project_description)


class Coding_Dev():
    def create_panel(self):
        st.header('_CODING/DEVELOPMENT_ :', divider='red')
        projects_data = {
            "2024": ["Autodesk Maya OpenAI API"],
            "2023": ["Eastern module", "Bake Manager Autodesk Maya/Renderman", "Nuke Camera Mapping Helper"],
        }
        for year, projects in projects_data.items():
            st.subheader(f'_{year}_ :', divider='red')
            column_sets = st.columns(len(projects))

            for col, project in zip(column_sets, projects):
                with col:
                    st.title(project)
                    

if __name__ == "__main__":
    main_app = Main_Interface()
    # anim = main_app.opening(LOTTIE_ANIMATION)
    # main_app.run_lottie_animation(anim, duration = 2)
    main_app.buttons()