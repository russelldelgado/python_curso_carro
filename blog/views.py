from django.shortcuts import render
from blog.models import Categoria,Post
# Create your views here.



def blog(request):

    posts = Post.objects.all()

    print("PROBANDO LOS POST : ") 
    print (posts)



    return render(request,"blog/blog.html",{"posts":posts})




def categoria(request, categoria_id) : 
    print("-------principio-------")
    categoria = Categoria.objects.get(id=categoria_id)
    print(categoria)
    posts= Post.objects.filter(categorias=categoria)
    print(posts)
    print("-------fin-------")

    return render(request, "blog/categoria.html",{"categoria":categoria,"posts":posts})
