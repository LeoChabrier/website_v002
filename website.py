from pathlib import Path
import os
import streamlit as st
import streamlit_option_menu as stop
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyautogui
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
PROFIL = ASSETS / "profile-pic.png"

CV = ASSETS / "CHABRIER_Léo_Curriculum_Vitae.pdf"
DIPLOME = ASSETS / "CHABRIER_Léo_diplôme_ESMA.png"
LOTTIE_ANIMATION = ASSETS / "hello-october.json"
PROJECTS_BREAKDOWNS = ASSETS / "achievements"

# https://discuss.streamlit.io/t/automatic-slideshow/38342/5
# https://github.com/haltakov/simple-photo-gallery/blob/master/README.md
# https://forum.mendix.com/link/space/app-development/questions/104660
# https://medium.com/allenhwkim/close-div-when-clicking-outside-it-97255c20a221

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
            - ✔️ Basic knowledges of C++, HTML, CSS, JavaScript.
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

        hide_img_fs = '''
                        <style>
                        button[title="View fullscreen"]{
                            visibility: hidden;}
                        </style>
                        '''
        st.markdown(hide_img_fs, unsafe_allow_html=True)

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
                    Feel free to contact me at chabrierleo@outlook.fr or by completing the following form.
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
            lighting_expander = st.expander("Details : ", expanded=False)
            with lighting_expander:
                st.caption("This demoreel contains lots of shots I've worked on during my formation at ESMA. Even if it's a lighting/compositing oriented reel, I've been often working on lot of others aspects.")

        with cols[1]:
            st.caption(':red[_Pipeline TD Demoreel_] 🤓👾🤖')
            st.video("https://youtu.be/oOppd268_i4")
            td_expander = st.expander("Details : ", expanded=False)
            with td_expander:
                st.caption("This demoreel contains lots of tools and applications I've been working on in different softwares like Nuke, Maya, Houdini, Unreal Engine and so on. I've mostly used Python, Qt Designer, and TKinter.")

        second_cols = st.columns(2)

        with second_cols[1]:
            st.caption(':red[_Houdini TD Demoreel_] 🌷🔥💧⚡❄🌊')
            st.title("COMING SOON")
            fx_expander = st.expander("Details : ", expanded=False)
            with fx_expander:
                st.caption("This demoreel contains Houdini pipelines i've been working on, RnD and HDA system i've done.")

        with second_cols[0]:
            st.caption(':red[_Lookdev Demoreel_] 🎨🔎')
            st.video("https://youtu.be/_Oi5iOdNe-o")
            lookdev_expander = st.expander("Details : ", expanded=False)
            with lookdev_expander:
                st.caption("This demoreel contains lots of assets i've been working on, from modeling to shading.")

    def load_video(self, video):
        video_file = open(video, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

class Projects_Breakdowns():
    def __init__(self):
        super().__init__()
        self.page_content_placeholder = st.empty()
        
    def create_panel(self):
        with self.page_content_placeholder.container():
            st.header('_PROJECTS BREAKDOWNS_ :', divider='red')
            project_date = os.listdir(PROJECTS_BREAKDOWNS)
            project_date.reverse()
            gray_image = Image.new("RGB", (384, 216))

            for year in project_date:
                st.subheader(f'_{year}_ :', divider='red')
                column_sets = st.columns(4)
                current_year = os.path.join(PROJECTS_BREAKDOWNS, year)

                for col, project in zip(column_sets, os.listdir(current_year)):
                    with col:
                        st.image(gray_image, use_column_width="always")
                        current_project = os.path.join(current_year, project)

                        if "details.txt" in os.listdir(current_project):
                            current_details = os.path.join(current_project, "details.txt")
                            current_details = current_details.replace("\\", "/")

                            with open(current_details, "r") as details:
                                loaded_details = details.read()

                            button_key = f"button{project}"
                            st.button(f"{project}", key=button_key, on_click=lambda: self.show_project_details(loaded_details, project))
        # self.page_content_placeholder.empty()

    def show_project_details(self, loaded_details, project):
        self.page_content_placeholder.empty()
        with self.page_content_placeholder.container():
            st.button("Restart", on_click=self.create_panel)
            st.title(f"About the project _{project}_ :")
            st.write(f"{loaded_details}")


        # projects_data = {
        #     "2024": [{"name": "The forgotten robot soldier", "description": "Actually in production."}
        #             ],
        #     "2023": [{"name": "Langor short film", "description": """
        #               One year production, actually not available, ESMA property.
        #                 Made with Yannis Clerima, Sam Moriceau, Guillaume Boeuf-Couëron, Roxelane Guilbaud, Eve Bermond-Gonnet, Solène Lablonde and Marianne Autret !"""},
        #             {"name": "Discovering", "description": "Discovering of Unreal Engine rendering sytem for animation. More an experimentation than a real project. Assets from Sketchfab and Megascans."},
        #             {"name": "The mines of Mandalore", "description": "First ever animation sequence rendered with Unreal Engine. Discovering of level sequencer, render layers, aovs in Unreal. Compositing in NukeX."},
        #             {"name": "An old friend", "description": "Single image rendered with Unreal Engine, focused on lighting and composition, using Megascans and Sketchfab assets."},
                        
        #                 ],

        #     "2022": [{"name": "Rolling Teapot", "description": "Texturing exercice made using Renderman Teapot, a good way to learn texturing in Mari and photorealistic integration."},
        #              {"name": "Madmax Motorcycle", "description": "Modeling, texturing, shading, showroom and VFX integration of a vehicle. This project was useful to learn about Mari, Nuke camera tracking and match move, grading, and CG elements integration."},
        #              {"name": "Self-Portrait", "description": "Self portrait, initially captured using RealityCapture, then cleaned in Zbrush, retopologized in Maya, sculpted again in Zbrush, textured in Mari, groomed in Houdini, and rendered with Maya and Renderman."},
        #              {"name": "Claws of Nights", "description": """6 weeks production project, made with Jérémie Lebuffe, Manon François, Eve Bermond-Gonnet, Killian Derlin and Emeline Le Fevre.
        #               I've been mostly working on lighting/texturing, compositing and fx !"""}],
        #     "2021": [{"name": "The insect", "description": ""},
        #              {"name": "The timelapse", "description": ""},
        #              {"name": "Camera Mapping", "description": ""},
        #              {"name": "Anguerran Declin's shop", "description": ""}],
        #     "2020": [
        #              {"name": "Breakfast", "description": ""},
        #              {"name": "Living room", "description": ""},
        #              {"name": "The film set", "description": ""},
        #              {"name": "The hero's lair", "description": ""}],

        #     "2019": [{"name": "Christmas Project", "description": ""},
        #              {"name": "Still Life", "description": ""}]
        # }

        # for year, projects in projects_data.items():
        #     st.subheader(f'_{year}_ :', divider='red')
        #     column_sets = st.columns(4)

        #     for col, project_info in zip(column_sets, projects):
        #         with col:
        #             project_name = project_info["name"]
        #             project_description = project_info["description"]
        #             image_extensions = [".jpg", ".png"]
        #             image_found = False
        #             for ext in image_extensions:
        #                 image_path = str(PROJECTS_BREAKDOWNS / project_name / f"{project_name} 01{ext}")
        #                 if os.path.exists(image_path):
        #                     image = Image.open(image_path)
        #                     st.image(image, use_column_width="always")
        #                     image_found = True
        #                     break
        #             if not image_found:
        #                 gray_image = Image.new("RGB", (384, 216))
        #                 st.image(gray_image, use_column_width="always")

        #             hide_img_fs = '''
        #                 <style>
        #                 button[title="View fullscreen"]{
        #                     visibility: hidden;}
        #                 </style>
        #                 '''
        #             st.markdown(hide_img_fs, unsafe_allow_html=True)
        #             st.button(project_name, key = f"button{project_name}")
                    
        #             st.markdown(
        #                 """
        #                 <style>
        #                 div.stButton > button {
        #                     display: block;
        #                     margin: auto;
        #                 }
        #                 </style>
        #                 """,
        #                 unsafe_allow_html=True,
        #             )

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
    main_app.buttons()
