from io import BytesIO, StringIO
from PIL import Image, ImageDraw, ImageFont
import textwrap
from django.core.files.base import ContentFile

# 이후 사용 편의를 위하여 함수 형태로 만들었습니다.
from django.core.files.uploadedfile import InMemoryUploadedFile


def make_image(message, problem_id):
    # Image size
    W = 640
    H = 400
    bg_color = 'rgb(255, 255, 255)'  # 아이소프트존

    # font setting
    font = ImageFont.truetype('arial.ttf', size=15)
    font_color = 'rgb(0, 0, 0)'  # or just 'black'

    image = Image.new('RGB', (W, H), color=bg_color)
    draw = ImageDraw.Draw(image)

    # Text wraper to handle long text
    # 40자를 넘어갈 경우 여러 줄로 나눔
    lines = textwrap.wrap(message, width=60)

    # start position for text
    x_text = 50
    y_text = 50

    # 각 줄의 내용을 적음
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height
        # height는 글씨의 높이로, 한 줄 적고 나서 height만큼 아래에 다음 줄을 적음

    return image

