# Фото поля для «Hoe het werkt»: размеры и промпт (19.11.2026)

Сейчас в блоке временное фото чужого питомника: «Rhododendronfeld einer Baumschule in Edewecht», автор JoachimKohler-HB, Wikimedia Commons, CC BY-SA 4.0. Задача — получить своё изображение, которое сразу ляжет в блок.

## Как фото стоит на странице

- **Полоса во всю ширину экрана.** Высота 300–640 px, на телефоне 240–380 px. Получается 1920 × 626 на большом мониторе, 1440 × 522 на ноутбуке, 1024 × 430 на планшете, 390 × 265 на телефоне.
- **Кадрирование.** Фото обрезается по полосе с упором вниз: на компьютере видна нижняя часть кадра, верх уходит.
- **Растворение.** Верхние 20 % полосы растворяются в цвет страницы, нижние 30 % тоже: там стоят шаги.
- **Цвет.** Фото умножается на цвет страницы (#f1efea): светлое небо становится цветом страницы, белые пятна исчезают.

Схема для кадра 16:9 лежит в `docs/img/schema-kadra-16x9.png`. Что в ней видно, сверху вниз:

| Часть кадра | Что там |
|---|---|
| Верхние ~28 % высоты | на компьютере не видны вообще (только на телефоне) |
| 28–41 % | растворение: здесь должны быть кроны деревьев и светлое небо |
| 41–73 % | чёткая зона: здесь кусты |
| 73–92 % | растворение: только тёмная земля, без важных деталей |
| Нижние ~8 % | не видны |

На телефоне видна полная высота, а по ширине примерно 7–90 % кадра. Поэтому главные кусты держать в центральных 60 % ширины, и по краям не должно быть обрезанных кустов.

## Что сдать

- **Формат.** 16:9 (3840 × 2160 или максимальный размер, который даёт сервис). Если сервис умеет сверхширокий кадр, лучше 12:5 (3840 × 1600).
- **Разрешение.** Не меньше 2880 px по ширине.
- **Файл.** JPG или PNG. Обрезать, сжать и поставить на страницу я могу сам.

## Промпт A — как сейчас, только чище

Близко к нынешнему кадру. Кусты целые и в центре, земля внизу, светлое небо вверху.

```
Wide landscape photograph of a Dutch rhododendron nursery field in late May, Veluwe region.
Rounded, freshly flowering rhododendron shrubs with soft lilac-pink blossoms and dark glossy
green leaves, about 1 to 1.5 m tall, grown in open ground in loose rows with generous space
between them, standing on dark, crumbly peat soil with a few tufts of grass.
Eye-level camera about 1 m above the ground, 50 mm lens, gentle depth of field: the middle
row of shrubs sharp, the background softly out of focus.
Behind the field a calm line of mature oak and birch trees, the edge of a forest, under a pale,
soft, overcast white sky. Soft diffused daylight, no hard shadows.
Composition: tree line in the upper third, the main shrubs centred just below the middle of the
frame and kept inside the central 60 percent of the width, no shrub cut off at the left or right
edge, the bottom quarter of the frame only bare dark soil.
Natural, slightly muted colours: deep green leaves, lilac-pink flowers, warm brown-black soil,
grey-green trees, cream-white sky. Calm, honest, premium documentary photo of a family nursery.
No people, no buildings, no machinery, no pots, no fences, no text, no watermark.
```

## Промпт B — переработанный под наш дизайн

Изменения против A:
- **Ракурс.** Камера чуть выше, ряды уходят слева направо, как маршрут из четырёх шагов под фото.
- **Кусты.** Четыре куста в переднем ряду, примерно над четырьмя колонками шагов.
- **Небо и цвет.** Неба больше, оно бледное, без синевы, поэтому верх мягко растворяется. Палитра ближе к странице: шалфей, крем, тёплая земля.

```
Wide landscape photograph of a Dutch rhododendron nursery field in late May, Veluwe region.
Slightly elevated viewpoint (camera about 1.6 m high), rows of rounded rhododendron shrubs
running diagonally from the left foreground into the right background, so the eye travels from
left to right across the frame.
In the front row, four rounded flowering shrubs, evenly spaced across the central part of the
frame, each about 1.2 m tall, with soft lilac-pink blossoms and dark glossy green leaves,
standing on dark, crumbly peat soil; the rows behind them softer and smaller.
Background: a quiet edge of oak and birch forest, low on the horizon, under a large pale,
milky-white overcast sky with no blue. Early-morning soft light, very gentle shadows,
light haze in the distance.
Composition: horizon at about one third from the top, the four front shrubs in the middle band
of the frame, the lower quarter only dark soil, nothing important near the left and right edges.
Muted, natural palette that matches a calm website in sage green, cream and warm brown:
avoid saturated green grass and blue sky. 50 mm lens, f/5.6, documentary style, honest and
premium, no people, no buildings, no machinery, no pots, no fences, no text, no watermark.
```

## Настройки и «чего не надо»

- **Midjourney.** В конец промпта добавить `--ar 16:9 --style raw` (или `--ar 12:5 --style raw`).
- **ChatGPT, Gemini и другие без выбора пропорций.** Попросить «landscape, 16:9, highest resolution». Если дадут 3:2, тоже подойдёт: я обрежу.
- **Если сервис принимает негативный промпт:**
  `blue sky, neon green grass, harsh sunlight, hard shadows, HDR, oversharpened, fisheye, people, buildings, tractor, plastic pots, fence, text, watermark, frame, cut-off shrub at the edge`

## Важно

- **Фото-пример как образец.** Его можно загрузить в генератор для пробы в макете. Но результат, сделанный по чужому снимку, остаётся производным от него: лицензия CC BY-SA требует указывать автора и ту же лицензию. Для настоящего сайта лучше генерировать только по тексту, без загрузки.
- **Генерированное фото на настоящем сайте.** Блок говорит «Van ons veld naar uw tuin», то есть «с нашего поля». Сгенерированное поле там будет выдавать себя за наше. Для макета это нормально, для сайта лучше своё фото с поля по той же схеме (план, пункт 3.13). Схема и промпт подойдут и как задание фотографу.
