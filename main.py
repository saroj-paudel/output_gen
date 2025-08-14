from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import subprocess
import os


os.makedirs("output",exist_ok=True)

usrname = input("enter username: ").strip()
folder = input("enter folder name: ").strip()
prog = input("enter c | cpp: ").strip()
c=True if prog == "c" else False
exeCmd = ("gcc" if c else "g++")

fpath = input("enter full path of folder: ").strip()
programFiles = [ x for x in os.listdir(path=fpath) if x.endswith(f".{prog}") ]

print("Starting..........\n")

for fname in programFiles:
    img = Image.open("img_op.png")
    draw = ImageDraw.Draw(img)

    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("cascadia_mono.ttf", 19)

    # draw.text((x, y),"Sample Text",(r,g,b))

    draw.text((10,125),f"C:\\Users\\{usrname}\\{folder}> "+ exeCmd + f" {fname} -o {fname.replace(prog,'')[:-1]}",(255,255,255),font=font)

    draw.text((10,150),f"C:\\Users\\{usrname}\\{folder}> .\\{fname.replace(prog,'')[:-1]}",(255,255,255),font=font)

    subprocess.run(['cd',fpath,'&&',exeCmd,fname,"-o" ,fname.replace(prog,'')[:-1]],shell=True)

    result = subprocess.run(['cd',fpath,'&&',f".\{fname.replace(prog,'')[:-1]}"], shell=True, capture_output=True, text=True)

    draw.text((10,175),result.stdout,(255,255,255),font=font)

    print(f"Saving {fname}")

    img.save(f"output/output_{fname.replace(prog,'')[:-1]}.png")

print("\nTask finished !")