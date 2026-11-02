# Top Rhododendrons — макет v3, концепция «Veld» (раунд 3, после аудита)

Одна концепция, пять страниц, собранных как самодостаточные HTML-файлы для просмотра в артефактах claude.ai на телефоне. Это доработанная версия после независимого аудита (`AUDIT.md`): визуальный язык вернулся к направлению C «Veld» и усилен, все функциональные находки закрыты (раздел «Что исправлено» внизу).

**Открыть:** `dist/index.html` (главная), `dist/assortiment.html`, `dist/product.html#nova-zembla` (любой сорт по хэшу + переключатель сортов на самой странице), `dist/plantgids.html`, `dist/groothandel.html`. Все страницы лежат плоско в `dist/`, медиа — в `dist/assets/` (ссылки вида `assets/…`). Каждая страница работает и в одиночку рядом с папкой `assets/`.

**Видео-превью для владельца:** `previews/<страница>-telefon.mp4` (390×844 @2x) и `previews/<страница>-kompyuter.mp4` (1440×900), по две на каждую из пяти страниц.

## Концепция «Veld»: что это и чем отличается от раунда 1 и от C

Структура, контент и компоненты — из v3 (страница сорта с корзиной, plantgids с таблицей и календарём, отдельный B2B-поток). Визуальный язык — развитие C «Veld», без «каталожной кожи» раунда 1 (крем + засечный шрифт + волосяные линии + нумерация + надзаголовки над каждой секцией).

- **Один характерный гротеск — Bricolage Grotesque** (оптический размер 12–96): заголовки 500, текст 400, подписи 600. Никаких засечных.
- **Глубокий цветовой мир вместо кремовой бумаги.** Опорные — ночь `#0f1a14` (шапка, футер, витрина-календарь, процесс B2B), мох `#1c3326` (кweker, offerte, баннеры), светлые поверхности — шалфейный камень `#e7eae2` / `#d8ddd0` / `#f4f5f1`. Единственный яркий акцент — цвет соцветий из фотографий и один «flower» `#c43a72` для активного состояния. На главной около половины экранов тёмные: hero → витрина (светлая, чтобы фото цветов остались дневными) → календарь (ночь: полосы в цвете соцветий, белые читаются) → поле во всю ширину → кweker на мху → две «двери» → FAQ → контакт → футер.
- **Крупная фотография.** Видео на весь первый экран; поле на всю ширину (62svh); карточки сортов в 3 колонки на десктопе и 2 на телефоне; фото в таблице сравнения и календаре; галерея сорта 4:5.
- **Меньше типографских штампов.** Надзаголовок-чип не больше 1–2 раз на страницу, нет нумерации 01–07, нет волосяных линий: карточки со скруглением 14/20 px, кнопки 8 px, чипы-фильтры, чипы-переключатель сортов.
- **Шапка прозрачная над hero** (тёмный скрим сверху даёт ≥ 4,5:1 для белого логотипа и меню на любом кадре), после прокрутки и на остальных страницах — матовая ночная полоса. Телефон и корзина в шапке всегда, WhatsApp — с 1280 px.
- **Логотип** — тот же знак-венчик (SVG), wordmark теперь гротеском.
- **Hero-видео «отодвинуто»**: один резкий вертикальный ролик 720×1180 (исходник без нижней полосы с водяным знаком, 7,5 с, шов петли закрыт полусекундным наплывом) стоит колонкой с мягкими краями поверх размытого затемнённого кадра той же сцены в тоне мха (`hero-ambient-wide.jpg` для ландшафта, `hero-ambient-tall.jpg` для портрета). На ландшафтных экранах ≥ 768 px колонка во всю высоту справа, правый край — по краю контента, текст слева; на телефонах и планшете в портрете колонка по центру над текстовым блоком (её высота — свободное место над текстом, низ растворяется в фоне), так что лицо и руки у цветов видны на всех проверенных размерах (360×640 … 1440×900). Под `prefers-reduced-motion` — постер в той же колонке. Водяной знак не попадает ни в один кадр (проверено пошагово по 0,25 с). Скрим усилен, у мелких строк text-shadow — попиксельный контраст 5-го перцентиля ≥ 8,9:1 на проверенных кадрах.

Сравнение: раунд 1 — крем, Newsreader, надзаголовки, hairlines; C — камень, Manrope, карточки, пилюли, капсула; v3-final — ночь/мох/шалфей, Bricolage, большие фото, чипы, без капсулы и пилюль-кнопок.

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
| `components/gallery.tsx` | Thumbnail image viewer (ibrandify, 37501) | лента миниатюр с клавиатурной навигацией; лайтбокс через portal в `body`, Escape/стрелки, ловушка и возврат фокуса |
| `pages/Assortiment.tsx` (фильтры) | Chip Group (35042) | чипы-переключатели `aria-pressed`, группы по фасетам; без анимации «+N» |
| `components/cart-drawer.tsx` | Drawer (31360) | side-sheet на десктопе / bottom-sheet на телефоне, без Base UI |
| `components/quantity.tsx` | Quantity Stepper (29940) | press-and-hold, `spinbutton`; без rolling digits |
| `components/bloom-calendar.tsx` | Gantt Chart (38523) | идея полос по лейнам на сетке месяцев, `role="img"` + текстовая подпись строки; CSS-grid вместо SVG, стековая версия для телефона |
| `components/compare-table.tsx` | Sortable Table (22166) | сортировка по заголовкам, `aria-sort`; без TanStack |
| `pages/Groothandel.tsx` (tarieven) | Pricing Tiers List (28540) | список ступеней строками (label, диапазон, описание, скидка) |
| `pages/Product.tsx` (крошки) | Breadcrumb (23681) | разметка `nav aria-label`, `aria-current` |
| `pages/Home.tsx` (цитата Герта) | Editorial Testimonial (9637) | крупная серифная цитата + подпись + портрет |
| `components/forms.tsx` | Contact Form (kevingirelli, 35258; из раунда 2) | двухколоночный контакт-блок, формы с голландской валидацией |
| `components/site-header.tsx`, `video-hero.tsx`, `faq.tsx`, `reveal.tsx` | Header 1 (8964), PrismaHero (12200), Accordion ± (24907), Reveal (19240) — из раунда 2 | прозрачная шапка над hero + ночная полоса после прокрутки, контент hero в потоке, FAQ карточками, без blur-анимаций |

Ключ 21st.dev нигде не записан.

## Проверки

- `npm run build` → `dist/` (5 страниц ≈ 390–410 КБ каждая, инлайн-скрипт и стили; `assets/` ≈ 7,6 МБ; весь `dist/` ≈ 9,7 МБ).
- `npm run check` (`tools/check.cjs`): локальный сервер отдаёт `dist/` с заголовком `Content-Security-Policy: default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com data:; img-src 'self' data: blob:; media-src 'self' blob:`; Playwright/Chromium открывает каждую страницу на 360×640, 375×667, 390×844, 768×1024, 1024×768, 1366×768, 1440×900. Результат: 35 видов, 0 ошибок консоли, 0 неудачных запросов, React-root отрисован, видео играет, 0 битых картинок, `scrollWidth === innerWidth` везде.
- `node tools/verify.cjs`: 18 проверок взаимодействий (лайтбокс открывается/листается/закрывается касанием и возвращает фокус; переключатель сортов на странице сорта; неизвестный хэш → «Soort niet gevonden»; возврат фокуса после корзины и prijslijst-диалога; ошибки формы привязаны к полям и фокус на первом ошибочном; нет переполнения на 360 px; CTA hero B2B в первом экране на 360×640 и 375×667) + попиксельный контраст белого текста над видео (3 кадра × 2 вьюпорта) и над фото «дверей» — всё ≥ 4,5:1 (5-й перцентиль).
- `node tools/states.cjs`: скриншоты состояний — в `.shots/states/` (не коммитится).
- Контраст статичных пар: muted `#55615a` на камне ≥ 5,6:1, белый/65–75 на ночи/мху ≥ 5,5:1, рамки полей ≥ 3:1; фокус — двойной контур; `prefers-reduced-motion` → постер вместо видео, без анимаций; мобильное меню, корзина, лайтбокс и диалог — `role="dialog"`, Escape, ловушка фокуса, `inert` на `main`, возврат фокуса на открывший элемент.
- `npm run previews` (`tools/previews.cjs`): видео-превью из покадровых @2x скриншотов (24 fps), hero-видео проигрывается покадрово ~3 с, затем плавная прокрутка с паузами на секциях; H.264 (yuv420p, faststart). Итог (10 файлов, 30 МБ): телефон 780×1688 — index 5,0 МБ/37 с, assortiment 3,6/25, product 2,6/21, plantgids 2,9/31, groothandel 2,5/33; компьютер 1440×900 — index 4,2 МБ/31 с, assortiment 3,1/21, product 2,1/21, plantgids 1,6/21, groothandel 1,6/22.

## Структура

```
mockup-v3/
  index.html, assortiment.html, product.html, plantgids.html, groothandel.html  — входы Vite
  build-single.mjs      — сборка каждой страницы в один HTML (JS как классический инлайн-скрипт, CSS инлайн), медиа в dist/assets, проверка ссылок
  src/data/content.ts   — единственный источник фактов и текстов (из старого сайта)
  src/components/       — логотип, шапка, футер, hero, календарь, карточка сорта, галерея, корзина, формы, таблица сравнения, …
  src/pages/            — Home, Assortiment, Product, Plantgids, Groothandel
  src/assets/           — hero-видео (hero-figure.mp4, 720×1180, без водяного знака) + постер + два размытых фона (ambient), фото WebP (≤1800 и ≤900 px)
  public/logo.svg, public/assets/og.jpg
  tools/                — server.cjs (CSP), check.cjs, states.cjs, previews.cjs
  dist/                 — собранные страницы (коммитятся)
  previews/             — 10 видео-превью
```

Команды: `npm install` (или скопировать `node_modules` из mockup-v2), `npm run build`, `npm run check`, `node tools/verify.cjs`, `npm run previews`, `npm run dev`.

### Режим артефакта

В просмотрщике артефактов каждая страница живёт отдельно: ссылки внутри страницы — голые `#id` (работают), а клик по ссылке на другой файл (`assortiment.html`, `product.html#…`) показывает тихую плашку «In de mockup: open de pagina … apart» вместо молчаливого отказа (`installArtifactLinkGuard` в `src/lib/utils.ts`; включается только когда адрес страницы не оканчивается на `.html`). На странице сорта есть переключатель всех 7 сортов и tuinturf, так что всё видно и без переходов. Демо-корзина хранится в `sessionStorage` (на обычном хостинге переживает переходы между страницами; в артефактах у каждой страницы свой origin, и счётчик там не общий).

## Открытые вопросы владельцу

1. **Формулировка гарантии.** В старом сайте два варианта: «wij vervangen kosteloos» (groothandel-FAQ, about-обещание) и «wij zoeken samen naar een passende oplossing» (розничный FAQ). В макете каждая стоит там же, где в источнике. Утвердить одну для всего сайта.
2. **Плантмомент в календаре.** Старый календарь закрашивал Feb–Mrt и Sep–Okt, а FAQ говорит «maart–april en september–oktober». В макете — по FAQ (Mrt–Apr, Sep–Okt). Подтвердить.
3. **WhatsApp-номер.** В старом сайте два: `31620297849` (шапка, контакт) и `31318592483` (плавающая кнопка). Использован первый.
4. **Скидки по ступеням (–12 / –22 / –30 %)** взяты со старой groothandel-страницы с пометкой «indicatief». Показывать ли их публично?
5. **Кейсы проектов** («Wooncomplex in de Randstad», …) и отзывы не перенесены как неподтверждённые. Есть ли реальные проекты/отзывы, которые можно назвать?
6. **Видео.** Нарезка переделана (лицо и кусты вместо торса), но это по-прежнему ИИ-ролик. Для продакшена советуем снять настоящее поле в мае (горизонтально и вертикально) и фото Герта на поле.
7. **Логотип.** Знак-венчик в SVG — предложение; wordmark набран шрифтом, для фирменного стиля его нужно перевести в кривые.
8. **«Rhododendrons op stam»** (H1 groothandel, из старого сайта): в B2B-лексиконе «op stam» могут прочитать как штамбовую форму; возможно точнее «op het veld» / «in de volle grond».
9. **Следующая фаза:** отправка форм (e-mail), онлайн-оплата, самохостинг шрифтов, JSON-LD, страницы privacy/voorwaarden в новом дизайне.

## Правки текстов относительно старого сайта

Всё остальное — дословно. Изменено или добавлено:
- Заголовки и лиды новых секций (hero «Rhododendrons die aanslaan.», «Zeven soorten van ons veld.», «Alles wat u wilt weten.», «Drie dingen die het verschil maken.», заголовки «дверей», CTA plantgids) — новая копия в регистре источника.
- «Kwekerij in Otterlo · sinds 2001» (подпись логотипа и надзаголовок hero) — из tagline `siteConfig`.
- Советы «Planten en verzorgen» — пересказ трёх ответов FAQ (wanneer, grond, snoeien).
- B2B-факты строкой: «10.000+ planten op stam, vers gerooid uit Otterlo», «Vanaf 25 stuks», «100% aangroeigarantie bij correcte aanplant», «Factuur 30 dagen» — из метрик и текстов старой B2B-страницы; «NAK Tuinbouw» остался в сервисах и FAQ.
- Четвёртый пункт «Werkwijze» («Plantpaspoort en fyto») собран из B2B-FAQ.
- Пояснение в блоке Герта на B2B: «U spreekt rechtstreeks met de kweker» (из источника); «uw vaste contactpersoon» убрано.

## Что исправлено (по аудиту `AUDIT.md`)

**Критично (2 из 2)**
| № | Находка | Что сделано |
|---|---|---|
| К1 | Лайтбокс инертен, нельзя закрыть касанием | `gallery.tsx`: лайтбокс рендерится через `createPortal` в `body`, фокус на «Sluiten», после закрытия возвращается на «Foto vergroten». Проверено касанием на 390 (`tools/verify.cjs`). |
| К2 | Визуальный регресс к раунду 1 («AI-premium»: крем + serif + hairlines + 01–07 + надзаголовки) | Полная смена визуального слоя при сохранении структуры и компонентов: Bricolage Grotesque вместо Newsreader/Hanken; ночь/мох/шалфей вместо кремовой бумаги; заголовок витрины и прочие заголовки переписаны; надзаголовок-чип ≤ 2 на страницу; нет нумерации сортов и волосяных линий; карточки/чипы; крупные фото (поле во всю ширину, 3-колоночная витрина, фото в таблице и календаре); прозрачная шапка над hero. См. раздел «Концепция». |

**Важно (9 из 9)**
| № | Находка | Что сделано |
|---|---|---|
| В1 | Ссылки на себя с именем файла; на странице сорта только Nova Zembla; `wa.me` без `target` | Внутристраничные ссылки — голые `#kwekerij`, `#contact`, `#offerte`, на странице сорта все карточки «Andere soorten» и новый **переключатель сортов** (7 + tuinturf) ведут на `#slug`; все `https:`-ссылки (WhatsApp, Instagram, maps, privacy/voorwaarden) с `target="_blank" rel="noopener noreferrer"`; клик по межстраничной ссылке в режиме артефакта показывает плашку «open de pagina … apart». |
| В2 | Белый текст на белых цветах в «Voor professionals» (~2:1) | Градиент на всю карточку (`from-night` → `night/80` на 50 % → `night/5`), надзаголовок и лид 100 % белого; попиксельно: label 9,3–9,6:1, лид 14,4–14,8:1. |
| В3 | Контраст надзаголовка и лида hero ниже AA на части кадров | Верхний скрим 32 % (под прозрачную шапку), нижний усилен (`via-night/60–65`, 82–88 % высоты), надзаголовок 100 % белого + `text-shadow`; после «отодвинутого» hero текст лежит на размытом фоне, а не на ролике — попиксельно на кадрах 1,5/4/6,5 с: eyebrow 8,9:1, лид 14,4:1 (1440); 14,2 / 15,4 (390). |
| В4 | WhatsApp-кнопка перекрывает контент на groothandel | `IntersectionObserver`: кнопка скрыта, пока видны hero, секция `#offerte` или футер; на телефоне круглая 48×48 без подписи; `main` получил нижний отступ. |
| В5 | Цена и CTA на странице сорта ниже первого экрана, нет липкой панели | На телефоне фото 4:3, под H1 сразу `short`, цены, размеры и CTA; длинный текст перенесён в блок «Over …/Kenmerken»; липкая нижняя панель «€ … · In winkelwagen» появляется, когда основная кнопка ушла за экран, и прячется у футера. На десктопе CTA в первом экране. |
| В6 | B2B на мобильном: нет телефона в шапке/hero, hero выше экрана на 360/375 | Телефон-иконка в B2B-шапке на всех ширинах; в hero на телефоне «Vraag offerte aan» + «Bel 06…», prijslijst — ссылкой; лид укорочен на < 640 px. Проверено: CTA в первом экране на 360×640 (низ 506 px) и 375×667 (533 px). |
| В7 | Сравнение в plantgids на телефоне показывает только имя и цвет | < 768 px — карточки по сорту (фото, 8 значений в `dl`, сортировка `select`); ≥ 768 — таблица с миниатюрами, липкой колонкой и подсказкой над таблицей (768–1023). |
| В8 | Изменённые/неподтверждённые факты | Розничный FAQ о гарантии — исходная формулировка «wij zoeken samen naar een passende oplossing»; корзина — «Verzendkosten worden berekend bij afrekenen» (без «incl. btw»); «uw vaste contactpersoon» убрано; подпись под фото — «Het veld van de kwekerij, Otterlo» без адреса; «tot 120 cm» без «en meer»; обещания about-секции и trust-bar — дословно («Direct contact. Direct voordeel.», «Persoonlijk advies», «Dagvers gerooid»); «Statussoorten · grootformaat» и «bij correcte aanplant» возвращены. Список правок — выше. |
| В9 | Фокус не возвращается после диалогов; ошибки форм не привязаны к полям | `rememberFocus()` в корзине, prijslijst-диалоге и лайтбоксе; формы: `aria-invalid`, текст ошибки под полем с `aria-describedby`, фокус на первое ошибочное поле, общий `role="alert"`-итог. |

**Желательно (15 из 15; два — частично/обосновано)**
| № | Находка | Что сделано |
|---|---|---|
| Ж1 | Бумажная шапка поверх hero | Прозрачная над hero, ночная после прокрутки. |
| Ж2 | ИИ-модель в hero; лицо под H1 на 768/1024 | Колонка с роликом стоит справа от текста на всех ландшафтных ширинах (лицо и руки вне H1 и лида), в портрете — над текстом. Замена ролика реальной съёмкой — вопрос владельцу (без съёмки невозможно). |
| Ж3 | «Veluwe sinds 2001» на телефоне | Надзаголовок «Kwekerij in Otterlo · sinds 2001» на всех ширинах. |
| Ж4 | Карточка tuinturf в сетке 2×N на телефоне | Карточка на всю ширину (`col-span-2`), горизонтальная компоновка, короткий текст. |
| Ж5 | Дубли контактов и футера на телефоне | В блоке контакта на телефоне только адрес, телефоны, e-mail, WhatsApp; часы — в футере (на ≥ 768 и в блоке). |
| Ж6 | Длинный ассортимент и фильтры на телефоне | Кнопка «Filters (n)» раскрывает панель (на десктопе панель всегда видна); карточки с `short` и компактной строкой 4 цен; страница на 390 — 8,1 тыс. px вместо 10,5. |
| Ж7 | Зигзаг ассортимента на десктопе | Плотная сетка 2 колонки с фото 4:3, ценами и CTA на карточке. |
| Ж8 | Live-регион с «Wis filters» | Кнопка вынесена из `role="status"`. |
| Ж9 | Неизвестный хэш → Nova Zembla | Экран «Soort niet gevonden» с переключателем сортов и ссылкой на ассортимент. |
| Ж10 | Нет «Nog vragen over úw plant?» на странице сорта | Блок под CTA: «Nog vragen over úw plant? De kweker helpt u persoonlijk, ma–za 09:00–17:00» + WhatsApp + Bel (на сортах и tuinturf). |
| Ж11 | Свотч переносится, мёртвый класс `.swatch` | У `Swatch` есть класс; малые карточки (`compact`) показывают только цвет, остальное не переносится. |
| Ж12 | Счётчик срабатывает на `pointerdown` | Шаг по `click`; автоповтор только после удержания 450 мс; жест прокрутки ничего не меняет. |
| Ж13 | Plantgids без фотографий | Фото поля в шапке, миниатюры в таблице, карточках и календаре. |
| Ж14 | Переполнение таблицы на 360 px | `whitespace-nowrap` для колонки «Maat» + `overflow-x-auto`; проверено: `scrollWidth === innerWidth` на 360 на всех страницах. |
| Ж15 | Мелочи | WhatsApp в retail-шапке (≥ 1280); корзина в `sessionStorage` (не «вечная»); «op stam» — вопрос владельцу (оставлено как в источнике); вес и JSON-LD — продакшен. |
