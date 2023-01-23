"""Importing Pillow module"""
from PIL import Image, ImageFont, ImageDraw


def img_cr(word):
    """Function to add on image text of word"""
    font_text = ImageFont.truetype('Fonts/Lato-Black.ttf', 120)
    img = Image.new("RGB", (600, 600), "White")
    draw = ImageDraw.Draw(img)
    draw.text((300, 300), word, fill="Black", anchor="ms", font=font_text)
    img.save("Images/img_done.png")

#DeFakto
