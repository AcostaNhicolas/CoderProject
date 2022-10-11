from django.shortcuts import render
from .forms import BlogForm, UserRegisterForm, UserEditForm, AvatarForm
from .models import Avatar, Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# def inicio(request):
#     return render(request, 'inicio.html', {})

def inicio(request):
    blogs = Blog.objects.all()
    return render(request, 'inicio.html',{'blogs':blogs,'avatar':getAvatar(request)})

######################################################################################
#-------------------------------------  CRUD  --------------------------------------------
def blogCompleto(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,'blogCompleto.html',{'blog':blog,'avatar':getAvatar(request)})

@login_required
def nuevoBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            subtitulo = info['subtitulo']
            autor = info['autor']
            cuerpo = info['cuerpo']
            imagen = info['imagen']
            blog = Blog(titulo=titulo,subtitulo=subtitulo,autor=autor,cuerpo=cuerpo,imagen=imagen)
            blog.save()
            blogs = Blog.objects.all()
            return render(request, 'inicio.html',{'blogs':blogs,'avatar':getAvatar(request)})
        return render(request,'nuevoBlog.html',{'form':form,'avatar':getAvatar(request),'mensaje':'Error al cagar el artículo'})
    else:
        form = BlogForm()
        return render(request, 'nuevoBlog.html',{'form':form,'avatar':getAvatar(request)})

@login_required
def editarBlog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            blog.titulo = info['titulo']
            blog.subtitulo = info['subtitulo']
            blog.autor = info['autor']
            blog.cuerpo = info['cuerpo']
            blog.imagen = info['imagen']
            blog.save()
            blogs = Blog.objects.all()
            return render(request, 'appBlog/inicio.html',{'blogs':blogs,'avatar':getAvatar(request)})
        else:
            return render(request,'editarBlog.html',{'form':form,'avatar':getAvatar(request),'mensaje':'Error al cagar el artículo'})
    else:
        form = BlogForm(initial={'titulo':blog.titulo,'subtitulo':blog.subtitulo,'autor':blog.autor,'cuerpo':blog.cuerpo,'imagen':blog.imagen})
        return render(request, 'editarBlog.html',{'form':form,'avatar':getAvatar(request)})

@login_required
def eliminarBlog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    blogs = Blog.objects.all()
    return render(request, 'inicio.html',{'blogs':blogs,'avatar':getAvatar(request)})

#######################################################################################

#----------------------------- LOGIN -------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            user = authenticate(username=usu, password=clave)
            if user is not None:
                login(request, user)
                blogs = Blog.objects.all()
                return render(request,'inicio.html',{'mensaje':f'Bienvenido {usu}','blogs':blogs,'avatar':getAvatar(request)})
        else:
            return render(request,'login.html',{'mensaje':'Error, datos incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            blogs = Blog.objects.all()
            return render(request, 'inicio.html',{'blogs':blogs,'mensaje':f'Usuario {username} Creado Correctamente','avatar':getAvatar(request)})
        else:
            return render(request, 'register.html',{'mensaje':'Formulario Invalido'})
    else:
        form = UserRegisterForm()
        return render(request,'register.html',{'form':form})

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            blogs = Blog.objects.all()
            return render(request,'inicio.html',{'blogs':blogs,'mensaje':'Perfil Editado Correctamente','avatar':getAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request,'editarPerfil.html',{'form':form,'usuario':usuario,'avatar':getAvatar(request)})

def addAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            last_avatar = Avatar.objects.filter(user=request.user)
            if (len(last_avatar)>0):
                last_avatar[0].delete()
            avatar = Avatar(user=request.user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            blogs = Blog.objects.all()
            return render(request,'inicio.html',{'usuario':request.user, 'mensaje':'Avatar Agregado Correctamente','imagen':avatar.imagen.url})
        else:
            return render(request, 'addAvatar.html',{'form':form,'mensaje':'Formulario Invalido', 'blogs':blogs, 'avatar':getAvatar(request)})
    else:
        form=AvatarForm()
        return render(request,'addAvatar.html',{'form':form,'usuario':request.user,'avatar':getAvatar(request)})

def getAvatar(request):
    lista = Avatar.objects.filter(user=request.user.id)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=''
    return imagen