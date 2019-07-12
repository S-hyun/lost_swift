from django.shortcuts import render

# Create your views here.

# 한줄 주석

"""
여러 줄 주석 쓰는 방법
"""


"""
MVC 패턴
Model - 데이터베이스를 클래스와 매칭시키는 것 (ORM) (DBA)
View - HTML, CSS, JS (Frontend Developer)
Controller - 실제 로직이 동작하는 코드 부분 (Backend Developer)
 
MVC -> MTV
Model - Model
Template - View
View - Controller
 
1. 모델 작성(설계) - 데이터베이스에 무슨 자료를 어떤 형태롤 저장할 것이냐? Models.py
blog - 글 작성자, 제목, 내용, 태그, 작성일, 수정일

2. 뷰(페이지, 기능) - 글 작성, 수정, 삭제, 목록 같은 기능 혹은 페이지 View.py
2-1 페이지(사용자가 보는 화면)가 필요하다? Template 작성(html, css, js) - .html

3. URL 연결(설계, 라우팅 테이블 만들기) 
"""

# 뷰(페이지, 기능)
# 1. 함수형 뷰 - 프로그래머 마음대로 작성하고 싶을 때는 함수형을 쓴다.
# 2. 클래스형 뷰 - 관례적으로 많이 사하는 기능은 이미 구현된 제네릭 뷰를 상속받아서 사용한다.


# 함수형 뷰는 첫번째 매개변수가 무조건 request 객체

from django.http import HttpResponse
# import django.http.HttpResponse

def welcome(request):
    # 뷰에서는 파이썬 코드로 하고 싶은거 한다.
    # 맨 마지막 줄에서는 항상 response를 해줘야 한다.

    return HttpResponse("Hello World")


# CRUDL

"""
데코레이터 : 함수 꾸밈자 - 함수 실행 전에 다른 함수를 실행하고 싶을 때
믹스인 : 클래스에 뭔가 기능을 추가하고 싶을 때
"""
from django.contrib.auth.mixins import LoginRequiredMixin
#믹스인은 상속할 깨 제네릭 뷰보다 앞에 있어야 한다.
from django.views.generic.edit import CreateView
from .models import Blog

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    success_url = '/'
    template_name = 'blog/create.html'

    def form_valid(self, form):
        # 글쓴이 설정 해주기
        form.instance.writer_id = self.request.user.id
        return super().form_valid(form)

from django.views.generic.list import ListView
'''
동작 : 뷰
뷰를 찾아가려면 : URL
동작한 결과 화면이 나타나려면 : Template
'''
class BlogList(ListView):
    model = Blog
    template_name = 'blog/list.html'

from django.views.generic.detail import DetailView
class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/detail.html'

from django.views.generic.edit import UpdateView, DeleteView
class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/update.html'

class BlogDelete(DeleteView):
    model = Blog
    success_url = '/'
    template_name = 'blog/delete.html'