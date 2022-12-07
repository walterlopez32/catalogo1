from django.shortcuts import render

template_name = "index.html"
contexto = {
    
}
def inicio(requets):
    return render(requets, template_name,contexto)
