# NSFW Prompts for Graphic Novel - IMPROVED VERSION

## Высококачественные промпты для эксплицитных сцен

### Вариант 1: Упрощенный и эффективный промпт
**Positive Prompt:**
```
(masterpiece:1.4), (best quality:1.4), (ultra highres:1.2), 
photorealistic, beautiful woman, perfect body, smooth skin,
doggy style, anal sex, intimate scene, bedroom, 
detailed anatomy, professional lighting, cinematic, 
8k, hyperrealistic, perfect proportions
```

**Negative Prompt:**
```
(worst quality:2), (low quality:2), (normal quality:2), lowres, 
bad anatomy, bad hands, text, error, missing fingers, 
extra digit, fewer digits, cropped, jpeg artifacts, signature, 
watermark, username, blurry, artist name, deformed, disfigured, 
ugly, gross proportions, malformed limbs, missing arms, 
missing legs, extra arms, extra legs, mutated hands, 
fused fingers, too many fingers, long neck
```

### Вариант 2: Более детальный промпт
**Positive Prompt:**
```
RAW photo, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, 
high quality, film grain, beautiful 20yo woman, perfect face,
natural breasts, fit body, long hair, passionate expression,
sexual position, intimate bedroom scene, warm lighting,
photorealistic, hyperrealistic, detailed background
```

### Вариант 3: Художественный стиль
**Positive Prompt:**
```
oil painting, renaissance style, beautiful nude woman,
classical art, perfect anatomy, soft lighting, warm colors,
intimate scene, artistic, museum quality, detailed, 
professional art, masterpiece, high resolution
```

## Оптимальные технические настройки:

### Для реалистичных изображений:
- **Sampling Method:** Euler a (ПРОСТОЙ И ЭФФЕКТИВНЫЙ!)
- **Steps:** 20-25 (не больше!)
- **CFG Scale:** 6-8 (ВАЖНО: не выше 8!)
- **Width/Height:** 512x768 или 768x512
- **Denoising:** 0.6

### Альтернативные методы сэмплинга:
1. **DPM++ SDE Karras** - хорошее качество
2. **DDIM** - быстрый и стабильный
3. **LMS** - для художественного стиля

### Важные настройки для качества:
- ✅ **Restore faces** - ОБЯЗАТЕЛЬНО
- ✅ **Tiling** - выключить
- ✅ **Highres fix** - включить
- **Upscaler:** Latent (для скорости) или R-ESRGAN 4x+
- **Hires steps:** 10-15

## Проблемы и решения:

### Если изображения странные/уродские:
1. **ПОНИЗЬТЕ CFG Scale до 6-7**
2. **Уменьшите количество steps до 20**
3. **Используйте Euler a вместо сложных сэмплеров**
4. **Уберите слишком много деталей из промпта**

### Если анатомия неправильная:
**Добавьте в negative prompt:**
```
bad anatomy, extra limbs, missing limbs, floating limbs,
disconnected limbs, malformed hands, missing fingers,
extra fingers, long neck, long torso, extra heads
```

### Простой рабочий промпт для начала:
```
Positive: beautiful woman, photorealistic, high quality, detailed
Negative: ugly, deformed, blurry, low quality

Settings:
- Sampler: Euler a
- Steps: 20
- CFG: 7
- Size: 512x768
```

## Советы по улучшению:

1. **Начните с простого промпта** - добавляйте детали постепенно
2. **CFG Scale 6-8** - выше дает артефакты
3. **Steps 20-25** - больше не значит лучше
4. **Euler a** - самый надежный сэмплер
5. **Включите Restore faces** для лучших лиц

Попробуйте эти настройки - должно получиться намного лучше!