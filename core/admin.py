# Admin django: onde os models que devem ser acessados (para adição, remoção e/ou edição) pelo admin são indicados


# Seção de importação de classes
from django.contrib import admin
from .models import People


# Seção para registrar os models
admin.site.register(People) # Define que o model de admin pode ser acessado via admin