from django.shortcuts import render

from django.http import HttpResponse
from PIL import Image
import pytesseract
from .serializers import imageSerializer, imgTotextSerializer
from rest_framework.generics import (CreateAPIView)
from generator.models import problem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from generator.refine_text import *

def index(request):
    return HttpResponse("EVM Project")

# 사용자로부터 이미지 받으면 이를 DB에 저장.
class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = problem.objects.all()

#DB에서 해당 problem_id 찾은 후, 해당 problem에서 지문 추출 후, 정제까지 완료. 정제된 지문 앱으로 전달.
@api_view(['GET'])
def scan_img_from_DB(request, id):
    temp_problem = problem.objects.get(problem_id=id)
    img = Image.open(temp_problem.image)
    one_text = pytesseract.image_to_string(img, lang='kor+eng')

    refined_text = ""

    #순서 유형 지문 정제
    if(temp_problem.type.type=="order"):
        refined_text = type_order(one_text, temp_problem.answer)
    elif(temp_problem.type.type=="blank"):
        refined_text = type_order(one_text, temp_problem.answer)
    elif (temp_problem.type.type == "insert"):
        refined_text = type_insert(one_text, temp_problem.answer)

    temp_problem.text = refined_text
    temp_problem.save()

    serializer = imgTotextSerializer(temp_problem)
    return Response(serializer.data)

# 사용자로부터 최종 text 받아서 keyword 추출 후, blank 생성.
def make_blank_in_text(request, id):
    temp_problem = problem.objects.get(problem_id=id)



