# View django: onde são criadas classes responsáveis por controlar os templates e/ou conectar os templates ao banco de dados
# Aqui podem ser realizadas, por exemplo, requisições no banco de dados, envio de informações para os templates e ações com base em informações enviadas nos templates (de ação do usuário)


# Seção de importação de classes
from django.shortcuts import render
from django.views import generic
from .models import People


# Classe referente à view Home
class HomeView(generic.TemplateView): # A classe HomeView herda as configurações de generic, pertencente a Template View, uma view já configurada de forma básica
    template_name = 'home.html' # Define o nome do template a ser renderizado na view

    def get_context_data(self, **kwargs): # Método responsável por obter e retornar uma contexto, isto é, um conjunto de informações a serem enviados para o template
        context = super().get_context_data(**kwargs) # Obtem o contexto da classe ao qual HomeView herda
        context["pessoas"] = People.objects.all() # Insere no contexto uma lista de todas as pessoas contidas no banco (e suas respectivas informações). Essa lista é referenciada pela chave "Pessoas"
        return context # Retorna o contexto