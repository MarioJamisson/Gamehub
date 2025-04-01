# 🎮 GameHub

Um projeto Django com interface simples, que lista jogos de uma pasta local e busca automaticamente as capas no banco de dados da IGDB.

---

## ✨ Features

- Interface futurista com TailwindCSS
- Busca capas automaticamente via IGDB
- Exibe os jogos em grid estilo Netflix
- Suporte a fallback com imagem padrão caso a capa não seja encontrada
- Sistema de upload manual planejado (futuro)

---

## 🧰 Tecnologias usadas

- Python 3.13+
- Django 5.1.7
- TailwindCSS 3+
- IGDB API (via Twitch dev credentials)
- PIL (Pillow) pra manipular imagens

---

## 🚀 Como rodar o projeto

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
venv\Scripts\activate

# Instala dependências
pip install -r requirements.txt

# Instala dependências JS
npm install

# Gera o CSS com Tailwind
npx tailwindcss -i ./gamehub_app/static/css/tailwind.css -o ./gamehub_app/static/css/style.css --watch

# Roda o servidor Django
python manage.py runserver
```

---

## 🧠 Observações

- Capas são salvas em `static/covers` com nome normalizado
- Tailwind lê os templates de `gamehub_app/templates/`
- O botão "Listar Jogos" abre a view que pede o caminho da pasta local

---

## 📦 .gitignore sugerido

```
*.pyc
__pycache__/
venv/
db.sqlite3
.vscode/
*.css.map
.env
.DS_Store
Thumbs.db
```

---

## 📷 Preview

Interface estilo Steam/Netflix com grid e degradê preto/vermelho 😎

---

## 💀 Feito por Mario Jamisson

> "A maquina de Madas" 🤖

---

## 📜 Licença

Esse projeto é livre, mas cuidado com os jogos que tu roda... 👀

