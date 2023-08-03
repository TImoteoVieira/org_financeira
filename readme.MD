# Org_Financeira - Aplicativo de Organização Financeira

Este é um aplicativo Django desenvolvido para ajudar na organização financeira pessoal.

## Instalação

Siga os passos abaixo para iniciar o projeto em sua máquina:

1. Clone o repositório:

git clone https://github.com/TImoteoVieira/org_financeira.git
cd org_financeira


2. Crie e ative um ambiente virtual (opcional, mas recomendado):
python3 -m venv venv

- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS/Linux:
  ```
  source venv/bin/activate
  ```

3. Instale as dependências:
pip install -r requirements.txt


4. Configure o banco de dados (opcional):
Se você deseja utilizar um banco de dados diferente do SQLite, atualize as configurações no arquivo `org_financeira/settings.py` conforme necessário.

5. Execute as migrações:
python manage.py migrate


6. Crie um superusuário:
python manage.py createsuperuser


7. Inicie o servidor de desenvolvimento:
python manage.py runserver


O aplicativo estará disponível em `http://localhost:8000/`. Você pode acessar a área de administração em `http://localhost:8000/admin/` usando as credenciais do superusuário que você criou.

## Como Contribuir

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar pull requests ou relatar problemas na página de problemas do GitHub.

## Licença

Este projeto é licenciado sob a licença [MIT](LICENSE).