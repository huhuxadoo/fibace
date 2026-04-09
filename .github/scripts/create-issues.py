#!/usr/bin/env python3
import os
import requests

def create_issue(title, body, labels):
    """Создает Issue в GitHub"""
    repo = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GH_TOKEN')
    
    if not repo or not token:
        print("No GitHub repo or token")
        return
    
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "title": f"[SECURITY BOT] {title}",
        "body": body,
        "labels": labels
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"✅ Created: {title}")
    else:
        print(f"❌ Failed: {response.text}")

# Тестовый запуск
print("🤖 Security bot script running!")

# Проверяем наличие реальных findings (в будущем)
# Сейчас создаем тестовый issue для демонстрации

if os.environ.get('GITHUB_REPOSITORY'):
    create_issue(
        title="Bot is ready for work",
        body="""## 🤖 Security Bot Activated

Этот Issue создан автоматически для тестирования интеграции.

**Что работает:**
- ✅ GitHub Actions workflow
- ✅ Автоматический запуск при push
- ✅ Создание Issues через API

**Следующий шаг:**
Добавить ANTHROPIC_API_KEY в Secrets и запустить настоящий pentest!

---
*Created by security-bot workflow*""",
        labels=['security', 'bot-test']
    )
else:
    print("Running locally - no GitHub token")
