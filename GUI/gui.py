
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button
from PIL import Image, ImageTk

# Set up path to the assets folder
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize the main window
window = Tk()
window.geometry("1920x1080")
window.configure(bg="#1E2E47")

# Set up the canvas
canvas = Canvas(
    window,
    bg="#1E2E47",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load entry image
entry_image_1 = ImageTk.PhotoImage(Image.open(relative_to_assets("entry_1.png")))
canvas.create_image(947.5, 134.0, image=entry_image_1)

# Create Text Entry widget
entry_1 = Text(bd=0, bg="#D9E2EB", fg="#000716", highlightthickness=0)
entry_1.place(x=132.0, y=72.0, width=1631.0, height=122.0)

# Function to load button images and create buttons
def create_button(image_file, x, y, width, height, command_text):
    button_image = ImageTk.PhotoImage(Image.open(relative_to_assets(image_file)))
    button = Button(
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(f"{command_text} clicked"),
        relief="flat",
        bg="#1E2E47",
        activebackground="#1E2E47"
    )
    button.image = button_image  # Keep a reference to avoid garbage collection
    button.place(x=x, y=y, width=width, height=height)

# Create all buttons
create_button("button_1.png", 119.0, 267.0, 180.0, 67.0, "button_1")
create_button("button_2.png", 330.0, 267.0, 180.0, 67.0, "button_2")
create_button("button_3.png", 541.0, 267.0, 180.0, 67.0, "button_3")
create_button("button_4.png", 1676.0, 267.0, 100.0, 67.0, "button_4")
create_button("button_5.png", 1551.0, 267.0, 100.0, 67.0, "button_5")
create_button("button_6.png", 946.0, 649.0, 100.0, 100.0, "button_6")
create_button("button_7.png", 1068.0, 649.0, 100.0, 100.0, "button_7")
create_button("button_8.png", 1190.0, 649.0, 100.0, 100.0, "button_8")
create_button("button_9.png", 946.0, 771.0, 100.0, 100.0, "button_9")
create_button("button_10.png", 1068.0, 771.0, 100.0, 100.0, "button_10")
create_button("button_11.png", 1190.0, 771.0, 100.0, 100.0, "button_11")
create_button("button_12.png", 946.0, 527.0, 100.0, 100.0, "button_12")
create_button("button_13.png", 1068.0, 527.0, 100.0, 100.0, "button_13")
create_button("button_14.png", 1190.0, 527.0, 100.0, 100.0, "button_14")
create_button("button_15.png", 946.0, 405.0, 100.0, 100.0, "button_15")
create_button("button_16.png", 1068.0, 405.0, 100.0, 100.0, "button_16")
create_button("button_17.png", 1190.0, 405.0, 100.0, 100.0, "button_17")
create_button("button_18.png", 473.0, 649.0, 100.0, 100.0, "button_18")
create_button("button_19.png", 595.0, 649.0, 100.0, 100.0, "button_19")
create_button("button_20.png", 717.0, 649.0, 100.0, 100.0, "button_20")
create_button("button_21.png", 473.0, 771.0, 100.0, 100.0, "button_21")
create_button("button_22.png", 595.0, 771.0, 100.0, 100.0, "button_22")
create_button("button_23.png", 717.0, 771.0, 100.0, 100.0, "button_23")
create_button("button_24.png", 473.0, 527.0, 100.0, 100.0, "button_24")
create_button("button_25.png", 595.0, 527.0, 100.0, 100.0, "button_25")
create_button("button_26.png", 717.0, 527.0, 100.0, 100.0, "button_26")
create_button("button_27.png", 473.0, 405.0, 100.0, 100.0, "button_27")
create_button("button_28.png", 717.0, 405.0, 100.0, 100.0, "button_28")
create_button("button_29.png", 595.0, 405.0, 100.0, 100.0, "button_29")
create_button("button_30.png", 1322.0, 649.0, 100.0, 100.0, "button_30")
create_button("button_31.png", 1322.0, 771.0, 100.0, 100.0, "button_31")
create_button("button_32.png", 1322.0, 527.0, 100.0, 100.0, "button_32")
create_button("button_33.png", 1322.0, 405.0, 100.0, 100.0, "button_33")
create_button("button_34.png", 1190.0, 894.0, 100.0, 100.0, "button_34")
create_button("button_35.png", 1322.0, 894.0, 100.0, 100.0, "button_35")
create_button("button_36.png", 946.0, 894.0, 100.0, 100.0, "button_36")
create_button("button_37.png", 1068.0, 894.0, 100.0, 100.0, "button_37")
create_button("button_38.png", 1551.0, 527.0, 225.0, 100.0, "button_38")
create_button("button_39.png", 1551.0, 405.0, 225.0, 100.0, "button_39")
create_button("button_40.png", 1551.0, 894.0, 225.0, 100.0, "button_40")
create_button("button_41.png", 119.0, 649.0, 225.0, 100.0, "button_41")
create_button("button_42.png", 119.0, 771.0, 225.0, 100.0, "button_42")
create_button("button_43.png", 119.0, 527.0, 225.0, 100.0, "button_43")
create_button("button_44.png", 119.0, 405.0, 225.0, 100.0, "button_44")

# Disable window resizing and run main loop
window.resizable(True, True)
window.mainloop()