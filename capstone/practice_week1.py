from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640, 480))
new_im.save("example_resized.jpg")
im.rotate(180).resize((640, 480)).save("flipped_and_resized.jpg")