from django.contrib import admin
from django.urls import path

from api.views import companies_list, company_detail, vacancies_list, vacancy_detail, company_vacancies, top_ten

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', company_detail),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', vacancy_detail),
    path('companies/<int:id>/vacancies', company_vacancies),
    path('vacancies/top_ten/', top_ten)
]