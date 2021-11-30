import xlwt
import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Calltrack_lite
from django.http import JsonResponse
from .models import Departs, Category_managers
import datetime

def index(request):
    return render(request, 'bot_back_end/index.html')


def about(request):
    return render(request, 'bot_back_end/about.html')


def export_calltrack_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="calltrack.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('calltrack')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'время', 'фраза клиента', 'вх.номер', 'регион',
               'доб.номер', 'ключевые слова']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    start_date = request.GET.get('from', None)
    end_date = request.GET.get('to', None)
    end_date = str(datetime.datetime.strptime(end_date, '%Y-%m-%d')+datetime.timedelta(days=1))

    rows = Calltrack_lite.objects.filter(date_time_calling__range=(start_date, end_date)).values_list(
        'id_rec', 'date_time_calling', 'text', 'innumber', 'region',
        'dial_route', 'key_words')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime.datetime):
                date_time = row[col_num].strftime('%Y-%m-%d %H:%M:%S')
                ws.write(row_num, col_num, date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def get_depart_or_name_manager(request):
    dial_route = request.GET.get('dial_route')

    if Departs.objects.filter(depart_added_phone_number=dial_route):
        name = Departs.objects.get(depart_added_phone_number=dial_route).depart_name
    elif Category_managers.objects.filter(phone_number=dial_route):
        name = Category_managers.objects.filter(phone_number=dial_route).values_list('name_man')[0][0]
    else:
        name = dial_route
    response = JsonResponse({'name': name})
    print('response:', response)
    return response