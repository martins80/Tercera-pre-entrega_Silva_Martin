from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
from django.http import HttpResponse
 
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

def busqueda_productos(request):

    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="articulo buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"]

        datos=Employee.objects.filter(eid__icontains=producto)

        return render(request,"resultado_busqueda.html", {"datos": Employee, "query": Employee})
    else:

        mensaje="No ingresaste ningun dato"

    return HttpResponse(mensaje)