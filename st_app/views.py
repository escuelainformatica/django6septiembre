from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.

# listado
from st_app.models import Auto, Marca


class Listado(View):
    def get(self,request):
        contexto = {
            'autos':list(Auto.objects.all())
            ,'titulo_pagina':'Listado Autos'
        } # listar todos los autos para mostrarlo en la vista
        return render(request, 'listado.html', contexto)
        pass
    def post(self,request):
        pass


# insertar
class Insertar(View):
    def get(self,request:WSGIRequest):
        contexto = {'auto':Auto(),'marcas':Marca.objects.all()} # listar todos los autos para mostrarlo en la vista
        return render(request, 'insertar.html', contexto)

    def post(self,request:WSGIRequest):
        # aqui quiero crear un objeto Auto
        auto=Auto()
        auto.patente=request.POST['patente']
        auto.propietario=request.POST['propietario']
        auto.id_marca_id=request.POST['id_marca_id']

        Auto.save(auto)  # insertar
        # y luego quiero guardarlo en la base de datos
        contexto = {'auto':auto,'marcas':Marca.objects.all()} # listar todos los autos para mostrarlo en la vista
        return redirect('/auto/') # return render(request, 'insertar.html', contexto)
# modificar

class Modificar(View):
    def get(self,request:WSGIRequest,id):
        auto=Auto.objects.get(id=id)  # obtengo un auto con el id determinado o None si no esta

        contexto = {'auto':auto,'marcas':Marca.objects.all()} # listar todos los autos para mostrarlo en la vista
        return render(request, 'modificar.html', contexto)

    def post(self,request:WSGIRequest,id):
        # la funcion save del modelo sirve para insertar o modificar.
        # si el objeto es creado desde cero, entonces save() inserta
        # si el objeto viene o es leido de la base de datos, entonces save() modifica
        auto = Auto.objects.get(id=id)
        auto.patente = request.POST['patente']
        auto.propietario = request.POST['propietario']
        auto.id_marca_id = request.POST['id_marca_id']
        Auto.save(auto)  # aqui va a modificar el objeto
        return redirect('/auto/')

# eliminar
class Eliminar(View):
    def get(self,request:WSGIRequest,id):
        auto = Auto.objects.get(id=id)  # leo un objeto desde la base de datos
        Auto.delete(auto) # borro el objeto desde la base de datos
        return redirect('/auto/')

    def post(self,request:WSGIRequest,id):
        pass

