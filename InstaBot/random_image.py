import tkinter as tk
import requests
from PIL import Image, ImageTk
import random
from io import BytesIO

def fetch_random_image(api_key):
    url = "https://api.pexels.com/v1/curated"
    headers = {"Authorization": "wl80YOohp4aeCMdLTwlt2iFushjwq4biU42LT4tXPBVHoWLyO4Og0eBk"}
    params = {"per_page": 1}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "photos" in data and len(data["photos"]) > 0:
        image_url = data["photos"][0]["src"]["large"]
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        return image

def main():
    # Create the main window
    root = tk.Tk()

    # Set the window title
    root.title("Random Pexels Image in Tkinter")

    # Set the window size (width x height)
    window_width = 500
    window_height = 350
    root.geometry(f"{window_width}x{window_height}")

    # Pexels API Key (Sign up for an API key at https://www.pexels.com/api/documentation/)
    api_key = "wl80YOohp4aeCMdLTwlt2iFushjwq4biU42LT4tXPBVHoWLyO4Og0eBk"

    # Fetch a random image using the Pexels API
    image = fetch_random_image(api_key)

    if image:
        # Resize the image to fit the window
        image = image.resize((window_width, window_height), Image.LANCZOS)

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
        error_label = tk.Label(root, text="Error fetching the image from Pexels API.")
        error_label.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
