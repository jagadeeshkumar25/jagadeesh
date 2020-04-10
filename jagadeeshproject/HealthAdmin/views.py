
from django.shortcuts import render,redirect
from django.views.generic import View
from HealthAdmin.forms import AdminForm,DiseaseForm,MedicineForm
from HealthAdmin.models import AdminLogin,Disease,Medicine
from useradmin.models import RgistrationModel
from django.contrib import messages


class AdminLoginPage(View):
    def get(self,request):
        return render(request,"HealthAdmin/adminlogin.html")
    def post(self,request):
        un=request.POST['n1']
        pa=request.POST['n2']
        try:
            res=AdminLogin.objects.get(USERNAME=un,PASSWORD=pa)
            return redirect('admin_home_page')
        except AdminLogin.DoesNotExist:
            mess="Invalid username and password"
            messages.success(request,mess)
            return render(request,"HealthAdmin/adminlogin.html")



class AdminHomePage(View):
    def get(self,request):
        return render(request,"HealthAdmin/admin_home.html")


class DiseaseName(View):
    def get(self,request):
        return render(request,"HealthAdmin/disease.html",{"df":DiseaseForm()})
    def post(self,request):
        d=request.POST['DISEASE_NAME']
        s=request.POST['SYMPTOMS']
        d1=Disease(DISEASE_NAME=d,SYMPTOMS=s)
        d1.save()
        return render(request,"HealthAdmin/disease.html",{"df":DiseaseForm,"message":"Details are saved"})


class ViewAllDisease(View):
    def get(self,request):
        qs=Disease.objects.all()
        return render(request,"HealthAdmin/view_all.html",{"data":qs})


class Update(View):
    def post(self,request):
        i=request.POST['i1']
        qs=Disease.objects.get(id=i)
        return render(request,"HealthAdmin/update.html",{"data":qs})


class UpdateDetails(View):
    def post(self,request):
        idno=request.POST['e2']
        disease=request.POST['d1']
        symptoms=request.POST['d2']
        res=Disease.objects.filter(id=idno)
        res.update(DISEASE_NAME=disease,SYMPTOMS=symptoms)
        return redirect('view_all_disease')


class Delete(View):
    def post(self,request):
        del_no=request.POST['i1']
        Disease.objects.filter(id=del_no).delete()
        return redirect('view_all_disease')


class MedicineName(View):
    def get(self, request):
        return render(request, "HealthAdmin/medicine.html", {"mf": MedicineForm()})

    def post(self, request):
        d = request.POST['DISEASE_NAME']
        s = request.POST['SYMPTOMS']
        m = request.POST['MEDICINE_NAME']
        md = request.POST['MEDICINE_DESCRIPTION']

        d1 = Medicine(DISEASE_NAME=d,SYMPTOMS=s,MEDICINE_NAME=m,MEDICINE_DESCRIPTION=md)
        d1.save()
        return render(request, "HealthAdmin/medicine.html", {"mf": MedicineForm, "message": "Details are saved"})


class ViewMedicine(View):
    def get(self, request):
        qs = Medicine.objects.all()
        return render(request, "HealthAdmin/view_all_medicine.html", {"data": qs})


class UpdateMedicine(View):
    def post(self, request):
        i = request.POST['i1']
        qs = Medicine.objects.get(id=i)
        return render(request, "HealthAdmin/update_medicine.html", {"data": qs})


class UpdateMedicineDetails(View):
    def post(self,request):
        idno=request.POST['e2']
        medicine=request.POST['d1']
        md=request.POST['d2']
        res=Medicine.objects.filter(id=idno)
        res.update(MEDICINE_NAME=medicine,MEDICINE_DESCRIPTION=md)
        return redirect('view_all_medicine')


class DeleteMedicine(View):
    def post(self, request):
        del_no = request.POST['i1']
        Medicine.objects.filter(id=del_no).delete()
        return redirect('view_all_medicine')


class ReportUsers(View):
    def get(self, request):
        qs = RgistrationModel.objects.all()
        return render(request, "HealthAdmin/view_all_users.html", {"data": qs})


class ViewAllMedicine(View):
    def get(self, request):
        qs = Medicine.objects.all()
        return render(request, "HealthAdmin/all_medicine.html", {"data": qs})






