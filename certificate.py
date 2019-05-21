#from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw
#img = Image.open("xy.jpg")
#draw = ImageDraw.Draw(img)
#selectfont = ImageFont.truetype("antaro.ttf",size = 60)
#draw.text((10,10),'gaurav',(255,0,0),font=selectfont)
#img.save('certi.pdf',"PDF",resolution=100.0)
################################################################################



# use a truetype font




################################################################################
#
from PIL import Image,ImageFont, ImageDraw
with open('xy.txt', 'r') as file:
    data = file.readlines()
    for name in data:
        image = Image.open("xy.jpg")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("IMissYourKiss-TTF.ttf", 130)
        name = name.replace('\n','')
        draw.text((415,1200), str(name),(154,118,174), font=font)
        image.save(str(name)+'.jpeg',"JPEG",resolution=100.0)
    
