# Model django: onde o banco de dados é descrito


# Seção de importação de classes
from django.db import models


# Classe que descreve o model de pessoa
class People(models.Model):
    name = models.CharField('Nome completo', max_length=100, null=False) # Atributo nome de pessoa. É do tipo charField (para textos pequenos), tem 'Nome completo' como nome a ser exibido no admin, tem tamanho máximo de 100 caracteres e não pode ser nulo
    cpf = models.IntegerField('CPF', primary_key=True) # Atributo cpf de pessoa. É do tipo integerField (para números), tem 'CPF' como nome a ser exibido no admin, está definido como chave primária do objeto (permite a identificação do objeto, pelo fato de ser única e bão nula. Caso se queira acessar um objeto em específico, é por meio da chave primária que isso é feito
    email = models.EmailField('E-mail',null=True, blank=True) # Atributo email de pessoa. É do tipo emailField (para e-mail - a string informada só é aceita se for de um e-mail válido), tem 'E-mail' como nome a ser exibido no admin, o campo pode ser deixado vazio

    class Meta: # Classe responsável pela organização da tabela exposta no admin
        ordering = ['name'] # Por padrão, ordena os itens pelo nome
        verbose_name = 'Pessoa' # Nomeia cada linha da tabela como "Pessoa" no admin
        verbose_name_plural = 'Pessoas' # Nomeia a tabela como "Pessoas"

    def __str__(self):
        return self.name # Caso seja acessado diretamente o objeto (e não os atributos dele, como se deve ser feito), retorna o atributo nome

