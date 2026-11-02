# Top Rhododendrons — макет v3, концепция «Kwekerij» (каталог питомника)

Третий раунд: одна концепция, пять страниц, собранных как самодостаточные HTML-файлы для просмотра в артефактах claude.ai на телефоне.

**Открыть:** `dist/index.html` (главная), `dist/assortiment.html`, `dist/product.html#nova-zembla`, `dist/plantgids.html`, `dist/groothandel.html`. Все страницы лежат плоско в `dist/`, медиа — в `dist/assets/` (ссылки вида `assets/…`, без `../`). Каждая страница работает и в одиночку рядом с папкой `assets/`.

**Видео-превью для владельца:** `previews/<страница>-telefon.mp4` (390×844 @2x) и `previews/<страница>-kompyuter.mp4` (1440×900), по две на каждую из пяти страниц.

## Концепция: что изменилось по сравнению с C «Veld» и почему это дороже и надёжнее

C была самой практичной (карточки с ценой, цветом, временем цветения, раздельные розница/B2B), но читалась как SaaS-шаблон: один гротеск, скругления 28 px, пилюли, капсульная навигация, бенто. Владелец: «ближе всех, но далеко от идеала». v3 берёт из C логику (витрина с ценами, спокойная двухколоночная подача, раздельные каналы) и меняет регистр на **каталог производителя**:

- **Голос.** Серифный **Newsreader** (оптический размер, заголовки и цены) + гротеск **Hanken Grotesk** (факты, таблицы, формы). Заголовки обычным регистром, с точкой: «Rhododendrons die aanslaan.», «Alle rhododendrons.», «Adviezen uit eigen kwekerij.» — интонация производителя, а не маркетинга.
- **Цвет.** Бумага `#f4f1ea` / `#ebe7dd`, чернила `#1b1f1b`, мох `#2f4a3a` (кнопки, offerte-блок), ночь `#182a20` (футер, шапка B2B), один винный акцент `#9e3448` только для надзаголовков и номеров. Фотографии цветов — единственные яркие пятна.
- **Каталожная точность вместо «лендинга».** Нумерация сортов 01–07, волосяные линии вместо карточек-плиток, табличные цифры, цены по четырём размерам прямо в списке ассортимента, миниатюра соцветия поверх фото куста, характеристики как `dl`-таблица, сравнительная таблица с сортировкой, календарь цветения с реальными цветами соцветий. Все скругления 3–4 px.
- **Доверие через конкретику.** В hero — четыре факта старого trust-bar (Sinds 2001 · Eigen transport · 10.000+ planten · Persoonlijk advies), цитата и портрет Герта Топа как редакционный блок, четыре обещания нумерованным списком, честные пометки «Demo» у форм и корзины, настоящие телефоны/KvK/часы, никаких выдуманных отзывов, кейсов и цифр.
- **Логотип.** Новый знак: пятилепестковый венчик рододендрона тонкой линией (`public/logo.svg`, тот же знак в шапке, футере и фавиконе), wordmark «Top Rhododendrons» засечным, подпись «Kwekerij · Otterlo · sinds 2001».
- **Hero-видео.** Десктопная нарезка переделана: вместо «безголового торса» (аудит X4) — полоса 3:2 с лицом, кустами и садом (y 40–520 исходника), апскейл Lanczos до 1440×960, CRF 26, 1,8 МБ. Мобильная нарезка из раунда 2 (низ с водяным знаком отрезан) сохранена. Водяной знак «Veo» не попадает ни в один кадр ни в одном варианте. Шапка — матовая бумажная полоса с первого пикселя (контраст логотипа и меню над любым кадром ≥ 4,5:1).
- **Путь покупки.** Карточка → страница сорта (галерея с лайтбоксом, 9 характеристик, выбор размера с реальным прайсом, количество, апселл tuinturf, «In winkelwagen») → выезжающая корзина (строки, количество, итог, честная пометка про онлайн-оплату, «Bel / E-mail», ссылка на партийную цену). Корзина живёт в `localStorage` и переживает переходы между страницами.
- **B2B — отдельный канал.** Своя шапка (тёмная, меню Afnemers/Werkwijze/Voorraad/Tarieven/Vragen, «Offerte aanvragen», ссылка «Particulier»), hero на фото поля, offerte-форма (поля старого сайта), карточка контактного лица, диалог «Ontvang de prijslijst», плавающий WhatsApp. Розничные страницы на B2B не ссылаются нигде, кроме одного спокойного блока «Voor professionals».

## Страницы

| Страница | Файл | Содержание |
|---|---|---|
| Главная (розница) | `dist/index.html` | видео-hero с фактами → витрина 7 сортов + tuinturf → **календарь цветения по месяцам** → «Bekijk de plantgids» → кwekerij (фото поля, история, 4 обещания) → цитата Герта Топа → две двери (tuin / professionals) → FAQ → контакт + форма |
| Ассортимент | `dist/assortiment.html` | рабочие фильтры (цвет, standplaats, высота, назначение; И между группами, ИЛИ внутри) + сортировка (популярность, имя, цена ↑↓, ранняя bloei, высота) → каталожные строки с 4 ценами → tuinturf → B2B-полоса |
| Сорт | `dist/product.html#<slug>` | шаблон для любого сорта по хэшу (`#nova-zembla`, `#cunninghams-white`, …, `#tuinturf-substraat`): крошки, галерея + лайтбокс, выбор размера, количество, апселл, корзина, характеристики, мини-календарь цветения, B2B-блок, другие сорта |
| Plantgids | `dist/plantgids.html` | сравнительная таблица с сортировкой → полный календарь bloei/plant → «Planten en verzorgen» (3 совета + tuinturf) → «Zeven lessen» → FAQ → CTA |
| Groothandel (B2B) | `dist/groothandel.html` | hero на поле + 4 факта → Afnemers (3 группы) → Werkwijze (4 сервиса) → Voorraad (таблица размеров) → Проces (4 шага) → Tarieven (3 ступени) → FAQ B2B → offerte-форма + контактное лицо + prijslijst-диалог + WhatsApp |

Навигация между страницами — обычные относительные ссылки (`assortiment.html`, `product.html#slug`, `index.html#contact`), работают с диска и с любого хостинга. В просмотрщике артефактов переходы между файлами не работают по его ограничению — поэтому каждая страница публикуется отдельно и живёт сама по себе.

## Инвентаризация контента старого сайта → где это живёт в v3

Источник: `/rhododendrons/app/**/page.tsx`, `components/*.tsx`, `lib/*.ts`.

| Старый блок | Файл-источник | Где в v3 |
|---|---|---|
| Header (Assortiment, Groothandel, Contact, WhatsApp, Offerte, корзина) | `components/header.tsx` | `site-header.tsx`: розничная шапка (Assortiment · Plantgids · De kwekerij · Contact · Groothandel, телефон, корзина со счётчиком), B2B-шапка; мобильное меню-диалог с Bel/WhatsApp |
| Hero с видео «Rhododendrons uit eigen kwekerij · Gekweekt in Otterlo sinds 2001» | `components/hero-section.tsx` | Главная, `video-hero.tsx`: видео на весь экран, «Rhododendrons die aanslaan.», подзаголовок с фактами из источника |
| Trust bar (Sinds 2001 / Eigen transport / 10.000+ planten / Persoonlijk advies) | `components/trust-bar.tsx` | Главная: полоса фактов внутри hero (десктоп) и полосой под hero (телефон) |
| Populaire rhododendrons (6 карточек + «Bekijk alle») | `components/products-section.tsx` | Главная, секция «Assortiment»: 7 карточек в том же порядке + tuinturf, кнопка «Alle maten en prijzen» → assortiment |
| Over ons: «Wij kweken rhododendrons. Niet meer, niet minder.», 4 обещания, портрет и цитата Герта | `components/about-section.tsx` | Главная: секция «De kwekerij» (фото поля, тексты p1–p2, 4 нумерованных обещания) + секция-цитата с портретом |
| **Bloei- & plantkalender по месяцам + «Bekijk plantgids»** | `components/bloom-section.tsx`, `bloom-timeline.tsx` | Главная, секция «Bloeikalender» (`bloom-calendar.tsx`): 12 месяцев, полосы в цвете соцветия, штриховка «ideaal plantmoment», отметка текущего месяца, легенда, кнопка «Bekijk de plantgids». Тот же компонент — в plantgids и мини-версия на странице сорта |
| FAQ (6 вопросов) | `components/faq-section.tsx` | Главная «Vraag & advies» и plantgids «Veelgestelde vragen» (`faq.tsx`) |
| Contact en Offerte aanvragen (форма particulier/hovenier, e-mail, WhatsApp) | `components/contact-form.tsx` | Главная, секция «Contact»: форма (naam, telefoon, e-mail, bericht), блок адрес/телефоны/часы, ссылка на groothandel для профессионалов |
| Offerte-модал «Particulier / Hovenier · Groothandel» | `components/offerte-modal.tsx` | Заменён двумя дверями на главной («Voor uw tuin» / «Voor professionals») и прямыми ссылками: розница → форма контакта, B2B → groothandel#offerte |
| Footer (описание, Instagram, KvK, ссылки, часы, адрес, телефоны, privacy/voorwaarden) | `components/footer.tsx` | `site-footer.tsx` на всех страницах; privacy/voorwaarden ведут на страницы старого сайта |
| WhatsApp sticky | `components/whatsapp-sticky.tsx` | `whatsapp-float.tsx` только на groothandel (розница — WhatsApp в контактах, меню и корзине) |
| Testimonials (3 отзыва) | `components/testimonials-section.tsx` | **Не перенесены**: на старой главной не подключены, имена и тексты выглядят выдуманными. Если есть настоящие отзывы Google — место есть под цитатой Герта |
| Assortiment: заголовок, 7 сортов (фото, цвет, bloei, высота, описание, 4 цены), tuinturf | `app/assortiment/page.tsx`, `catalog-grid.tsx`, `lib/products.ts` | `assortiment.html` + рабочие фильтры (`bloeikleurFilter`, `standplaatsFilter`, `maxHoogte`, `geschiktVoor` из `products.ts`) и сортировка |
| Страница сорта: крошки, галерея (2 фото), описание, выбор размера, количество, апселл tuinturf, trust-badges, kenmerken (9), B2B-блок, «Terug» | `app/assortiment/[slug]/page.tsx`, `product-actions.tsx`, `product-gallery.tsx` | `product.html#<slug>` — всё перенесено, плюс мини-календарь и «Andere soorten» |
| Tuinturf-substraat: описание, цена, 6 kenmerken, 3 пункта | `app/assortiment/tuinturf-substraat/page.tsx` | `product.html#tuinturf-substraat`; апселл на странице сорта; баннер на главной и в ассортименте |
| Корзина (drawer, количество, subtotaal, «Afrekenen» недоступен, ссылка на offerte) | `components/cart-drawer.tsx`, `lib/cart-context.tsx` | `cart-drawer.tsx`: то же + Bel/E-mail, хранение в localStorage |
| **Plantgids: сравнительная таблица (kleur, bloei, hoogte, breedte, groei, standplaats, winterhard) с сортировкой** | `app/plantgids/page.tsx`, `plantgids-comparison-table.tsx` | `plantgids.html` «Vergelijken» (`compare-table.tsx`): те же 8 колонок, сортировка по клику, липкая первая колонка, строки ведут на сорт |
| **Plantgids: 7 советов («Plant niet te diep», «Vermijd de mulch-vulkaan», …)** | `app/plantgids/page.tsx` (`tips`) | `plantgids.html` «Zeven lessen die wij elke klant meegeven» — все 7 дословно |
| Plantgids: «Gegevens zijn indicatief» | там же | под таблицей |
| Groothandel hero (заголовок, подзаголовок, 3 CTA, 3 метрики) | `app/groothandel/page.tsx` | `groothandel.html` hero: тот же заголовок, CTA (offerte, prijslijst, bel), факты строкой без «цифр-гигантов» |
| Wie wij beleveren (3 группы × 3 строки) | там же | секция «Afnemers» |
| Hoe wij voor u werken (3 преимущества) + plantpaspoort из FAQ | там же | секция «Werkwijze» (4 пункта) |
| Beschikbare aantallen (таблица 5 размеров + примечание) | там же | секция «Voorraad» |
| Hoe werkt een projectorder (4 шага) | там же | секция «Het proces» |
| Uitgelichte projecten (3 кейса) | там же | **Не перенесены**: обезличенные кейсы без подтверждения — вопрос владельцу |
| Zakelijke tarieven (3 ступени, –12/–22/–30 %) | там же | секция «Tarieven» с пометкой «Indicatief; definitieve prijs in de offerte» |
| FAQ B2B (6) | там же | секция «Vragen» |
| Projectofferte-форма (bedrijfsnaam, kvk, contactpersoon, telefoon, e-mail, projecttype, aantal, leverdatum, omschrijving) | `app/groothandel/groothandel-form.tsx` | секция «Offerte» (`forms.tsx` → `OfferteForm`), те же поля + soort/maat, валидация по-голландски |
| Prijslijst-модал (naam, e-mail, bedrijf) | `components/prijslijst-modal.tsx`, `prijslijst-button.tsx` | `PrijslijstModal` на groothandel (hero, tarieven, offerte-блок) |
| Privacy / Voorwaarden | `app/privacy`, `app/voorwaarden` | ссылки на существующие страницы старого сайта (в макет не входят) |
| SEO: title/description/OG, JSON-LD | `lib/site-config.ts`, `layout.tsx` | title/description/OG у каждой страницы, `assets/og.jpg`; JSON-LD — на этапе продакшена |

## Компоненты 21st.dev (найдены через MCP `search`, код получен `get_component`, адаптированы вручную; AI-генерация не использовалась)

| Файл v3 | Источник 21st.dev (id) | Что взято / изменено |
|---|---|---|
| `components/gallery.tsx` | Thumbnail image viewer (ibrandify, 37501) | лента миниатюр с клавиатурной навигацией; добавлен лайтбокс с Escape/стрелками и ловушкой фокуса |
| `pages/Assortiment.tsx` (фильтры) | Chip Group (35042) | чипы-переключатели `aria-pressed`, группы по фасетам; без анимации «+N» |
| `components/cart-drawer.tsx` | Drawer (31360) | side-sheet на десктопе / bottom-sheet на телефоне, без Base UI |
| `components/quantity.tsx` | Quantity Stepper (29940) | press-and-hold, `spinbutton`; без rolling digits |
| `components/bloom-calendar.tsx` | Gantt Chart (38523) | идея полос по лейнам на сетке месяцев, `role="img"` + текстовая подпись строки; CSS-grid вместо SVG, стековая версия для телефона |
| `components/compare-table.tsx` | Sortable Table (22166) | сортировка по заголовкам, `aria-sort`; без TanStack |
| `pages/Groothandel.tsx` (tarieven) | Pricing Tiers List (28540) | список ступеней строками (label, диапазон, описание, скидка) |
| `pages/Product.tsx` (крошки) | Breadcrumb (23681) | разметка `nav aria-label`, `aria-current` |
| `pages/Home.tsx` (цитата Герта) | Editorial Testimonial (9637) | крупная серифная цитата + подпись + портрет |
| `components/forms.tsx` | Contact Form (kevingirelli, 35258; из раунда 2) | двухколоночный контакт-блок, формы с голландской валидацией |
| `components/site-header.tsx`, `video-hero.tsx`, `faq.tsx`, `reveal.tsx` | Header 1 (8964), PrismaHero (12200), Accordion ± (24907), Reveal (19240) — из раунда 2 | упрощены под концепцию: матовая полоса без капсулы, в hero контент в потоке, без blur-анимаций |

Ключ 21st.dev нигде не записан.

## Проверки

- `npm run build` → `dist/` (5 страниц ≈ 390 КБ каждая, инлайн-скрипт и стили; `assets/` ≈ 9 МБ; весь `dist/` ≈ 9,7 МБ).
- `npm run check` (`tools/check.cjs`): локальный сервер отдаёт `dist/` с заголовком `Content-Security-Policy: default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com data:; img-src 'self' data: blob:; media-src 'self' blob:`; Playwright/Chromium открывает каждую страницу на 360×640, 375×667, 390×844, 768×1024, 1024×768, 1366×768, 1440×900. Результат: 35 видов, 0 ошибок консоли, 0 неудачных запросов, React-root отрисован, видео играет, 0 битых картинок, `scrollWidth === innerWidth` везде.
- `node tools/states.cjs`: скриншоты состояний (мобильное меню, корзина, фильтры, сортировка, лайтбокс, prijslijst-диалог, tuinturf) — в `.shots/states/` (не коммитится).
- Контраст (расчёт): винный акцент на бумаге 6,1:1, muted 5,1–5,6:1, белый/70 на мхе 5,8:1, рамки полей ≥ 3:1; фокус — двойной контур; `prefers-reduced-motion` → постер вместо видео, без анимаций; мобильное меню, корзина, лайтбокс и диалог — `role="dialog"`, Escape, ловушка фокуса, `inert` на `main`.
- `npm run previews` (`tools/previews.cjs`): видео-превью из покадровых @2x скриншотов (24 fps), hero-видео проигрывается покадрово ~3 с, затем плавная прокрутка с паузами на секциях; H.264, каждое < 15 МБ.

## Структура

```
mockup-v3/
  index.html, assortiment.html, product.html, plantgids.html, groothandel.html  — входы Vite
  build-single.mjs      — сборка каждой страницы в один HTML (JS как классический инлайн-скрипт, CSS инлайн), медиа в dist/assets, проверка ссылок
  src/data/content.ts   — единственный источник фактов и текстов (из старого сайта)
  src/components/       — логотип, шапка, футер, hero, календарь, карточка сорта, галерея, корзина, формы, таблица сравнения, …
  src/pages/            — Home, Assortiment, Product, Plantgids, Groothandel
  src/assets/           — hero-видео (десктоп/мобайл, без водяного знака) + постеры, фото WebP (≤1800 и ≤900 px)
  public/logo.svg, public/assets/og.jpg
  tools/                — server.cjs (CSP), check.cjs, states.cjs, previews.cjs
  dist/                 — собранные страницы (коммитятся)
  previews/             — 10 видео-превью
```

Команды: `npm install` (или скопировать `node_modules` из mockup-v2), `npm run build`, `npm run check`, `npm run previews`, `npm run dev`.

## Открытые вопросы владельцу

1. **Формулировка гарантии.** В старом сайте два варианта: «wij vervangen kosteloos» (groothandel-FAQ, about) и «wij zoeken samen naar een passende oplossing» (розничный FAQ). В макете везде первая. Утвердить одну.
2. **Плантмомент в календаре.** Старый календарь закрашивал Feb–Mrt и Sep–Okt, а FAQ говорит «maart–april en september–oktober». В макете — по FAQ (Mrt–Apr, Sep–Okt). Подтвердить.
3. **WhatsApp-номер.** В старом сайте два: `31620297849` (шапка, контакт) и `31318592483` (плавающая кнопка). Использован первый.
4. **Скидки по ступеням (–12 / –22 / –30 %)** взяты со старой groothandel-страницы с пометкой «indicatief». Показывать ли их публично?
5. **Кейсы проектов** («Wooncomplex in de Randstad», …) и отзывы не перенесены как неподтверждённые. Есть ли реальные проекты/отзывы, которые можно назвать?
6. **Видео.** Нарезка переделана (лицо и кусты вместо торса), но это по-прежнему ИИ-ролик. Для продакшена советуем снять настоящее поле в мае (горизонтально и вертикально) и фото Герта на поле.
7. **Логотип.** Знак-венчик в SVG — предложение; wordmark набран шрифтом, для фирменного стиля его нужно перевести в кривые.
8. **Следующая фаза:** отправка форм (e-mail), онлайн-оплата, самохостинг шрифтов, JSON-LD, страницы privacy/voorwaarden в новом дизайне.
