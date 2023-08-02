from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.template.loader import render_to_string
from perfil.models import Conta, Categoria
from .models import Valores
import datetime
import os
from weasyprint import HTML
from django.conf import settings
from io import BytesIO

def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')

        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo
        )

        valores.save()

        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
            entrada_saida = 'Entrada'
        else:
            conta.valor -= int(valor)
            entrada_saida = 'Saída'

        conta.save()

        messages.add_message(request, constants.SUCCESS,
                            f'{entrada_saida} cadastrada com sucesso!')

        return redirect('/extrato/novo_valor')

def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    valores = Valores.objects.all()
    conta_get = request.GET.get('conta')
    if conta_get:
        valores = valores.filter(conta__id=conta_get)
    categoria_get = request.GET.get('categoria')
    if categoria_get:
        valores = valores.filter(categoria__id=categoria_get)
    periodo_get = request.GET.get('periodo')
    date_now = datetime.datetime.now()
    if periodo_get:
        days_ago = date_now - datetime.timedelta(days=int(periodo_get))
        valores = valores.filter(data__gte=days_ago)
    else:
        valores = valores.filter(data__month=date_now.month)
    return render(request, 'view_extrato.html', {'valores': valores, 'contas': contas, 'categorias': categorias})

def exportar_pdf(request):
    date_now = datetime.datetime.now()
    valores = Valores.objects.filter(data__month=date_now.month)
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/extrato.html')
    template_render = render_to_string(path_template, {'valores': valores})
    path_output = BytesIO()
    HTML(string=template_render).write_pdf(path_output)
    path_output.seek(0)
    return FileResponse(path_output, filename='extrato.pdf')