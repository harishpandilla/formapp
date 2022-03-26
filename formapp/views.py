from django.shortcuts import render
from django.views import View
from .models import Reg
from .forms import RegForm
from django.http import HttpResponse
class RegInput(View):
    def get(sellf,request):
        rf=RegForm()
        con_dict={"regform":rf}
        return render(request,"reginput.html",con_dict)
class Register(View):
    def post(self,request):
        rf=RegForm(request.POST)
        if rf.is_valid():
            r=Reg(firstname=rf.cleaned_data['firstname'],
                  lastname=rf.cleaned_data['lastname'],
                  username=rf.cleaned_data['username'],
                  password=rf.cleaned_data['password'],
                  cpassword=rf.cleaned_data['cpassword'],
                  mailid=rf.cleaned_data['mailid'],
                  mobno=rf.cleaned_data['mobno'])
            r.save()
            return HttpResponse("successfully inserted data")
