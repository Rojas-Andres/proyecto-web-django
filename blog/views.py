from django.shortcuts import render
from blog.models import Categoria,Post 
# Create your views here.

def blog(req):
    posts = Post.objects.all()
    return render(req,"blog/blog.html",{"posts":posts})
def categoria(req,categoria_id):
    print(categoria_id,type(categoria_id))
    categorias = Categoria.objects.get(id=categoria_id)
    print(categorias)
    posts = Post.objects.all()
    print(posts)
    posts = Post.objects.filter(categorias=categorias)
    #print("\n\n categorias {} \n Post : {}",categorias,posts)
    return render(req,"blog/categoria.html",{"categoria":categoria,"posts":posts})
    #return render(req,"blog/blog.html")#,{"posts":posts})