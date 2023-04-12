from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    response = JsonResponse(companies_json, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

def company_vacancies(request, id):
    vacancies = Vacancy.objects.filter(company=id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    print(vacancies_json)
    return JsonResponse(vacancies_json, safe=False)