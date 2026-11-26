# Страница Groothandel: анализ текста первой версии (26.11.2026)

Что разобрано: весь текст `/groothandel` первой версии сайта (`rhododendrons/app/groothandel/page.tsx`, `groothandel-form.tsx`, `components/prijslijst-button.tsx` с `prijslijst-modal.tsx`, `components/offerte-modal.tsx`). Сверено с новой главной и страницей гарантии (`mockup-v3/block-mockups/waarom-kweker/index.html`, `garantie.html`), блоком «Voor professionals» (`pro.html`), `docs/plan-verbeteringen.md` (2.6, 3.x), `docs/audit-backlog.md`, `docs/prijzen.md`, последними записями `docs/mockup-decisions.md`.

Это отчёт, страница не собиралась. Весь предлагаемый текст сайта дан на нидерландском.

Сырые результаты инструментов: `/tmp/claude-0/-home-user/c2629853-388a-5a4a-89c1-ca1bace13c36/scratchpad/groothandel-tekst/` (`sections/` — отправленный текст, `lt/` — ответы LanguageTool, `yoast/` — скрипт, входные страницы и результаты).

---

## 1. Сводка: главное

1. **Почти вся страница стоит на неподтверждённых цифрах.** Скидки −12/−22/−30 %, партия от 25, ответ за 24 часа (повторён 5 раз), счёт на 30 дней, три проекта, объёмы по аудиториям, «10.000+», NAK. Если их убрать, от восьми блоков остаётся примерно три. Это главный довод за короткую страницу.
2. **Гарантия противоречит новому сайту трижды.** «100% aangroeigarantie bij correcte aanplant» (hero), «in het eerste seizoen» (FAQ) против «3 maanden aangroeigarantie na levering». Третье противоречие глубже: в условиях на `garantie.html` (статья 2) гарантия действует только для частных покупателей («die u als particulier bij ons koopt»). Старый FAQ обещает её и на партии в 1.000 штук. Пока владелец не решит, гарантии на странице Groothandel быть не должно.
3. **«Op stam» — неверный термин, и он стоит в H1, в meta description, в alt и ещё в трёх местах (6 раз).** У покупателя растений «rhododendron op stam» означает штамбовую форму (деревце на стволе), это отдельный товар. Страница имеет в виду «растёт в поле, ещё не выкопан». Заменить на «in de volle grond», «op ons veld», «op voorraad».
4. **«BTW verlegd» для нидерландских покупателей, скорее всего, фактическая ошибка** (4 упоминания). Перенос НДС в Нидерландах применяется в особых случаях (субподряд в строительстве, поставки в другие страны ЕС и т. п.), а доставка у нас только по Нидерландам. Это не вопрос стиля, а обещание в счёте: убрать до ответа бухгалтера.
5. **Документы названы неточно.** Официальный термин — «plantenpaspoort» (так пишут NVWA и Naktuinbouw), на странице «plantpaspoort». Организация называется «Naktuinbouw» (одним словом), и это инспекция, а не объединение: в ней не «состоят» («aangesloten bij»), у неё получают регистрацию. Фитосертификаты на экспорт выдаёт NVWA, и при доставке только по Нидерландам они не нужны.
6. **Страница длинная и телеграфная.** 9 блоков, 662 слова, 127 «предложений» в среднем по 5,3 слова; одно и то же сказано по 3–5 раз (услуга посадки ×6, 24 uur ×5, 30 dagen ×4, eigen transport ×3). Надзаголовки дублируют заголовки («PROJECTOFFERTE / Projectofferte aanvragen», «VEELGESTELDE VRAGEN / Veelgestelde vragen»). Это тот самый шаблонный вид, который владелец отвергает.
7. **Кнопка прайс-листа обещает не то, что делает.** «Download prijslijst (PDF)» ничего не скачивает, а открывает форму сбора контактов; до отправки написано «direct per e-mail», после — «binnen 24 uur». На новом сайте цены по размерам открыты, поэтому закрытый прайс-лист только мешает.

Отдельно: на странице ни разу не сказано «met kluit», хотя для профессионала это первый вопрос, и нет цены доставки (€ 75) и самовывоза в Wekerom.

---

## 2. Результаты инструментов

### 2.1 LanguageTool (реально запущен)

Публичный API `https://api.languagetool.org/v2/check`, `language=nl`, версия сервера 6.9-SNAPSHOT. 11 запросов по разделам, все ответы 200. Телефоны, e-mail, номер KvK и имена-заполнители перед отправкой убраны. Всего 38 срабатываний.

**Настоящие замечания (8 срабатываний, 6 проблем):**

| Что нашёл | Где | Вывод |
|---|---|---|
| `PDF` → `pdf` (×2) | кнопка прайс-листа | Верно: по норме названия форматов пишутся строчными; на `garantie.html` уже «pdf». |
| `BTW-nummer` → `btw-nummer` | FAQ | Верно: норма — «btw». Инструмент отметил одно место, на странице «BTW» 5 раз. Заодно: «KVK-nummer» в форме против «KvK» в подвале нового сайта; выбрать одно написание. |
| `grootformaat` → `groot formaat` | таблица размеров, FAQ | Жаргон. Проще «grote maten». |
| `fyto` | тарифы | Жаргонное сокращение; в чистом тексте ему не место. |
| `voorranglevering` и `Voorrangslevering` | тарифы, окно выбора | Слова нет в словаре, а главное — два разных написания одного слова на сайте. |
| `NAK Tuinbouw` | FAQ | Совет инструмента (дефис) неверен, но название и правда написано неправильно: «Naktuinbouw». |

**Ложные срабатывания (30):**
- `rhododendrons` ×6. Словарь хочет «rododendron» (так в официальном списке слов). Отрасль, название фирмы и весь новый сайт пишут через «rh». Оставить, не смешивать.
- Названия сортов ×13 (Catawbiense, Roseum Elegans, Ponticum, Cunningham's и т. д.).
- `Plantservice` ×4, `tuinturf-substraat` ×2: правильные составные слова, словарь их не знает.
- `U` с заглавной ×1 (это начало предложения после заголовка), `de aanplant` ×1.
- `Projectofferte Projectofferte` ×1 и `bijv.` ×2: следствие склейки подписей в один текст. Первое, впрочем, показывает реальную проблему: надзаголовок повторяет заголовок.

**Чего LanguageTool не увидел (моя вычитка):**
- пропущенный артикль: «Vraag offerte aan», «Wij maken offerte» (на новой главной — «Vraag een offerte aan»);
- «Akkoord op de offerte?» → «akkoord met»;
- «blokken uw leverdatum» — калька; «leggen vast» или «reserveren»;
- «Factuur op 30 dagen» — фламандский оборот; в Нидерландах «betaling binnen 30 dagen»;
- «Statussoorten» — такого слова нет;
- «25+ Jaar specialist» — заглавная в середине фразы; «1000» и «1.000» на одной странице;
- «← swipe voor meer →» — англицизм и подсказка, которая нужна только из-за таблицы;
- «wij» и «we» в одном предложении («kweken wij … dan kijken we»);
- «stuks» и «planten» вперемешку (7 и 10 раз);
- «Bedankt voor uw aanvraag!» — восклицательный знак против спокойного тона.

**Проверка моего варианта текста** (раздел 3 и 6, файл `sections/20-voorstel.txt`): 15 срабатываний, все ложные («rhododendrons» и названия сортов).

### 2.2 Yoast (реально запущен)

Пакет `yoastseo@3.7.0` в Node 22, нидерландский `Researcher`, штатные `ContentAssessor` и `SeoAssessor`. Скрипт: `yoast/run.js`. Библиотека заработала, свои подсчёты вместо неё не понадобились. Оговорки:
- в открытом пакете нет морфологии нидерландского (она в платной версии), поэтому ключевая фраза ищется по точным словоформам: «rhododendron» не равно «rhododendrons»;
- ширину заголовка Yoast в браузере меряет сам; в Node я измерил её шрифтом Liberation Sans 20 px (метрически совпадает с Arial) и передал в библиотеку;
- оценки «нет картинок», «нет ссылок» относятся к текстовой выжимке, а не к странице, их не учитывать;
- отдельной проверки «ключ в H1» в библиотеке нет (есть только «один H1»); H1 проверен вручную.

Ключевая фраза: **`groothandel rhododendrons`**. Для сравнения прогнал и `rhododendron groothandel`: без морфологии она не находится нигде (0 вхождений, SEO 56). Частотность запросов не проверялась: инструмента для этого нет.

**Читаемость**

| Показатель | Старая страница | Мой вариант |
|---|---|---|
| Слов | 662 | 367 |
| Предложений, средняя длина | 127; 5,3 слова | 53; 6,9 слова |
| Предложений длиннее 20 слов | 0 (макс. 18) | 2 (макс. 22); оценка «зелёная» |
| Самый длинный абзац | 27 слов | 42 слова; «зелёная» |
| Пассивный залог | 1 из 104 («BTW wordt verlegd…») | 0 из 53 |
| Слова-связки | 7 из 127 = 5,5 %, оценка 3 (мало) | 5 из 53 = 9,4 %, оценка 3 (мало) |
| Одинаковые начала подряд | нет | нет |
| Flesch (нидерландская формула) | **48,4** (уровень 5 из 5, трудно) | **72,9** (уровень 2, довольно легко) |
| Общая оценка читаемости | 90 | 90 |

Как это читать:
- Общие 90 у старой страницы обманчивы. Предложения короткие, потому что это обрывки («Plantservice optioneel.», «Gefaseerd mogelijk»), а Flesch 48 показывает, что слова длинные и канцелярские: «projectontwikkelaars», «gespecificeerde», «grondverbetering», «fytosanitaire», «betaaltermijn».
- Мало слов-связок — следствие того же телеграфного стиля. Для страницы из строк и шагов это нормально; гнаться за 30 % не нужно.

**SEO, ключ `groothandel rhododendrons`**

| Проверка | Старая страница | Мой вариант |
|---|---|---|
| Ключ в SEO-заголовке | да, в начале (9) | да, в начале (9) |
| Ширина заголовка | 68 знаков, 652 px: **шире предела 600 px** (3) | 59 знаков, 581 px (9) |
| Meta description: длина | 154 знака (9) | 145 знаков (9) |
| Meta description: ключ | **нет** (3) | да (9) |
| Ключ во вступлении | **нет** (3) | да (9) |
| Ключ в тексте | **0 раз** (4) | 2 раза, 0,54 % (9) |
| Ключ в H1 (вручную) | только «Rhododendrons», слова «groothandel» нет | оба слова |
| Ключ в подзаголовках | нет (3) | нет (3) — сознательно, см. ниже |
| Ключ в slug | частично: `groothandel` (6) | то же (6) |
| Один H1 | да | да |
| Общая оценка SEO | 61 | 83 |

Вывод: старый заголовок начинается с ключа, но дальше слово «groothandel» встречается в тексте один раз, в надзаголовке, и нигде рядом с «rhododendrons». Meta description занята неподтверждённым («10.000+», «vanaf 25 stuks») и неверным («op stam»). Ключ в подзаголовках не вставлял: «Groothandel» в каждом H2 — тот самый шаблонный вид.

---

## 3. По разделам

Обозначение в предлагаемых текстах: `[после подтверждения]` — вставлять только после ответа владельца (раздел 4).

### 3.1 Metadata и hero

**Работает:** «Direct van de kweker», «Vers gerooid op uw leverdatum» — конкретно и совпадает с главной («rooien uw planten pas vlak daarvoor»). Три способа связи.

**Не работает:**
- «op stam» в H1, в описании, в alt и в цифрах (см. сводку, п. 3);
- полоса из трёх больших цифр: «25+ jaar» (с 2001 года прошло ровно 25, плюс лишний), «10.000+» (на главной «10.000», и это число ещё ждёт подтверждения: бэклог 14, план 3.10), «100% aangroeigarantie» (в бэклоге в списке «Do not do»: безусловная «100% guarantee»);
- подзаголовок из двух обрывков, второй пустой («Levering afgestemd op uw project»);
- три равных по весу кнопки; надзаголовок капсом;
- «uit Otterlo», а поле и самовывоз в Wekerom.

**Предложение:**

> **Groothandel in rhododendrons. Rechtstreeks van de kweker.**
>
> Groothandel voor hoveniers, tuinarchitecten, gemeenten en projectontwikkelaars: u koopt uw rhododendrons per partij bij de kwekerij zelf, vers gerooid en met kluit.
>
> [Vraag een offerte aan] · Of bel 06 20 10 43 12
>
> Sinds 2001 · 7 soorten · 40 tot 225 cm · met kluit

Строка фактов — только подтверждённое, тихим текстом, без крупных цифр. Если нужен H1 без слова «groothandel» (как H2 блока на главной): «Rhododendrons voor hoveniers en projecten.»; тогда проверка «ключ в H1» не проходит.

### 3.2 Аудитории («Wie wij beleveren»)

**Работает:** сам перечень: hoveniers, tuinarchitecten, gemeenten, vastgoed.

**Не работает:**
- таблица 3×3 ради девяти обрывков; на телефоне её приходится листать вбок («swipe voor meer»);
- объёмы 30–150 / 100–500 / 150–1000 не подтверждены и ничего не дают читателю: он свой объём знает;
- строка «Voorwaarden» раздаёт общие условия по аудиториям случайно: счёт на 30 дней будто бы только садовникам, паспорт растений — только муниципалитетам;
- аудитории названы по-разному в четырёх местах: «projectontwikkelaars» (meta), «Vastgoed en wooncomplexen» (таблица), «Landschapsarchitect» (форма), «tuinarchitecten» (таблица).

**Предложение:** отдельный блок убрать. Аудитории уже названы одной строкой во вступлении hero (см. 3.1), теми же словами, что в блоке главной.

### 3.3 Преимущества («Hoe wij voor u werken»)

**Работает:** «U spreekt rechtstreeks met de kweker» — сильный и правдивый довод. «Eén gewas» перекликается с главной («Wij kweken alleen rhododendrons»).

**Не работает:**
- два из трёх преимуществ не подтверждены: посадка на месте (план 3.11), счёт на 30 дней и «BTW verlegd»;
- надзаголовок «ONZE VOORDELEN» и заголовок «Hoe wij voor u werken» говорят одно и то же, а через блок идёт «Hoe werkt een projectorder»;
- «daardoor weten wij wat u nodig heeft» — утверждение без опоры;
- нет главного для профессионала: ком, выкопка к дню, доставка, самовывоз.

**Предложение** (строки с волосяными линиями, как в блоке на главной):

> **Eén kwekerij, één aanspreekpunt.**
>
> **Partij** — U krijgt een prijs per partij, in een offerte op maat.
> **Rooien** — Wij rooien uw planten pas vlak voor de levering, met kluit.
> **Levering** — Wij bezorgen met eigen transport door heel Nederland, op de dag die wij samen afspreken. Afhalen in Wekerom kan ook.
> **Betalen** — Bedrijven betalen op factuur.
> **Contact** — U overlegt rechtstreeks met de kwekerij, van offerte tot levering.

`[после подтверждения]` для строки Partij: «Vanaf 25 planten krijgt u een partijprijs, in een offerte op maat.»

### 3.4 Размеры («Beschikbare aantallen»)

**Работает:** семь сортов перечислены, и это те же семь, что на главной.

**Не работает:**
- заголовок обещает количества, а в таблице их нет: только «Ruim op voorraad / Op voorraad / Op aanvraag»; проверить это нельзя, и оно устаревает;
- классы размеров не совпадают с новым сайтом: здесь 40–60, там 40–50 и 50–60 (`docs/prijzen.md`);
- «120 cm +» без верхней границы, хотя на главной «tot 225 cm»; при этом в `docs/prijzen.md` 100–120 — последний класс с ценой, крупнее по запросу, и это совпадает;
- столбец «Geschikt voor» — общие слова; «Statussoorten» — несуществующее слово;
- «Andere soorten op aanvraag» и FAQ «kweken wij regelmatig op aanvraag» не подтверждены (план 3.8);
- цен нет вообще, хотя на новом сайте они открыты.

**Предложение:** без таблицы, со ссылкой на каталог.

> **Zeven soorten, van 40 tot 225 cm.**
>
> Nova Zembla, Catawbiense Grandiflorum, Cunningham's White, Catawbiense Boursault, Roseum Elegans, Ponticum en Ponticum Roseum. Alle planten groeien in de volle grond en wij leveren ze met kluit. Welke maten er zijn, verschilt per soort. Maten boven 120 cm leveren wij op aanvraag.
>
> [Alle maten en prijzen]

### 3.5 Процесс («Hoe werkt een projectorder»)

**Работает:** четыре шага, как «in vier stappen» на главной; шаги 1 и 4 конкретны.

**Не работает:**
- «Binnen 24 uur» не подтверждено и спорит с часами работы (в воскресенье закрыто);
- «op stam» и «blokken» в шаге 3, «Plantservice optioneel» в шаге 4;
- «Wij maken offerte» без артикля; «gespecificeerde offerte» — канцелярит;
- нет цены доставки и самовывоза;
- надзаголовок «HET PROCES» лишний.

**Предложение** (названия шагов в форме главной: Kiezen, Bestellen, Afspreken, Ontvangen):

> **Van aanvraag tot levering, in vier stappen.**
>
> **Aanvragen** — U stuurt ons de soorten, maten en aantallen, en de week waarin u de planten nodig heeft.
> **Offerte** — U krijgt een offerte met de prijs per soort en maat. Ook de kosten van bezorgen staan erin.
> **Afspreken** — Na uw akkoord reserveren wij de planten. Daarna spreken wij samen de leverdag af.
> **Ontvangen** — Wij rooien vlak voor de levering en bezorgen met eigen transport. Afhalen kan in Wekerom.

`[после подтверждения]` к шагу Offerte: «U hoort binnen één werkdag van ons.» («один рабочий день» честнее, чем «24 часа», при закрытом воскресенье.)

### 3.6 Проекты («Uitgelichte projecten»)

**Работает:** ничего, на что можно опереться.

**Не работает:** три проекта не подтверждены. Они анонимны («Wooncomplex in de Randstad»), а фраза «Klantgegevens delen wij niet; uw project blijft vertrouwelijk» объясняет, почему их нельзя проверить. Для профессионального покупателя это выглядит как заполнитель и подрывает доверие к остальному.

**Предложение:** блок убрать. Вернуть, когда будет хотя бы один настоящий проект с разрешением заказчика: место, год, сорта и количество, фото. Тогда одна строка с фото, без рамки «Uitgelichte projecten».

### 3.7 Тарифы («Zakelijke tarieven»)

**Работает:** идея дать порядок цен до запроса.

**Не работает:**
- скидки −12/−22/−30 % не подтверждены, но набраны самым крупным шрифтом страницы;
- не сказано, от какой цены скидка. На новом сайте цены взяты временно (`docs/prijzen.md`), и правило там — одна цена на размер, без «вечной скидки»; проценты к временным ценам дают обещание, которое никто не считал;
- «Indicatief; definitieve prijs in de offerte» повторено дважды в одном блоке: цифра названа и сразу отозвана;
- описания ступеней повторяют то, что уже было («Vaste contactpersoon», «plantservice», «eigen transport»), а «Vaste contactpersoon» вдруг оказывается привилегией от 50 растений, хотя выше обещан всем;
- «scherpe partijprijzen» — оценка без доказательства; «Grootverbruik», «fyto» — жаргон;
- план 2.6 уже решил не выносить проценты на главную.

**Предложение:** блок убрать; цена остаётся одной строкой «Partij» (3.3). Если владелец подтвердит ступени, одна спокойная строка вместо трёх карточек:

> `[после подтверждения]` Vanaf 25 planten krijgt u een partijprijs. Hoe groter de partij, hoe lager de prijs per plant; u ziet het in de offerte.

### 3.8 FAQ

**Работает:** вопросы настоящие, такие и задаёт закупщик. Ответ про дату («Wij rooien op uw leverdatum, niet eerder») конкретен.

**Не работает:**

| Вопрос | Проблема |
|---|---|
| Aangroeigarantie bij grote partijen | «eerste seizoen» против «3 maanden»; условия гарантии сейчас только для частных лиц. |
| Aanplant op locatie | Услуга не подтверждена (план 3.11); «tarief per plant» обещает прайс, которого нет. |
| Leverdatum | «maximale aanslagkans» — превосходная степень без опоры; снова «op stam». |
| Facturatie | 30 дней и «BTW verlegd» не подтверждены; второе, вероятно, неверно. |
| Plantpaspoort | «plantpaspoort» → «plantenpaspoort»; «aangesloten bij de NAK Tuinbouw» неверно по названию и по сути; экспортные сертификаты при доставке только по Нидерландам не нужны. |
| Andere soorten | «kweken wij regelmatig op aanvraag» не подтверждено (план 3.8). |

Ещё: вопросы на «jullie», ответы на «u» — допустимо (вопрос голосом клиента), но в шестом вопросе вдруг «ik». Четыре ответа из шести повторяют блоки выше.

**Предложение:** четыре вопроса, только то, чего нет в строках и шагах.

> **Veelgestelde vragen**
>
> **Kan ik de planten vooraf bekijken?**
> Ja. U bent welkom op ons veld aan de Apeldoornseweg in Wekerom, ook zonder afspraak. Wij zijn open van maandag tot en met vrijdag van 8.00 tot 17.00 uur en op zaterdag van 9.00 tot 13.00 uur.
>
> **Wat kost bezorgen?**
> Bezorgen in Nederland kost € 75 per bestelling. Afhalen in Wekerom is gratis.
>
> **Kan ik ook een klein aantal bestellen?**
> Ja. U bestelt vanaf 1 plant, gewoon via de site. Een offerte is bedoeld voor grotere partijen.
>
> **Leveren jullie met plantenpaspoort?** `[после подтверждения]`
> Ja. Elke partij krijgt een plantenpaspoort.

Вопрос о гарантии — только после решения владельца, один из двух готовых ответов:

> **Geldt de aangroeigarantie ook voor zakelijke partijen?**
> Вариант А (гарантия та же): Ja. Ook voor zakelijke partijen geldt 3 maanden aangroeigarantie na levering. Slaat een plant niet aan, dan vervangen wij hem door dezelfde soort en maat.
> Вариант Б (гарантия только частным): De aangroeigarantie op deze site geldt voor particuliere kopers. Voor zakelijke partijen leggen wij de afspraken vast in de offerte.

При варианте А нужно править статью 2 условий на `garantie.html` и показать текст юристу (план 3.12).

### 3.9 Форма

**Работает:** обязательных полей четыре; ошибки на «u» и по делу; при сбое есть выход («of bel ons»); поля сгруппированы логично.

**Не работает:**
- «24 uur» трижды: над формой, под кнопкой и в подтверждении;
- надзаголовок, заголовок и кнопка — три раза «Projectofferte aanvragen»;
- «Projectomschrijving» обязательна, минимум 10 знаков, а сорта, размеры и количество (то, из чего делается предложение) спрятаны в подсказке к ней;
- KVK-nummer до первого разговора — лишний барьер; «Projecttype» дублирует описание;
- подсказка «bijv. maart 2026» уже в прошлом;
- подсказки внутри полей («Uw bedrijf», «Uw naam») повторяют подпись и исчезают при вводе;
- звёздочки без пояснения; в окне прайс-листа необязательное помечено «(optioneel)» — два способа на одном сайте;
- «Door dit formulier te verzenden gaat u akkoord met ons privacybeleid»: согласие с политикой для ответа на запрос не требуется, и формула «вы соглашаетесь» звучит как условие;
- подтверждение с восклицательным знаком и обещанием «projectofferte op maat» за 24 часа;
- нет выбора «доставка или самовывоз», хотя от него зависит цена (€ 75 или бесплатно).

**Предложение:** в разделе 6.

### 3.10 Кнопка прайс-листа и окно выбора типа клиента

**Кнопка «Download prijslijst (PDF)» и её окно**

Работает: «Geen spam», «Uw gegevens worden niet gedeeld met derden» — спокойно и по делу.

Не работает:
- подпись обещает скачивание, действие — форма сбора контактов;
- «direct per e-mail toegestuurd» до отправки и «binnen 24 uur» после: два разных обещания; судя по коду, письмо отправляется вручную или не отправляется вовсе (запрос уходит «в никуда», ошибка проглатывается);
- запятая вместо точки между двумя предложениями («Vul uw gegevens in, de prijslijst wordt…»);
- «Geen spam, geen verplichtingen» — рекламный штамп;
- существует ли оптовый прайс-лист, неизвестно.

Предложение: кнопку и окно убрать. Вместо них ссылка на открытые цены: **«Alle maten en prijzen»** (та же подпись, что на главной). Если у владельца есть настоящий оптовый прайс-лист в pdf: прямая ссылка **«Prijslijst (pdf)»** без формы.

**Окно «Offerte aanvragen» (`offerte-modal.tsx`)**

Не работает:
- «Kies uw situatie voor het beste aanbod» — магазинный тон;
- «Scherpe partijprijzen», «Voorrangslevering voor vaste afnemers», «Breed assortiment op bestelling» — три неподтверждённых обещания (и «breed assortiment» при семи сортах);
- «Directe levering aan huis» спорит с «день по договорённости»; «Aangroeigarantie inbegrepen» без срока;
- «Vraag handelsprijs op» и «Hovenier · Groothandel» — ещё два названия того же самого.

Предложение: в новом дизайне окно не нужно. В шапке уже есть пункт «Groothandel», на главной — блок «Voor hoveniers en projecten.» с кнопкой «Vraag een offerte aan». Одна формулировка действия на всём сайте: **«Vraag een offerte aan»**.

---

## 4. Что подтвердить у владельца

| № | Утверждение | Где стоит | Что спросить |
|---|---|---|---|
| 1 | Гарантия для бизнеса: «100% bij correcte aanplant», «eerste seizoen», «ook bij 1.000 stuks» | hero, FAQ, meta, окно выбора | Действует ли гарантия 3 месяца на оптовые партии? Если да — на тех же условиях (замена тем же сортом и размером, бесплатная доставка замены)? Если нет — что обещаем профессионалам? |
| 2 | Партия от 25 растений | meta, тарифы, блок на главной | Есть ли порог, с которого цена ниже? 25 или другой? |
| 3 | Скидки −12 / −22 / −30 % при 25–49 / 50–149 / 150+ | тарифы | Существуют ли такие ступени? От какой цены считается скидка? Можно ли называть проценты на сайте? |
| 4 | Предложение за 24 часа | процесс, форма (×3), окно прайс-листа | За какое время реально отвечаете? Подойдёт ли «binnen één werkdag»? |
| 5 | Счёт на 30 дней | аудитории, преимущества, FAQ | Продаёте ли компаниям с отсрочкой? Срок? Всем или постоянным клиентам? |
| 6 | «BTW verlegd» | аудитории, преимущества (×2), FAQ | Спросить бухгалтера: применяется ли перенос НДС хоть к одной вашей продаже в Нидерландах? Если нет — убрать навсегда. |
| 7 | Посадка на месте с улучшением почвы | преимущества, процесс, тарифы, FAQ (6 упоминаний) | Делаете ли посадку? Своя бригада? Как считается цена? (план 3.11) |
| 8 | NAK / plantenpaspoort / фитосертификаты | аудитории, тарифы, FAQ | Есть ли регистрация для выдачи plantenpaspoort (номер)? Даёте ли паспорт с каждой партией? Экспорт не упоминаем: верно? |
| 9 | Три проекта (280, 65, 150 растений) | проекты | Настоящие ли они? Есть ли проект, который заказчик разрешит назвать, с фото? |
| 10 | «10.000+ planten» | hero, meta, alt | Сколько растений на поле? Писать «10.000» или иначе? (бэклог 14, план 3.10) |
| 11 | Объёмы по аудиториям (30–150, 100–500, 150–1000) | аудитории | Предлагаю убрать. Возражений нет? |
| 12 | «Vaste contactpersoon», «rechtstreeks met de kweker» | преимущества, тарифы, форма | Кто отвечает на оптовые запросы: сам владелец или кто-то из команды? |
| 13 | «Voorranglevering» от 50 растений, «voor vaste afnemers» | тарифы, окно выбора | Есть ли приоритет в доставке? Предлагаю убрать. |
| 14 | «Andere soorten op aanvraag», «kweken regelmatig op aanvraag» | размеры, FAQ | Выращиваете ли под заказ? Какие сорта, кроме семи? (план 3.8) |
| 15 | Наличие по размерам («Ruim op voorraad…»), «120 cm +» | размеры | Какие размеры есть в оптовых количествах? Верхняя граница 225 см верна для опта? |
| 16 | «Gefaseerd mogelijk» (поставка частями) | аудитории | Возите ли партию в несколько приёмов? Как тогда считается доставка? |
| 17 | Доставка € 75 за заказ | (на старой странице нет) | Одна цена для любой партии, и для 300 растений тоже? Или для опта считается отдельно? |
| 18 | Оптовый прайс-лист в pdf | кнопка в hero | Он существует? Если нет — убираем кнопку. |

---

## 5. Структура новой страницы

Сейчас 9 блоков и 662 слова. Предлагаю 6 блоков и около 370 слов (с FAQ и вступлением к форме).

| Старый блок | Решение | Куда |
|---|---|---|
| Hero, три цифры | Оставить, упростить | H1, одна строка, одна кнопка и телефон текстом, тихая строка фактов. Без крупных цифр. |
| Wie wij beleveren | Слить | Одна строка во вступлении hero. Таблицы нет. |
| Hoe wij voor u werken | Слить с тарифами | Блок «Eén kwekerij, één aanspreekpunt.»: пять строк (Partij, Rooien, Levering, Betalen, Contact). |
| Beschikbare aantallen | Сократить | «Zeven soorten, van 40 tot 225 cm.»: абзац и ссылка «Alle maten en prijzen». Без таблицы. |
| Hoe werkt een projectorder | Оставить | Четыре шага по одной-две строки, слова в форме шагов главной. |
| Uitgelichte projecten | Убрать | Вернуть с настоящим проектом и фото. |
| Zakelijke tarieven | Убрать | Строка «Partij»; проценты только после подтверждения, одной фразой. |
| FAQ | Сократить | 4 вопроса (5 с гарантией после решения). |
| Aanvraagformulier | Оставить, упростить | Светлый фон вместо тёмной плашки; 4 обязательных поля. |
| Кнопка прайс-листа, окно выбора | Убрать | Ссылка «Alle maten en prijzen». |

Порядок: hero → что вы получаете (строки) → сорта и размеры → четыре шага → вопросы → форма.

Принципы:
- каждое утверждение один раз;
- без надзаголовков капсом: заголовок-предложение с точкой, как на главной;
- одно действие на всей странице («Vraag een offerte aan»), телефон рядом текстом;
- одни слова для одного и того же: «planten» (не «stuks»), «partij», «met kluit», «bezorgen / afhalen», «rooien», «wij»;
- цифры только те, что уже утверждены на главной: 2001, 7 сортов, 40–225 см, € 75, часы работы.

---

## 6. Микротекст формы

**Заголовок и вступление**

> **Vraag een offerte aan voor uw partij rhododendrons.**
> Vertel ons wat u nodig heeft. U krijgt een offerte met de prijs per soort en maat, rechtstreeks van de kwekerij.

**Поля** (необязательные помечены словом, звёздочек нет)

| Подпись | Подсказка под полем | Обяз. |
|---|---|---|
| Bedrijfsnaam | — | да |
| Uw naam | — | да |
| E-mailadres | — | да |
| Telefoonnummer (optioneel) | Handig als wij een vraag hebben over uw aanvraag. | нет |
| Soorten, maten en aantallen | Bijvoorbeeld: 40 × Nova Zembla, 60–80 cm. Weet u het nog niet precies? Een schatting is genoeg. | да |
| Gewenste levering (optioneel) | Bijvoorbeeld: week 12, of maart. | нет |
| Bezorgen of afhalen | Выбор: «Bezorgen in Nederland» / «Afhalen in Wekerom» | да |
| Plaats van levering (optioneel) | Показывать только при «Bezorgen». | нет |

Убрать: «KVK-nummer» (нужен для счёта, а не для предложения), «Projecttype» (если владельцу нужен для сортировки запросов — оставить необязательным), подсказки внутри полей.

**Ошибки**

| Поле | Текст |
|---|---|
| Bedrijfsnaam | Vul uw bedrijfsnaam in. |
| Uw naam | Vul uw naam in. |
| E-mailadres | Vul een geldig e-mailadres in, bijvoorbeeld naam@bedrijf.nl. |
| Soorten, maten en aantallen | Vul in welke soorten u zoekt en hoeveel planten. |
| Сбой отправки | Verzenden is niet gelukt. Probeer het opnieuw, of bel 06 20 10 43 12. |

**Кнопка:** Vraag een offerte aan · при отправке: Bezig met verzenden…

**Под кнопкой**

> Wij gebruiken uw gegevens alleen om uw aanvraag te beantwoorden. Lees onze [privacyverklaring].

Строку «Reactie binnen 24 uur» убрать. `[после подтверждения]`: «U hoort binnen één werkdag van ons.»

**Подтверждение**

> **Uw aanvraag is ontvangen.**
> U krijgt de offerte per e-mail. Hebben wij eerst een vraag, dan bellen of mailen wij u.
> Liever meteen overleggen? Bel 06 20 10 43 12.

Без восклицательного знака и без срока, пока он не подтверждён.

---

## 7. SEO

| Элемент | Предложение |
|---|---|
| Ключевая фраза | `groothandel rhododendrons` |
| Title | Groothandel rhododendrons van de kweker \| Top Rhododendrons — 59 знаков, 581 px (предел 600) |
| Meta description | Groothandel in rhododendrons, rechtstreeks van de kweker in Otterlo. Zeven soorten, 40 tot 225 cm, vers gerooid met kluit. Vraag een offerte aan. — 145 знаков |
| H1 | Groothandel in rhododendrons. Rechtstreeks van de kweker. |
| Slug | `/groothandel` — оставить: совпадает с пунктом меню, на него уже ведут ссылки. Yoast даёт «частично» (6 из 9); менять адрес ради этого не стоит. |
| Alt фото hero | Ons rhododendronveld (как решено для главной, бэклог 19); без «op stam» и без «10.000+». |

Замечания:
- Формат заголовка совпадает с новыми страницами («Aangroeigarantie | Top Rhododendrons»): черта вместо точек-разделителей. Короткий запасной вариант: «Groothandel rhododendrons | Top Rhododendrons» (446 px).
- В описании только подтверждённые факты: семь сортов, 40–225 см, ком, Оттерло.
- Написание «rhododendron» через «rh» оставить везде; в официальном списке слов стоит «rododendron», но фирма, отрасль и весь новый сайт пишут через «rh».
- Слово «groothandel» строго означает посредника, а здесь продаёт сам питомник. Поэтому в H1 и в описании оно сразу уточнено: «rechtstreeks van de kweker».
- Yoast с этим текстом: SEO 83, читаемость 90, Flesch 72,9. Остаются «красными» только слова-связки (9,4 %) и ключ в подзаголовках; оба сознательно не исправлял, чтобы не утяжелять текст.
- Частотность запросов не проверялась. Перед запуском стоит сравнить в Google Search Console или в планировщике ключевых слов «groothandel rhododendrons», «rhododendron kweker» и «rhododendrons voor hoveniers».
