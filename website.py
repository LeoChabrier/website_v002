
import streamlit as st
import streamlit_option_menu
import streamlit.components.v1 as components
from smtplib import SMTP
from PIL import Image
from pathlib import Path
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
PROFIL = ASSETS / "profile-pic.png"
CV = ASSETS / "CHABRIER_Léo_Curriculum_Vitae.pdf"
DIPLOME = ASSETS / "CHABRIER_Léo_diplôme_ESMA.png"
LOTTIE_ANIMATION = ASSETS / "hello-october.json"
PROJECTS_BREAKDOWNS = ASSETS / "achievements"

# html_file = open("index.html", "r", encoding='utf-8')
# source_code = html_file.read()
# components.html(source_code)

class Main_Interface():
    def __init__(self):
        super().__init__()
        st.set_page_config(page_title = "Léo Chabrier Website", layout="wide")

        self.about_me_widget = AboutMe_Widgets()
        self.contacts_widget = GetInTouch_Widgets()
        self.demoreel_widget = Demoreels_Widget()
        self.projects_breakdowns = Projects_Breakdowns()
        self.coding_dev = Coding_Dev()

        with open(CSS_FILE) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def buttons(self):
        with st.sidebar:
            selected = streamlit_option_menu.option_menu(
                menu_title = "Welcome !",
                options = ["About me","Get in touch","Demoreels","Projects breakdowns"],# "Coding/Development","Tutorials","Photography"],
                icons = ["house","envelope","camera-reels-fill","list-stars"], #,"terminal-fill","eyeglasses","camera-fill"],
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

        # elif selected == "Coding/Development":
        #     self.coding_dev.create_panel()

class AboutMe_Widgets():

    def create_panel(self):
        st.header('_ABOUT ME_ :', divider='red')

        NAME = "Léo Chabrier"
        DESCRIPTION = """
        I'm a junior 3D generalist, with a master degree in 3D animation and visual effects delivered by ESMA,
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
        # diplome_pic = Image.open(DIPLOME)


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
        # with layout_column[1]:
        #     st.image(diplome_pic, width=700)

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
            - ✔️ Strong artistic eye and attention to detail in composition, light, colors.
            - ✔️ Capacity to adapt skills to any visual graphic style.
            - ✔️ Great interest in photography.
            - ✔️ Strong adaptability to different pipelines and workflows.
            """
            )
        with layout_column[1]:
            st.subheader("Hard Skills :")
            st.write(
                """
            - ✔️ Ability to intervene in any department of a 3D production. 
            - ✔️ Strong knowledges of Python, abitility to automate lots of tasks.
            - ✔️ Good mastery of UI design with Qt Designer/PySide2/PyQt5/TKinter, Streamlit.
            - ✔️ AI development Maya, Nuke and Houdini with OpenAi API and Whisper. 
            - ✔️ Strong understanding on lots of 3D softwares, ability to solve technical problems.
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
        col = st.columns([1,8,1])
        with col[1]:
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
        server = SMTP("smtp-mail.outlook.com", 587)
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
            st.caption(':red[_Lighting Demoreel_] 🪔🕯💡🔦🏮🎥🎬')
            st.video("https://www.youtube.com/watch?v=TXWRN_PdKg0")
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
            st.caption(':red[_Compositing Demoreel_] 🎥📹🎦')
            st.title("COMING SOON")
            compositing_expander = st.expander("Details : ", expanded=False)
            with compositing_expander:
                st.caption("This demoreel contains mostly some VFX shots i've been working on in compositing.")

        with second_cols[0]:
            st.caption(':red[_Lookdev Demoreel_] 🎨🔎')
            st.video("https://www.youtube.com/watch?v=zIsjDpLtXro")
            lookdev_expander = st.expander("Details : ", expanded=False)
            with lookdev_expander:
                st.caption("This demoreel contains lots of assets i've been working on, from modeling to shading.")

        third_cols = st.columns(2)

        with third_cols[0]:
            st.caption(':red[_Houdini TD Demoreel_] 🌷🔥💧⚡❄🌊')
            st.title("COMING SOON")
            fx_expander = st.expander("Details : ", expanded=False)
            with fx_expander:
                st.caption("This demoreel contains Houdini pipelines i've been working on, RnD and HDA system i've done.")

        

    def load_video(self, video):
        video_file = open(video, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

class Projects_Breakdowns():
    def __init__(self):
        super().__init__()

    def get_all_image_files(self, directory):
        all_files = []
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    all_files.append(os.path.join(dirpath, filename))
        return all_files

    def get_text_file(self, directory):
        text_files = []
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.lower().endswith(('.txt', ".json")):
                    text_files.append(os.path.join(dirpath, filename))
        return text_files
    
    def create_panel(self):
        st.markdown(
            """
            <style>
            div.stButton > button {
                width: 100%;
                display: block;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('''
                    <style>
                    button[title="View fullscreen"]{
                        visibility: hidden;}
                    </style>
                    ''', unsafe_allow_html=True)

        subdirectories = [d for d in next(os.walk(PROJECTS_BREAKDOWNS))[1]]
        year_subfolders_dict = {}

        for year_folder in subdirectories:
            year_folder_path = os.path.join(PROJECTS_BREAKDOWNS, year_folder)
            sub_folders = next(os.walk(year_folder_path))[1]
            sub_folders.sort()
            year_subfolders_dict[year_folder] = sub_folders

        year_subfolders_dict = dict(sorted(year_subfolders_dict.items(), key=lambda item: item[0], reverse=True))
        all_files = self.get_all_image_files(PROJECTS_BREAKDOWNS)
        text_files = self.get_text_file(PROJECTS_BREAKDOWNS)

        st.header('*PROJECTS BREAKDOWNS* :', divider='red')


        button_container = st.empty()
        visible_buttons = []
        clicked_button_label = None
        with button_container.container():
            for year, subdir in year_subfolders_dict.items():
                st.subheader(year, divider='red')
                columns = st.columns(4)
                for col, sub_item in zip(columns, subdir):
                    with col:
                        matching_files = [file for file in all_files if sub_item in file]
                        matching_files.sort()
                        project_name = sub_item.split('_')[1]
                        if matching_files:
                            image_path = matching_files[0]
                            new_width = 1920
                            new_height = 1080
                            original_image = Image.open(image_path)
                            left = (original_image.width - new_width) // 2
                            top = (original_image.height - new_height) // 2
                            right = (original_image.width + new_width) // 2
                            bottom = (original_image.height + new_height) // 2
                            cropped_image = original_image.crop((left, top, right, bottom))
                            reduced_width = cropped_image.width // 10
                            reduced_height = cropped_image.height // 10
                            reduced_image = cropped_image.resize((reduced_width, reduced_height))

                            st.image(reduced_image, use_column_width=True)
                        else : 
                            st.image(Image.new("RGB", (1920, 1080)))

                        if col.button(project_name, key=f'{project_name}_button'):
                            clicked_button_label = project_name
                            break
                        
        if clicked_button_label:
            col = st.columns([2,6,2])
            visible_buttons.append(clicked_button_label)
            button_container.button("Back to gallery")

            st.session_state.current_subdirectory = clicked_button_label

        for subdir in visible_buttons:
            matching_files = [file for file in all_files if subdir in file]
            matching_files.sort()
            text_file = [file for file in text_files if subdir in file]

            loaded_details = None
            loaded_link = None

            for text in text_file:
                try :
                    text = text.replace("\\", "/")
                except :
                    pass
                if str(text.split('/')[-1]) == "details.txt":
                    with open(text, "r") as details:
                        loaded_details = details.read()
                else:
                    try:
                        with open(text, "r") as link:
                            loaded_link = link.readlines()
                    except:
                        pass


            with col[1]:
                st.write(f"About _{subdir}_ :\n\n{loaded_details}")
                for i in matching_files:
                    try : 
                        i = i.replace("\\", "/")
                    except :
                        pass
                    name = str(i.split('/')[-1]).split('.')[0]
                    image = Image.open(i)
                    st.image(image, use_column_width="always", caption=name)
                
                if loaded_link:
                    for link in loaded_link:
                        st.video(link.split('\n')[0])

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
