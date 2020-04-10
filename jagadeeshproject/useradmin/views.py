
from django.shortcuts import render,redirect
from django .views.generic import View
from useradmin.forms import RegistrationForm
from useradmin.models import RgistrationModel,UserAdmin,UserLoginForm
from django.contrib import messages
from HealthAdmin.models import AdminLogin,Medicine




class REgistrationForm(View):
    def get(self,request):
        return  render(request,"useradmin/registeration.html",{"rf":RegistrationForm()})
    def post(self,request):
        # print("hi")
        # # rf=request.POST['s1']
        # print("hello")
        # # if rf=="rf":
        #   print("hai")
          rf=RegistrationForm()

          rf=RegistrationForm(request.POST)
          if rf.is_valid():
               print("hm")
               fn=request.POST['First_Name']
               ln=request.POST['Last_Name']
               age=request.POST['Age']
               gen=request.POST['Gender']
               add=request.POST['Address']
               user=request.POST['UserName']
               password=request.POST['Password']
               RgistrationModel(First_Name=fn,Last_Name=ln,Age=age,Gender=gen,Address=add,UserName=user,Password=password).save()
               UserAdmin(USERNAME=user,PASSWORD=password).save()
               mess="Details are saved in databse"
               messages.success(request,mess)
               return render(request, "useradmin/registeration.html",
                             {"rf": RegistrationForm})

          else:
            return render(request, "useradmin/registeration.html", {"rf": RegistrationForm,"error":"please check details are invalid"})


class UserHomePage(View):
    def get(self,request):
        return render(request,"useradmin/user_home_page.html")


class UserLoginPage(View):
    def get(self,request):
        return  render(request,"useradmin/user_login_page.html",{"uf":UserLoginForm()})
    def post(self,request):
        username=request.POST['n1']
        password=request.POST['n2']
        try:
             res=UserAdmin.objects.get(USERNAME=username,PASSWORD=password)
             return redirect('user_home_page')
        except UserAdmin.DoesNotExist:
            return  render(request,"useradmin/user_login_page.html",{"error":"Invalid username and password"})


class AllRegisterUsers(View):
    def get(self, request):
        qs = RgistrationModel.objects.all()
        return render(request, "useradmin/view_all_registerusers.html", {"data": qs})


class UserMedicineData(View):
    def get(self,request):
        return  render(request,"useradmin/view_all_user_medicine.html")


class SearchMedicine(View):
    def get(self,request):
        return  render(request,"useradmin/search_medicine.html")
    def post(self,request):
        disease=request.POST['d1']
        qs=Medicine.objects.get(DISEASE_NAME=disease)
        return  render(request,"useradmin/search_medicine.html",{"data":qs})


class ChangePassword(View):
    def get(self,request):
        return render(request,"useradmin/changepassword.html")

    def post(self,request):
        old=request.POST['p1']
        print(old)
        new=request.POST['p2']
        print(new)
        res=RgistrationModel.objects.filter(Password=old)
        print(res)
        res.update(Password=new)
        us=UserAdmin.objects.filter(PASSWORD=old)
        print(us)
        us.update(PASSWORD=new)
        return  redirect('change_password')


