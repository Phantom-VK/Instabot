import requests
import random
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from io import BytesIO

# Important links
url = "https://api.pexels.com/v1/curated"
headers = {"Authorization": "wl80YOohp4aeCMdLTwlt2iFushjwq4biU42LT4tXPBVHoWLyO4Og0eBk"}

# Getting Response
response = requests.get(url, headers=headers).json()

# Generating Random number to pick a random image
num = random.randrange(1, 15)


def give_image(image_number):
    image_id = response['photos'][image_number]["id"]
    photo_url = response['photos'][image_number]["src"]["original"]
    photographer = response['photos'][image_number]["photographer"]

    return image_id, photo_url, photographer


photo_id, link, name, = give_image(num)
print("Photo id : {}\nPhoto link: {}\nClicked by : {}".format(photo_id, link, name))


def get_image(photo_url):
    image_response = requests.get(photo_url)
    raw_image = Image.open(BytesIO(image_response.content))
    return raw_image


def view_image():
    root = tk.Tk()
    root.title("Todays Quote")
    window_width = 1920
    window_height = 1080

    root.geometry(f"{window_width}x{window_height}")
    final_image = get_image(link)

    if final_image:
        # Resize the image to fit the window
        image = final_image.resize((window_width, window_height), Image.LANCZOS)

        # Add text to the image
        draw = ImageDraw.Draw(image)
        text = "Hello there how are you"  # Replace this with the desired text
        font_size = 60
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font=font)
        text_position = ((window_width - text_width) // 2, (window_height - text_height) // 2)
        text_color = (255, 255, 255)  # RGB color of the text (white in this case)
        draw.text(text_position, text, fill=text_color, font=font)

        # Apply image filter (optional, you can remove this line if not needed)
        image = image.filter(ImageFilter.GaussianBlur(radius=3))

        # Convert the image to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Create a Label widget to display the image
        image_label = tk.Label(root, image=photo)

        # Keep a reference to the PhotoImage to prevent it from being garbage collected
        image_label.image = photo

        # Pack the image label to make it visible in the window
        image_label.pack(pady=20)

    else:
        # If no image is available, display an error message
        error_label = tk.Label(text="Error fetching the image from Pexels API.")
        error_label.pack(pady=20)

    root.mainloop()


view_image()
