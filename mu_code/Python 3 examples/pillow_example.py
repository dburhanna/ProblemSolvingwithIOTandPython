from PIL import Image, ImageDraw, ImageFont
import sys

#use try and except to open a picture file
try:
    picture = Image.open("images/peru.jpeg")
    print("File is open...\n")
except:
    print("Unable to load image")
    sys.exit(1)
width,height = picture.size
print(width)
print(height)

# using Image.Draw to get picture ready to draw on
idraw = ImageDraw.Draw(picture)
# text to draw on picture
text = 'cheeseburgers are yummy'
print(text)
print()
# choose a font to draw on picture
font = ImageFont.truetype("fonts/404ERROR.TTF", size=100)
# add the text to the picture
print("adding text to image...\n")
idraw.text((200, 500), text,(149,165,166), font = font)

#save the modified file with a new name AND file type
print("saving file now...\n")
picture.save('images/peru_watermarked.png')
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!
#adding a comment at the END of the file!!!