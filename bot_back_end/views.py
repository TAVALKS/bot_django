import xlwt
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

    columns = ['id_rec', 'text', 'text_lemm', 'innumber', 'region',
               'dial_route', 'key_words']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Calltrack_lite.objects.all().values_list(
        'id_rec', 'text', 'text_lemm', 'innumber', 'region',
        'dial_route', 'key_words')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response