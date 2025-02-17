from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306

class OLED:
    def __init__(self,fontsize=16):
        #initalize
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
        self.disp.begin()
        self.disp.clear()
        self.width = self.disp.width
        self.height = self.disp.height

        self.image = Image.new('1',(self.width,self.height)) #1 means binary colorscheme
        self.draw = ImageDraw.Draw(self.image)

        self.font = ImageFont.load_default()

    def clearImage(self):
        """clears image and then displays it"""
        self.disp.clear()
        self.disp.display()

    def display(self):
        """displays current image"""
        self.disp.image(self.image)
        self.disp.display()

    def drawPoint(self,pos,bit=1):
        """draws to image, no displaying, bit is 1 or 0"""
        self.draw.point(pos,fill=bit)

    def drawFont(self,word,pos):
        """draws text to image"""
        self.draw.text(pos,word,font = self.font,fill=255)