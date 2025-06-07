.PHONY: lint lint-format lint-check lint-type lint-style

# Каталог с исходниками (можно подстроить)
SRC_DIR := app

# Линтеры и команды
lint: lint-format lint-check lint-type lint-style

lint-check:
	@echo "🧹 Запуск всех линтеров..."

lint-format:
	@echo "🎨 black (проверка форматирования)..."
	@black --check $(SRC_DIR) || echo "[black] ❌ Ошибка!"

lint-type:
	@echo "🔍 mypy (проверка типов)..." || echo "[mypy] ❌ Ошибка!"
	@mypy $(SRC_DIR) || echo "[flake8] ❌ Ошибка!"

lint-style:
	@echo "🧪 pylint и flake8 (стиль и ошибки)..."
	@pylint $(SRC_DIR) || echo "[pylint] ❌ Ошибка!"
	@flake8 $(SRC_DIR)

format:
	@echo "✨ Форматирование black'ом..."
	@black $(SRC_DIR)