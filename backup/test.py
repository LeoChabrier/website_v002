# import streamlit as st
# from streamlit_elements import elements, mui, html, sync


# IMAGES = [
#     "C:/Users/jdslo/OneDrive/Bureau/website/assets/projects/Langor short film/Langor short film 01.png",
#     "C:/Users/jdslo/OneDrive/Bureau/website/assets/projects/Langor short film/Langor short film 02.JPG",
#     "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
#     "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
#     "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
# ]


# def slideshow_swipeable(images):
#     # Generate a session state key based on images.
#     key = f"slideshow_swipeable_{str(images).encode().hex()}"

#     # Initialize the default slideshow index.
#     if key not in st.session_state:
#         st.session_state[key] = 0

#     # Get the current slideshow index.
#     index = st.session_state[key]

#     # Create a new elements frame.
#     with elements(f"frame_{key}"):

#         # Use mui.Stack to vertically display the slideshow and the pagination centered.
#         # https://mui.com/material-ui/react-stack/#usage
#         with mui.Stack(spacing=2, alignItems="center"):

#             # Create a swipeable view that updates st.session_state[key] thanks to sync().
#             # It also sets the index so that changing the pagination (see below) will also
#             # update the swipeable view.
#             # https://mui.com/material-ui/react-tabs/#full-width
#             # https://react-swipeable-views.com/demos/demos/
#             with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
#                 for image in images:
#                     html.img(src=image, css={"width": "100%"})

#             # Create a handler for mui.Pagination.
#             # https://mui.com/material-ui/react-pagination/#controlled-pagination
#             def handle_change(event, value):
#                 # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
#                 st.session_state[key] = value-1

#             # Display the pagination.
#             # As the index value can also be updated by the swipeable view, we explicitely
#             # set the page value to index+1 (page value starts at 1).
#             # https://mui.com/material-ui/react-pagination/#controlled-pagination
#             mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


# if __name__ == '__main__':
#     st.title("Streamlit Elements Slideshow")
#     st.subheader("Swipeable slideshow")
#     slideshow_swipeable(IMAGES)

# components.html(
#     """
# <!DOCTYPE html>
# <html>
# <head>
# <meta name="viewport" content="width=device-width, initial-scale=1">
# <style>
# * {box-sizing: border-box;}
# body {font-family: Verdana, sans-serif;}
# .mySlides {display: none;}
# img {vertical-align: middle;}

# /* Slideshow container */
# .slideshow-container {
#   max-width: 1000px;
#   position: relative;
#   margin: auto;
# }

# /* Caption text */
# .text {
#   color: #f2f2f2;
#   font-size: 15px;
#   padding: 8px 12px;
#   position: absolute;
#   bottom: 8px;
#   width: 100%;
#   text-align: center;
# }

# /* Number text (1/3 etc) */
# .numbertext {
#   color: #f2f2f2;
#   font-size: 12px;
#   padding: 8px 12px;
#   position: absolute;
#   top: 0;
# }

# /* The dots/bullets/indicators */
# .dot {
#   height: 15px;
#   width: 15px;
#   margin: 0 2px;
#   background-color: #bbb;
#   border-radius: 50%;
#   display: inline-block;
#   transition: background-color 0.6s ease;
# }

# .active {
#   background-color: #717171;
# }

# /* Fading animation */
# .fade {
#   animation-name: fade;
#   animation-duration: 1.5s;
# }

# @keyframes fade {
#   from {opacity: .4} 
#   to {opacity: 1}
# }

# /* On smaller screens, decrease text size */
# @media only screen and (max-width: 300px) {
#   .text {font-size: 11px}
# }
# </style>
# </head>
# <body>

# <h2>Automatic Slideshow</h2>
# <p>Change image every 2 seconds:</p>

# <div class="slideshow-container">

# <div class="mySlides fade">
#   <div class="numbertext">1 / 3</div>
#   <img src="C:/Users/jdslo/OneDrive/Bureau/website/assets/projects/Langor short film/Langor short film 01.png" style="width:100%">
#   <div class="text">Caption Text</div>
# </div>

# <div class="mySlides fade">
#   <div class="numbertext">2 / 3</div>
#   <img src="https://unsplash.com/photos/eHlVZcSrjfg/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Two</div>
# </div>

# <div class="mySlides fade">
#   <div class="numbertext">3 / 3</div>
#   <img src="https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920" style="width:100%">
#   <div class="text">Caption Three</div>
# </div>

# </div>
# <br>

# <div style="text-align:center">
#   <span class="dot"></span> 
#   <span class="dot"></span> 
#   <span class="dot"></span> 
# </div>

# <script>
# let slideIndex = 0;
# showSlides();

# function showSlides() {
#   let i;
#   let slides = document.getElementsByClassName("mySlides");
#   let dots = document.getElementsByClassName("dot");
#   for (i = 0; i < slides.length; i++) {
#     slides[i].style.display = "none";  
#   }
#   slideIndex++;
#   if (slideIndex > slides.length) {slideIndex = 1}    
#   for (i = 0; i < dots.length; i++) {
#     dots[i].className = dots[i].className.replace(" active", "");
#   }
#   slides[slideIndex-1].style.display = "block";  
#   dots[slideIndex-1].className += " active";
#   setTimeout(showSlides, 2000); // Change image every 2 seconds
# }
# </script>

# </body>
# </html> 

#     """,
#     height=600,
# )
# import streamlit as st

# Display the image using st.image
# st.image("langor_seq06_Sh250.png", caption="Your Image", use_column_width=True)

# import streamlit as st
# from PIL import Image

# IMAGES = [
#     "assets/projects/Langor short film/Langor short film 01.png",
#     "assets/projects/Langor short film/Langor short film 02.JPG",
#     "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
#     "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
#     "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
# ]

# def display_images(images, index):
#     image_path = images[index]
    
#     # Open the local image using Image.open
#     if image_path.startswith("http"):
#         st.image(image_path, caption="Your Image", use_column_width=True)
#     else:
#         local_image = Image.open(image_path)
#         st.image(local_image, caption="Your Local Image", use_column_width="always")

# if __name__ == '__main__':
#     st.title("Streamlit Image Slideshow")
#     index = st.slider("Select Image", 0, len(IMAGES) - 1, 0)
#     display_images(IMAGES, index)
    
# import streamlit as st
# from PIL import Image

# IMAGES = [
#     "assets/projects/Langor short film/Langor short film 01.png",
#     "assets/projects/Langor short film/Langor short film 02.JPG",
#     "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
#     "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
#     "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
# ]

# def display_images(images):
#     for image_path in images:
#         # Open the local image using Image.open
#         if image_path.startswith("http"):
#             st.image(image_path, caption="Your Image", use_column_width=True)
#         else:
#             local_image = Image.open(image_path)
#             st.image(local_image, caption="Your Local Image", use_column_width="always")

# if __name__ == '__main__':
#     st.title("Streamlit Vertical Image Alignment")
#     display_images(IMAGES)

# import streamlit as st
# from PIL import Image
# import requests
# from io import BytesIO

# IMAGES = [
#     "assets/projects/Langor short film/Langor short film 01.png",
#     "assets/projects/Langor short film/Langor short film 02.JPG",
#     "https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920",
#     "https://unsplash.com/photos/S5uIITJDq8Y/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTAzMzAz&force=true&w=1920",
#     "https://unsplash.com/photos/E4bmf8BtIBE/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjUyOTEzMzAw&force=true&w=1920",
# ]

# def display_images(images):
#     # Affiche la première image en miniature
#     thumbnail = Image.open(images[0])
#     thumbnail = thumbnail.resize((100, 100))  # Ajustez la taille de la miniature selon vos besoins
#     st.image(thumbnail, caption="Your Thumbnail", use_column_width=False, output_format="JPEG")

#     # Si le bouton est cliqué, affiche toutes les images dans une deuxième fenêtre
#     if st.button("Click to view in full screen"):
#         full_screen_images = []
#         captions = []

#         for image_path in images:
#             if image_path.startswith("http"):
#                 response = requests.get(image_path)
#                 image_content = BytesIO(response.content)
#                 full_screen_images.append(Image.open(image_content))
#             else:
#                 full_screen_images.append(Image.open(image_path))
            
#             # Ajoutez une légende pour chaque image
#             captions.append(f"Caption for {image_path}")

#         # Utilisez st.empty() pour créer un conteneur vide
#         container = st.empty()

#         # Affiche les images dans le conteneur vide
#         container.image(full_screen_images, caption=captions, use_column_width="always")

# if __name__ == '__main__':
#     st.title("Streamlit Image Viewer")
#     display_images(IMAGES)




import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def main():
    st.title("Sliding Image App")

    # Check if the user has clicked on the image button
    is_clicked = st.button("🖼️ Show Image", key="image_button")

    # Display the image based on the click
    if is_clicked:
        show_image()

def show_image():
    # Path to your image file
    image_path = "langor_seq06_Sh250.png"

    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to a base64-encoded string
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Custom HTML and CSS to create a sliding image from the center
    html_code = f"""
        <style>
            .sliding-image {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%) scale(1);
                max-width: 100%;
                max-height: 100%;
                z-index: 9999;
                animation: slideIn 1s forwards;
            }}

            @keyframes slideIn {{
                from {{ transform: translate(-50%, -50%) scale(0); }}
                to {{ transform: translate(-50%, -50%) scale(1); }}
            }}
        </style>

        <img class="sliding-image" src="data:image/png;base64,{image_base64}" alt="Sliding Image">
    """

    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
