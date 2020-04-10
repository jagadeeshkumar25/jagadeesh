"""HEalthCare_mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from HealthAdmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/',views.AdminLoginPage.as_view(),name="admin_login"),
    path('admin_home_page',views.AdminHomePage.as_view(),name="admin_home_page"),
    path('disease/',views.DiseaseName.as_view(),name="disease"),
    path('view_all_disease/',views.ViewAllDisease.as_view(),name="view_all_disease"),
    path('update/',views.Update.as_view(),name="update"),
    path('update_details/',views.UpdateDetails.as_view(),name="update_details"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('medicine/',views.MedicineName.as_view(),name="medicine"),
    path('view_all_medicine/',views.ViewMedicine.as_view(),name="view_all_medicine"),
    path('update_medicine/',views.UpdateMedicine.as_view(),name="update_medicine"),
    path('update_medicine_details/',views.UpdateMedicineDetails.as_view(),name="update_medicine_details"),
    path('delete_medicine/',views.DeleteMedicine.as_view(),name="delete_medicine"),
    path('view_all_users/', views.ReportUsers.as_view(), name="view_all_users"),
    path('all_medicine/', views.ViewAllMedicine.as_view(), name="all_medicine")

]
