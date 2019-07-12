from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView

class BlogLoginView(LoginView):
    template_name = 'accounts/login.html'

class BlogLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

from .forms import RegisterForm
def register(request):
    if request.method == "POST":
        # 회원 가입 완료
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/register_done.html', {'new_user':user})
    else:
            # 회원 가입 창 띄우기
         form = RegisterForm()

    return render(request, 'accounts/register.html', {'form':form})