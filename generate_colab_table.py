# generate_colab_table.py, учитывающий отсутствие README.md
import os
from urllib.parse import quote

# Настройки
GITHUB_USER = "jkrndkot"
GITHUB_REPO = "GitPyProba"
CHEATSHEETS_DIR = "cheatsheets"

# Получаем список всех .ipynb файлов
if not os.path.isdir(CHEATSHEETS_DIR):
    print(f"❌ Папка '{CHEATSHEETS_DIR}' не найдена.")
    exit(1)

notebooks = [f for f in os.listdir(CHEATSHEETS_DIR) if f.endswith(".ipynb")]
notebooks.sort()

def filename_to_title(filename):
    name = filename.replace(".ipynb", "")
    name = name.replace("_", " ")
    return name

# Генерируем таблицу
lines = []
lines.append("<!-- START CHEATSHEETS TABLE -->")
lines.append("| Тема | Открыть в Colab |")
lines.append("|------|------------------|")
for nb in notebooks:
    title = filename_to_title(nb)
    local_link = f"{CHEATSHEETS_DIR}/{quote(nb)}"
    colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{GITHUB_REPO}/blob/master/{CHEATSHEETS_DIR}/{quote(nb)}"
    colab_badge = f"[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    lines.append(f"| [{title}]({local_link}) | {colab_badge} |")
lines.append("<!-- END CHEATSHEETS TABLE -->")

table_md = "\n".join(lines)

README_PATH = "README.md"
if os.path.exists(README_PATH):
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()

    if "<!-- START CHEATSHEETS TABLE -->" in readme and "<!-- END CHEATSHEETS TABLE -->" in readme:
        before = readme.split("<!-- START CHEATSHEETS TABLE -->")[0]
        after = readme.split("<!-- END CHEATSHEETS TABLE -->")[1]
        new_readme = before + table_md + after
        print("🔄 Таблица обновлена в существующем README.md между маркерами.")
    else:
        new_readme = readme + "\n\n" + table_md
        print("➕ Маркеры не найдены, таблица добавлена в конец README.md.")
else:
    new_readme = "# Шпаргалки\n\n" + table_md
    print("📄 README.md не найден. Создан новый файл с таблицей.")

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(new_readme)
