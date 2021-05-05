from django.shortcuts import render

from django.http import HttpResponse
from PIL import Image
import pytesseract
from .serializers import imageSerializer, imgTotextSerializer
from rest_framework.generics import (CreateAPIView)
from generator.models import problem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from generator.refine_text import type_order

def index(request):
    return HttpResponse("EVM Project")

class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = problem.objects.all()

@api_view(['GET'])
def scan_img_from_DB(request, id):
    temp_problem = problem.objects.get(problem_id=id)
    img = Image.open(temp_problem.image)
    one_text = pytesseract.image_to_string(img, lang='kor+eng')

    refined_text = ""

    #순서 유형 지문 정제
    if(temp_problem.type.type=="order"):
        refined_text = type_order(one_text, temp_problem.answer)

    temp_problem.text = refined_text
    temp_problem.save()

    serializer = imgTotextSerializer(temp_problem)
    return Response(serializer.data)


