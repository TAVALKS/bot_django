import xlwt
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Calltrack_lite

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

    rows = Calltrack_lite.objects.all().values_list(
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