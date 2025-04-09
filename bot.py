import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'YOUR_TOKEN_HERE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопки для быстрого доступа
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(KeyboardButton("/githelp"), KeyboardButton("/dockerfile node"))
menu_kb.add(KeyboardButton("/gitignore python"), KeyboardButton("/readme"))
menu_kb.add(KeyboardButton("/license mit"), KeyboardButton("/security headers"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я DevHelperBot — бот для помощи IT-разработчикам.\n\n"
        "Доступные команды:\n"
        "🧾 Git: /githelp, /gitignore python, /git reset\n"
        "🐳 Docker: /dockerfile node, /docker help, /docker compose example\n"
        "📦 Пакеты: /npm express, /pip flask\n"
        "⚙️ Генераторы: /readme, /license mit\n"
        "⚡ Bash: /bash find, /linux disk\n"
        "🔐 Безопасность: /security headers, /env .env\n",
        reply_markup=menu_kb
    )

# Git
@dp.message_handler(commands=['githelp'])
async def git_help(message: types.Message):
    await message.answer(
        "📘 Топ Git команд:\n"
        "git init — инициализация\n"
        "git add . — добавить все файлы\n"
        "git commit -m 'msg' — коммит\n"
        "git push — отправка на сервер\n"
        "git pull — получить изменения\n"
        "git status — статус файлов\n"
        "git log — история коммитов"
    )

@dp.message_handler(commands=['gitignore'])
async def gitignore(message: types.Message):
    args = message.get_args()
    templates = {
        'python': '__pycache__/\n*.py[cod]\n*.env\n.env\nvenv/\n*.log',
        'node': 'node_modules/\n.env\ndist/\n*.log',
        'php': 'vendor/\n.env\n*.log\n*.cache'
    }
    if args:
        content = templates.get(args.lower())
        if content:
            await message.answer(f"```\n{content}\n```", parse_mode='Markdown')
        else:
            await message.answer("Такой технологии нет. Попробуй python, node или php")
    else:
        buttons = InlineKeyboardMarkup()
        for tech in templates:
            buttons.add(InlineKeyboardButton(text=tech, callback_data=f"gitignore_{tech}"))
        await message.answer("Выберите технологию:", reply_markup=buttons)

@dp.callback_query_handler(lambda c: c.data.startswith("gitignore_"))
async def process_gitignore_callback(callback_query: types.CallbackQuery):
    tech = callback_query.data.split('_')[1]
    content = {
        'python': '__pycache__/\n*.py[cod]\n*.env\n.env\nvenv/\n*.log',
        'node': 'node_modules/\n.env\ndist/\n*.log',
        'php': 'vendor/\n.env\n*.log\n*.cache'
    }.get(tech)
    await callback_query.message.answer(f"```\n{content}\n```", parse_mode='Markdown')

@dp.message_handler(commands=['git'])
async def git_reset(message: types.Message):
    await message.answer("`git reset` используется для отмены изменений в индексации или истории коммитов.\nПримеры:\n- git reset --soft HEAD~1 — удалить последний коммит, но оставить изменения\n- git reset --hard — полностью отменить изменения", parse_mode='Markdown')

# Docker
@dp.message_handler(commands=['dockerfile'])
async def dockerfile_node(message: types.Message):
    args = message.get_args()
    if args == 'node':
        dockerfile_text = (
            "```Dockerfile\n"
            "FROM node:18\n"
            "WORKDIR /app\n"
            "COPY . .\n"
            "RUN npm install\n"
            "CMD [\"npm\", \"start\"]\n"
            "```"
        )
        await message.answer(dockerfile_text, parse_mode='Markdown')

@dp.message_handler(commands=['docker'])
async def docker_help(message: types.Message):
    await message.answer("🛠 Основные команды Docker:\n- docker build -t name .\n- docker run -p 80:80 name\n- docker ps -a\n- docker stop <id>\n- docker rm <id>\n- docker rmi <image>")

@dp.message_handler(commands=['docker', 'compose'])
async def docker_compose_example(message: types.Message):
    await message.answer("```yaml\nversion: '3'\nservices:\n  web:\n    image: nginx\n    ports:\n      - '80:80'\n```", parse_mode='Markdown')

# Пакеты
@dp.message_handler(commands=['npm'])
async def npm_package(message: types.Message):
    pkg = message.get_args()
    if pkg:
        await message.answer(f"📦 Установка npm пакета `{pkg}`:\n```bash\nnpm install {pkg}\n```", parse_mode='Markdown')

@dp.message_handler(commands=['pip'])
async def pip_package(message: types.Message):
    pkg = message.get_args()
    if pkg:
        await message.answer(f"🐍 Установка pip пакета `{pkg}`:\n```bash\npip install {pkg}\n```", parse_mode='Markdown')

# Генераторы
@dp.message_handler(commands=['readme'])
async def readme_template(message: types.Message):
    await message.answer("```markdown\n# Название проекта\n\n## Описание\nОписание вашего проекта.\n\n## Установка\n```bash\ngit clone <repo>\ncd project\npip install -r requirements.txt\n```\n\n## Запуск\n```bash\npython main.py\n```\n\n## Лицензия\nMIT\n```", parse_mode='Markdown')

@dp.message_handler(commands=['license'])
async def license_gen(message: types.Message):
    if message.get_args() == 'mit':
        await message.answer("MIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy... (и т.д.)")

# Bash & Linux
@dp.message_handler(commands=['bash'])
async def bash_find(message: types.Message):
    if message.get_args() == 'find':
        await message.answer("Примеры `find`:\n- Найти все .py: `find . -name '*.py'`\n- Найти файлы >10Мб: `find . -size +10M`", parse_mode='Markdown')

@dp.message_handler(commands=['linux'])
async def linux_disk(message: types.Message):
    if message.get_args() == 'disk':
        await message.answer("Проверка места на диске: `df -h`\nПроверка использования: `du -sh *`", parse_mode='Markdown')

# Security
@dp.message_handler(commands=['security'])
async def security_headers(message: types.Message):
    if message.get_args() == 'headers':
        await message.answer("📌 Безопасные HTTP-заголовки:\n- Content-Security-Policy\n- X-Frame-Options\n- X-Content-Type-Options\n- Strict-Transport-Security")

@dp.message_handler(commands=['env'])
async def env_example(message: types.Message):
    if message.get_args() == '.env':
        await message.answer("```env\nSECRET_KEY=your-secret\nDB_NAME=mydb\nDB_PASS=strongpassword\n```", parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
