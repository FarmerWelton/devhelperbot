# DevHelperBot 🤖

Бот-помощник для IT-разработчиков, созданный на [aiogram 2.x](https://github.com/aiogram/aiogram).

## 🔧 Возможности:

🧾 **Git & GitHub**
- `/gitignore python` — генерирует `.gitignore` под язык
- `/git reset` — объясняет команду `git reset`
- `/githelp` — список самых нужных git-команд

🐳 **Docker**
- `/dockerfile node` — шаблон Dockerfile для Node.js
- `/docker help` — команды для работы с Docker
- `/docker compose example` — пример `docker-compose.yml`

📦 **Пакетные менеджеры**
- `/npm express` — команда установки и описание пакета
- `/pip flask` — то же самое для pip

⚙️ **Генераторы**
- `/readme` — шаблон README.md
- `/license mit` — текст MIT-лицензии

⚡ **Bash & Linux**
- `/bash find` — примеры `find`
- `/linux disk` — как проверить занятое место

🔐 **Безопасность**
- `/security headers` — важные HTTP-заголовки
- `/env .env` — пример безопасного `.env`

---

## 🚀 Установка и запуск

```bash
git clone https://github.com/FarmerWelton/devhelperbot.git
cd devhelperbot
pip install -r requirements.txt
```

Замените токен в файле `main.py`:
```python
API_TOKEN = 'YOUR_TOKEN_HERE'
```

Запуск:
```bash
python main.py
```

---

## 📂 requirements.txt
```txt
aiogram==2.25.1
```

---

## 🧑‍💻 Автор
[FarmerWelton](https://github.com/FarmerWelton)
