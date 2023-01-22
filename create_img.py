from PIL import Image, ImageFont, ImageDraw


def img_cr(word):
    font_text = ImageFont.truetype('Lato-Black.ttf', 120)
    im = Image.new("RGB", (600, 600), "White")
    d = ImageDraw.Draw(im)
    # d.line(((0, 100), (600, 300)), "gray")
    # d.line(((300, 0), (300, 600)), "gray")
    d.text((300, 300), word, fill="Black", anchor="ms", font=font_text)
    im.save("img_done.png")
    # with Image.open("img.png") as im:
    #     image_editable = ImageDraw.Draw(im)
    #
    #     image_editable.text((213, 208), word, (0, 0, 0), font=font_text)
    #     im.save("img_done.png")

