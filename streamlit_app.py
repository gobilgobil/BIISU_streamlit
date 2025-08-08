import streamlit as st
import base64
from PIL import Image
from pathlib import Path

def zoomed_scrollable_image(image_path, zoom_factor, container_height):
    """
    Displays a zoomed and scrollable image in a container.

    Args:
    image_path (str or Path): The path to the image file.
    zoom_factor (int): The factor by which to zoom the image.
    container_height (int): The height of the scrollable container in pixels.
    """
    try:
        # Open the image to get its original dimensions
        img = Image.open(image_path)
        original_width, original_height = img.size

        # Calculate zoomed dimensions
        zoomed_width = original_width * zoom_factor
        zoomed_height = original_height * zoom_factor

        # Read image file and encode it in base64
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        
        encoded_image = base64.b64encode(image_bytes).decode()
        image_ext = Path(image_path).suffix.lstrip('.')

        # Create the HTML for the scrollable container and the zoomed image
        html_content = f"""
        <div style="overflow: scroll; height: {container_height}px; border: 1px solid #ddd;">
            <img src="data:image/{image_ext};base64,{encoded_image}" 
                 style="width: {zoomed_width}px; height: {zoomed_height}px; display: block;">
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error(f"Image file not found at {image_path}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# --- App Layout ---

# Create a two-column layout: 1/3 for controls, 2/3 for the image
col1, col2 = st.columns([1, 2])

# Content for the left column
with col1:
    st.title("🎈 My new app")
    st.write(
        "This is the control panel area. All text and widgets go here."
    )
    st.write(
        "The image on the right is zoomed 4x and placed in a scrollable window."
    )
    st.write(
        "For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

# Content for the right column
with col2:
    st.subheader("Scrollable Image Viewer")
    # You can replace 'teste.png' with your image file.
    # Make sure the image is in the same folder as your script.
    image_file = 'teste.png'
    zoomed_scrollable_image(image_file, zoom_factor=4, container_height=600)

