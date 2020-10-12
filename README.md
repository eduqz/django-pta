# [PTA] Treinamento de Django

Projeto desenvolvido durante o treinamento de Django do Processo de Trainee por Área (PTA) do CITi de 2019.2.

## Como rodar o projeto
Após clonar o repositório, em seu diretório raiz siga o passo a passo a seguir.

### Crie um ambiente virtual:
Para Windows:
```bash
virtualenv venv
```
Para Linux:
```bash
virtualenv venv -p python3
```

### Ative o ambiente virtual:
Para Windows:
```bash
venv\Scripts\activate
```
Para Linux:
```bash
source venv/bin/activate
```

### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Crie e aplique as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Crie um superusuário:
```bash
python manage.py createsuperuser
```

### Execute o projeto:
```bash
python manage.py runserver
```
