from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Pages

formulario ="""
<form action= "" method="POST">
	Nombre: <input type="text" name="nombre">
	Pagina: <input type="text" name="pagina">
	<input type="submit" value="Enviar">
</form>
"""
@csrf_exempt
def barra(request):
	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + ' <a href="/logout"> Logout</a>'
	else:
		logged = 'Not logged in. <a href="/login"> Login</a>'
	
	if request.method == "POST":
		g = Pages(name = request.POST['nombre'], page = request.POST['pagina'])
		g.save()
	
	salida = logged

	lista = Pages.objects.all()
	salida += "<ul>"
	for page in lista:
		salida += '<li><a href="page/' + str(page.id) + '">' + page.name + '</a>'
	salida += "</ul>"

	if request.user.is_authenticated():
		salida += formulario

	return HttpResponse(salida)

@csrf_exempt
def pages(request, numero):
	if request.method == "POST":
		g = Pages(name = request.POST['nombre'], page = request.POST['pagina'])
		g.save()
	try:
		page = Pages.objects.get(id=int(numero))
	except Pages.DoesNotExist:
		return HttpResponseNotFound('<h1>' + numero + ' not found.</h1>')
	return HttpResponse(page.name + " " + str(page.page))