# from PIL import Image, ImageFilter
from PIL import Image

# img = Image.open("./Pokedex/pikachu.jpg")
# # filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert("L")

# # resize = filtered_img.resize((300, 300))
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("grey.png", "png")

img = Image.open("./astro.jpg")
img.thumbnail((400, 200))

img.save("thumb.jpg")
