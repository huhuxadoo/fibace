#!/usr/bin/env python3
import os
import urllib.request
import json

def create_issue(title, body, labels):
    """Создает Issue в GitHub через API"""
    repo = os.environ.get('GITHUB_REPOSITORY')
    token = os.environ.get('GH_TOKEN')
    
    if not repo or not token:
        print("ℹ️  No GitHub repo or token - running locally")
        return
    
    url = f"https://api.github.com/repos/{repo}/issues"
    
    payload = json.dumps({
        "title": f"[SECURITY BOT] {title}",
        "body": body,
        "labels": labels
    }).encode('utf-8')
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                print(f"✅ Created issue: {title}")
            else:
                print(f"⚠️  Response: {response.status}")
    except Exception as e:
        print(f"❌ Failed: {e}")

# Тестовый запуск
print("🤖 Security bot script starting...")

create_issue(
    title="Bot is ready for work",
    body="""## 🤖 Security Bot Activated

Этот Issue создан автоматически для тестирования интеграции.

**Что работает:**
- ✅ GitHub Actions workflow
- ✅ Автоматический запуск при push
- ✅ Создание Issues через API (urllib)

**Следующий шаг:**
Запустить локально: `claude -> /pentest:pentest`

---
*Created by security-bot workflow*""",
    labels=['security', 'bot-test']
)

print("✅ Script completed!")
