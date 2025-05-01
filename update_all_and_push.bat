@echo off
chcp 65001 > nul

echo ============================================
echo 🚀 Запуск скрипта обновления таблицы...
python generate_colab_table.py

if %errorlevel% neq 0 (
    echo ❌ Ошибка при запуске скрипта. Проверь generate_colab_table.py
    pause
    exit /b
)

echo ============================================
echo 📚 Добавление файлов в Git...
git add .

echo ============================================
echo 📝 Создание коммита...
git commit -m "Автообновление: README.md и другие изменения"

echo ============================================
echo ☁️ Отправка изменений на GitHub...
git push origin master

echo ============================================
echo ✅ Всё готово! Все изменения загружены на GitHub.
pause
