import pandas as pd
from PIL import Image, ImageDraw, ImageFont

url= 'lists.csv'
df=pd.read_csv(url)

print("1st 10 rows")
d=df.head(10)
print(d)


name_list =df["names"].tolist()
for i in name_list:
    im = Image.open('c3.jpg')
    d = ImageDraw.Draw(im)
    location = (100, 398)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 120)
    d.text(location, i, fill = text_color, font = font)
    im.save("certificate_" + i + ".pdf")