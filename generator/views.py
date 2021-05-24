from django.shortcuts import render

from django.http import HttpResponse
from PIL import Image
import pytesseract
from .serializers import imageSerializer, imgTotextSerializer
from rest_framework.generics import (CreateAPIView)
from generator.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from generator.refine_text import *
from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import monitor
from .PK_From_DB import *
from .make_blank import Create_Blank
from .make_image import make_image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
import EVM.settings
from io import BytesIO, StringIO

import base64

def home(request):
    _email = request.session.get('user')
    problem_num = problem.objects.filter(ID=_email).count()
    context = {'email': _email, 'PN': problem_num}
    return render(request, 'generator/Dashboard.html', context)

#사진 업로드 하는 창 부름
def Upload_Photo(request):
    _email = request.session.get('user')
    problem_num = problem.objects.filter(ID=_email).count()
    context = {'email': _email, 'PN': problem_num}
    return render(request, 'generator/Upload_Photo.html', context)

#업로드 된 문제에 관한 정보들을 갖고, problem DB에 저장. 그리고 scan_from_DB로 OCR 인식.
def create(request):
    if(request.method == 'POST'):
        _problem_id = GET_PK("problem")
        _problem_type = request.POST['problem_type']
        _blank_num = int(request.POST['blank_num'])
        _answer = int(request.POST['answer'])
        _info = request.POST['info']
        _email = request.session.get('user')
        _user = monitor.objects.get(email=_email)

        for img in request.FILES.getlist('imgs'):
            _imgs = img

        _problem = problem(problem_id = _problem_id,ID=_user,type=_problem_type, image=_imgs,
                           blank_num=_blank_num, answer=_answer, info=_info).save()
        context = scan_img_from_DB(_problem_id)
        context['email']=_email
        context['id']=_problem_id

        request.session['problem_id'] = _problem_id

        return render(request, 'generator/OCR.html', context)

    else:
        return render(request, 'generator/Upload_Photo.html')

def show_problem(request):
    _email = request.session.get('user')
    context = {}
    context['email'] = _email

    _text = request.POST.get('text', '')
    _problem_id = request.session.get('problem_id','')

    _problem_text = Create_Blank(_text)

    _img = make_image(_problem_text, _problem_id)

    # 빈칸 텍스트, 빈칸 텍스트 이미지화 한 것 DB에 저장.
    _update_prob = problem.objects.get(problem_id=_problem_id)

    _img_name = "\\results\\"+_problem_id+"_blank.png"
    _img_path = EVM.settings.MEDIA_ROOT + _img_name


    _img.save(_img_path)

    _update_prob.problem_image = _img_path
    _update_prob.text = _text
    _update_prob.blank_text = _problem_text

    _update_prob.save()

    context['problem'] = _update_prob

    return render(request, 'generator/Show_BlankText.html', context)

# 사용자로부터 이미지 받으면 이를 DB에 저장.
class ImageCreateAPIView(CreateAPIView):
    serializer_class = imageSerializer
    queryset = problem.objects.all()


#DB에서 해당 problem_id 찾은 후, 해당 problem에서 지문 추출 후, 정제까지 완료. 정제된 지문 앱으로 전달.
def scan_img_from_DB(id):
    temp_problem = problem.objects.get(problem_id=id)
    img = Image.open(temp_problem.image)
    one_text = pytesseract.image_to_string(img, lang='kor+eng')

    refined_text = ""

    #순서 유형 지문 정제
    if(temp_problem.type=="order"):
        refined_text = type_order(one_text, temp_problem.answer)
    elif(temp_problem.type=="blank"):
        refined_text = type_blank(one_text, temp_problem.answer)
    elif (temp_problem.type == "insert"):
        refined_text = type_insert(one_text, temp_problem.answer)

    temp_problem.text = refined_text
    temp_problem.save()

    context = {'problem':temp_problem}
    return context

# 사용자로부터 최종 text 받아서 keyword 추출 후, blank 생성.
def make_blank_in_text(request, id):
    temp_problem = problem.objects.get(problem_id=id)

# 사용자가 생성한 problem들 보여주기.
def show_UserProblem(request):
    _email = request.session.get('user')
    context = {}
    context['email'] = _email

    candidates = problem.objects.filter(ID=_email)
    context['candidates'] = candidates

    return render(request, 'generator/Show_UserProblemList.html', context)



