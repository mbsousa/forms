from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import UsuarioForm
from .models import Usuario
import random
import string

# Função para gerar senha aleatória
def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# View para cadastro de usuário
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Cria um novo usuário com os dados do formulário
            usuario = form.save(commit=False)
            
            # Gera uma senha aleatória
            senha_gerada = gerar_senha()
            usuario.senha = senha_gerada
            usuario.save()

            # Comentado - Código para envio de e-mail
            # Envia um e-mail de confirmação para o usuário com a senha gerada
            """
            assunto = 'Cadastro Confirmado'
            mensagem = f'Olá {usuario.nome},\n\nSeu cadastro foi realizado com sucesso.\nSua senha é: {senha_gerada}'
            de_email = 'seu_email@gmail.com'  # E-mail do remetente
            para_email = [usuario.email]  # E-mail do destinatário

            send_mail(assunto, mensagem, de_email, para_email)
            """
            
            # Redireciona para uma página de sucesso ou mostra a senha
            return render(request, 'resultado.html', {'usuario': usuario})
    else:
        form = UsuarioForm()
    
    return render(request, 'cadastro.html', {'form': form})
