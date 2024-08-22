# Projeto Django com API REST

Este é um projeto Django que inclui uma aplicação para gerenciamento de estudantes com uma API RESTful usando Django REST Framework (DRF) e documentação Swagger com drf-spectacular.

## Descrição

Este projeto permite gerenciar informações de estudantes, incluindo nome, idade, notas e informações do professor. Ele inclui uma API RESTful para operações CRUD e páginas HTML para visualização e manipulação dos dados.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:
- Python 3.12 ou superior
- Django 5.1 ou superior
- Django REST Framework
- drf-spectacular

## Instalação

1. Clone o repositório:   
     ```bash
    git clone https://github.com/usuario/repo.git
    cd repo
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o painel administrativo:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

- **Acessar a aplicação**: Abra o navegador e vá para `http://127.0.0.1:8000/` para visualizar e manipular os dados dos estudantes usando as páginas HTML.
- **Acessar a API**: Utilize as seguintes URLs para interagir com a API:
  - **Listar e criar estudantes**: `http://127.0.0.1:8000/api/students/`
  - **Detalhes, atualizar e deletar estudantes**: `http://127.0.0.1:8000/api/students/<id>/`

## Endpoints da API

- `GET /api/students/`: Lista todos os estudantes.
- `POST /api/students/`: Cria um novo estudante.
- `GET /api/students/<id>/`: Obtém os detalhes de um estudante.
- `PUT /api/students/<id>/`: Atualiza um estudante existente.
- `DELETE /api/students/<id>/`: Deleta um estudante.

## Documentação

- **Swagger UI**: `http://127.0.0.1:8000/api/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/api/redoc/`
