# used to generatre the image bullets
from io import BytesIO
from base64 import b64encode
from PIL import Image, ImageDraw

size = 100
color = '#4e5173'
buffer = BytesIO()

image = Image.new('RGBA', (size,size))
draw = ImageDraw.Draw(image)

draw.ellipse((1, 1, size - 1, size - 1), fill=color, outline=color)

image.save(buffer, format="PNG")

base64 = b64encode(buffer.getvalue()).decode()

print(f'data:image/png;base64,{base64}')