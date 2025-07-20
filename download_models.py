#!/usr/bin/env python3
"""
Скрипт для загрузки рекомендованных NSFW моделей для Stable Diffusion WebUI
Для генерации реалистичных изображений персонажей графической новеллы
"""

import os
import urllib.request
import sys
from pathlib import Path

# Рекомендованные модели для реалистичной NSFW генерации
MODELS = {
    "Realistic Vision v5.1": {
        "url": "https://civitai.com/api/download/models/130072",
        "filename": "realisticVisionV51_v51VAE.safetensors",
        "description": "Фотореалистичная модель с поддержкой NSFW контента"
    },
    "DreamShaper v8": {
        "url": "https://civitai.com/api/download/models/128713", 
        "filename": "dreamshaper_8.safetensors",
        "description": "Универсальная модель с хорошим качеством лиц и тел"
    },
    "ChilloutMix": {
        "url": "https://civitai.com/api/download/models/11745",
        "filename": "chilloutmix_NiPrunedFp32Fix.safetensors", 
        "description": "Азиатский реализм, отлично подходит для аниме-реализма"
    }
}

def download_file(url, filepath, description):
    """Загружает файл с прогресс-баром"""
    print(f"\n📥 Загружаю: {description}")
    print(f"URL: {url}")
    print(f"Сохраняю в: {filepath}")
    
    def progress_hook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = min(100, (downloaded / total_size) * 100)
            size_mb = total_size / (1024 * 1024)
            downloaded_mb = downloaded / (1024 * 1024)
            print(f"\r🔄 {percent:.1f}% ({downloaded_mb:.1f}/{size_mb:.1f} MB)", end="")
        else:
            downloaded_mb = downloaded / (1024 * 1024)
            print(f"\r🔄 Загружено: {downloaded_mb:.1f} MB", end="")
    
    try:
        urllib.request.urlretrieve(url, filepath, progress_hook)
        print(f"\n✅ Модель загружена успешно!")
        return True
    except Exception as e:
        print(f"\n❌ Ошибка загрузки: {e}")
        return False

def main():
    # Проверяем, что мы в правильной директории
    webui_path = Path("stable-diffusion-webui")
    if not webui_path.exists():
        print("❌ Папка stable-diffusion-webui не найдена!")
        print("Запустите скрипт из директории, где установлен WebUI")
        sys.exit(1)
    
    models_dir = webui_path / "models" / "Stable-diffusion"
    models_dir.mkdir(parents=True, exist_ok=True)
    
    print("🎨 Установщик NSFW моделей для графической новеллы")
    print("=" * 60)
    
    # Показываем доступные модели
    print("\n📋 Доступные модели:")
    for i, (name, info) in enumerate(MODELS.items(), 1):
        print(f"{i}. {name}")
        print(f"   {info['description']}")
    
    print("\n⚠️  ВАЖНО: Эти модели содержат NSFW контент!")
    print("📁 Модели будут сохранены в:", models_dir.absolute())
    
    # Запрашиваем подтверждение
    choice = input("\n🤔 Загрузить все модели? (y/n): ").lower().strip()
    
    if choice not in ['y', 'yes', 'да', 'д']:
        print("❌ Загрузка отменена")
        return
    
    # Загружаем модели
    success_count = 0
    for name, info in MODELS.items():
        filepath = models_dir / info["filename"]
        
        # Проверяем, не загружена ли уже
        if filepath.exists():
            print(f"\n⏭️  {name} уже загружена, пропускаю...")
            success_count += 1
            continue
        
        if download_file(info["url"], filepath, f"{name} - {info['description']}"):
            success_count += 1
    
    print(f"\n🎉 Загрузка завершена! Успешно: {success_count}/{len(MODELS)}")
    
    if success_count > 0:
        print("\n🚀 Следующие шаги:")
        print("1. Перезапустите Stable Diffusion WebUI")
        print("2. В интерфейсе выберите загруженную модель")
        print("3. Начинайте генерировать персонажей для новеллы!")
        print("\n💡 Для сохранения лица персонажа используйте фиксированный seed")

if __name__ == "__main__":
    main() 