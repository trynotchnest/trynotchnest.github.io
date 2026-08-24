# -*- coding: utf-8 -*-
"""Translations for the remaining /learn/ articles across all non-English locales.
Assembled into ARTICLES (build_i18n_data) so build_article() renders them.
%STORE% is replaced with the locale App Store URL at build time."""
from build_i18n_articles import C, AUTHOR_LONG

READ5 = {"de": "5 Min. Lesedauer", "zh": "阅读 5 分钟", "ar": "قراءة 5 دقائق", "fr": "5 min de lecture",
         "pt-BR": "5 min de leitura", "pt-PT": "5 min de leitura", "es-MX": "5 min de lectura"}
READ6 = {"de": "6 Min. Lesedauer", "zh": "阅读 6 分钟", "ar": "قراءة 6 دقائق", "fr": "6 min de lecture",
         "pt-BR": "6 min de leitura", "pt-PT": "6 min de leitura", "es-MX": "6 min de lectura"}
KICK = {  # kicker labels reused across articles
    "basics": {"de": "Grundlagen", "zh": "基础", "ar": "الأساسيات", "fr": "Les bases", "pt-BR": "Básico", "pt-PT": "Básico", "es-MX": "Conceptos básicos"},
    "guide": {"de": "Anleitung", "zh": "指南", "ar": "دليل", "fr": "Guide", "pt-BR": "Guia", "pt-PT": "Guia", "es-MX": "Guía"},
    "explainer": {"de": "Erklärung", "zh": "解读", "ar": "شرح", "fr": "Explication", "pt-BR": "Explicação", "pt-PT": "Explicação", "es-MX": "Explicación"},
    "roundup": {"de": "Übersicht", "zh": "盘点", "ar": "اختيارات", "fr": "Sélection", "pt-BR": "Seleção", "pt-PT": "Seleção", "es-MX": "Selección"},
    "comparison": {"de": "Vergleich", "zh": "对比", "ar": "مقارنة", "fr": "Comparatif", "pt-BR": "Comparativo", "pt-PT": "Comparação", "es-MX": "Comparativa"},
}

# fixed yes/no/partial classes for the 3-way table (language-independent)
CLS3 = [("partial", "partial", "partial"), ("partial", "partial", "partial"), ("yes", "no", "partial"),
        ("yes", "no", "no"), ("yes", "no", "no"), ("yes", "no", "no"), ("yes", "no", "no"),
        ("yes", "partial", "no"), ("yes", "no", "partial"), ("yes", "no", "no"),
        ("partial", "yes", "no"), ("yes", "no", "no"), ("yes", "no", "no"),
        ("yes", "partial", "yes"), ("yes", "partial", "partial")]


def _table3(loc, th, feats, cells):
    head = f'<thead><tr><th>{th}</th><th>NotchNest</th><th>Boring Notch</th><th>NotchDrop</th></tr></thead>'
    body = ""
    for i, feat in enumerate(feats):
        c = cells[i]; cl = CLS3[i]
        body += (f'<tr><td>{feat}</td><td class="{cl[0]}">{c[0]}</td>'
                 f'<td class="{cl[1]}">{c[1]}</td><td class="{cl[2]}">{c[2]}</td></tr>')
    return f'<table class="cmp-table">{head}<tbody>{body}</tbody></table>'
RELATED_H2 = {"de": "Weiterlesen", "zh": "继续阅读", "ar": "اقرأ أيضًا", "fr": "À lire aussi", "pt-BR": "Continue lendo", "pt-PT": "Continue a ler", "es-MX": "Sigue leyendo"}

_LOCS = ["de", "zh", "ar", "fr", "pt-BR", "pt-PT", "es-MX"]


def _related(loc, extra_en):
    """Two localized links + one English fallback."""
    d = {"de": "de/", "zh": "zh/", "ar": "ar/", "fr": "fr/", "pt-BR": "pt-br/", "pt-PT": "pt-pt/", "es-MX": "es-mx/"}[loc]
    label = {"de": ("MacBook-Notch nutzen", "Drei Schritte zur nützlichen Notch.", "Beste macOS-Notch-Apps", "Übersicht 2026."),
             "zh": ("使用 MacBook 刘海", "三步让刘海有用。", "最佳 macOS 刘海应用", "2026 盘点。"),
             "ar": ("استخدام نتش الماك بوك", "ثلاث خطوات نحو نتش مفيد.", "أفضل تطبيقات نتش macOS", "اختيارات 2026."),
             "fr": ("Utiliser l'encoche du MacBook", "Trois étapes vers une encoche utile.", "Meilleures apps d'encoche macOS", "Sélection 2026."),
             "pt-BR": ("Usar o notch do MacBook", "Três passos para um notch útil.", "Melhores apps de notch macOS", "Seleção 2026."),
             "pt-PT": ("Usar o notch do MacBook", "Três passos para um notch útil.", "Melhores apps de notch macOS", "Seleção 2026."),
             "es-MX": ("Usar el notch del MacBook", "Tres pasos hacia un notch útil.", "Mejores apps de notch macOS", "Selección 2026.")}[loc]
    return [
        (f"/{d}learn/how-to-use-the-macbook-notch/", label[0], label[1]),
        (f"/{d}learn/best-macos-notch-apps/", label[2], label[3]),
        extra_en,
    ]


# ── what-is-the-macos-notch ─────────────────────────────────────────────────
WHATIS = {
    "de": {"title": "Was ist die macOS-Notch? — NotchNest",
           "description": "Die kleine schwarze Aussparung oben an neueren MacBooks. Was drinsteckt, welche Macs eine haben, wozu sie dient — und wie du sie wirklich nützlich machst.",
           "og_title": "Was ist die macOS-Notch?", "og_desc": "Was die Notch ist, welche Macs sie haben und wozu sie dient.",
           "jsonld_headline": "Was ist die macOS-Notch?", "jsonld_desc": "Die macOS-Notch erklärt: was drinsteckt, welche Macs eine haben und wie man sie nützlich macht.",
           "kicker": KICK["basics"]["de"], "h1": "Was ist die macOS-Notch?",
           "lede": "Die kleine schwarze Aussparung oben an neueren MacBooks. Hier, was drinsteckt, welche Macs eine haben, wozu sie dient — und wie du sie wirklich nützlich machst.",
           "readtime": READ5["de"], "crumb_this": "Was ist die macOS-Notch?",
           "faq": [("Welche Macs haben eine Notch?", "MacBook Pro 14\" und 16\" (ab 2021) sowie MacBook Air 13\" und 15\" (M2 und neuer). iMac, Mac mini, Mac Studio und Mac Pro haben keine."),
                   ("Ist die Notch dasselbe wie Dynamic Island?", "Nein. Dynamic Island ist eine Software-Funktion des iPhones. Die Mac-Notch ist nur eine physische Aussparung — macOS platziert selbst keine UI darin. Apps wie NotchNest füllen die Lücke."),
                   ("Kann ich die Notch loswerden?", "Apple lässt kein Entfernen zu, aber eine skalierte 16:10-Auflösung polstert den oberen Rand schwarz und versteckt sie. Du verlierst dabei etwa 75 vertikale Pixel Menüleiste.")],
           "body": """<p>Die <strong>macOS-Notch</strong> ist die kleine rechteckige Aussparung oben in der Mitte neuerer MacBook-Displays. Sie erschien erstmals im Oktober 2021, als Apple das MacBook Pro mit einer 1080p-FaceTime-HD-Kamera neu gestaltete. Um die größere Kamera unterzubringen, ohne den Rand höher zu machen, stanzte Apple ein Loch in den oberen Bildschirmrand — die Notch.</p>
    <p>Die Notch sitzt <em>innerhalb</em> der Menüleiste. Das ist der wichtige Punkt. Apple hat deinen Apps keinen Bildschirmplatz gestohlen; die Notch lebt in dem Bereich, den die Menüleiste ohnehin nutzte. Meist bemerkst du nur eine Uhr und ein WLAN-Symbol beiderseits einer schwarzen Lücke.</p>
    <h2>Welche Macs haben eine Notch?</h2>
    <p>Stand 2026 kommt die Notch bei diesen Modellen:</p>
    <ul>
      <li><strong>MacBook Pro 14"</strong> — M1 Pro/Max (2021), M2 Pro/Max (2023), M3 Pro/Max (2023), M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro 16"</strong> — dieselben Generationen wie das 14".</li>
      <li><strong>MacBook Air 13"</strong> — M2 (2022), M3 (2024), M4 (2025).</li>
      <li><strong>MacBook Air 15"</strong> — M2 (2023), M3 (2024), M4 (2025).</li>
    </ul>
    <p>Kein iMac, Mac mini, Mac Studio oder Mac Pro hat eine Notch — sie werden mit externen Displays gepaart, und die haben keine.</p>
    <h2>Warum ist sie da?</h2>
    <p>Drei Gründe:</p>
    <ol>
      <li><strong>Kameraqualität.</strong> Apple wollte denselben 1080p-FaceTime-Sensor wie beim iMac. Der ist physisch größer als die alte 720p-Kamera und braucht mehr vertikale Tiefe.</li>
      <li><strong>Mehr Bildschirm.</strong> Das Ausschneiden rund um die Kamera ließ Apple die Pixel bis zum oberen Gehäuserand schieben — daher die zusätzliche Menüleisten-Fläche auf beiden Seiten.</li>
      <li><strong>iPhone-Familienähnlichkeit.</strong> Apple arbeitet seit Jahren daran, dass sich jedes Bildschirmgerät verwandt anfühlt. Die Notch am Mac spiegelt den Look der Notch (und jetzt Dynamic Island) am iPhone.</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Mach deine Notch in 90 Sekunden nützlich</h3>
        <p>NotchNest verwandelt die Notch in eine Zentrale für Kalender, Zwischenablage, Notizen, Musik und AirDrop. Kostenlos.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>
    <h2>Ist die Notch dasselbe wie Dynamic Island?</h2>
    <p>Nein. Das <em>Dynamic Island</em> des iPhones ist eine Software-Funktion — eine aktiv animierte UI für Live-Aktivitäten (Timer, Musik, AirPods, Karten). Die Mac-Notch ist nur eine physische Aussparung. macOS selbst platziert keine UI darin.</p>
    <p>Diese Lücke füllen Drittanbieter-Apps. <a href="/de/">NotchNest</a> umhüllt die Notch mit einem <a href="/de/learn/how-to-use-the-macbook-notch/">hover-aktivierten Panel</a>: Zeiger drüber und die Notch klappt zu einer Glass-Widget-Oberfläche auf. Gleiche Hardware, komplett anderes Gefühl.</p>
    <h2>Steht die Notch im Weg?</h2>
    <p>Selten. macOS verschiebt Menüleisten-Icons automatisch um sie herum. Hast du <em>so viele</em> Menüleisten-Icons, dass sie mit der Notch kollidieren, werden die darunter versteckt, bis du in die Menüleiste klickst. Eine App wie Bartender oder Ice kann die Menüleiste kompakter machen — siehe unseren Leitfaden zum <a href="/de/">Anpassen der macOS-Menüleiste</a>.</p>
    <h2>Kann ich sie loswerden?</h2>
    <p>Apple lässt kein Entfernen zu, aber du kannst den Bildschirm so verhalten lassen, als wäre sie nicht da. <strong>Alle Auflösungen anzeigen → Skaliert</strong> gibt dir eine 16:10-Auflösung, die den oberen Rand schwarz polstert und die Notch hinter einem gleichmäßigen Balken versteckt. Dafür verlierst du rund 75 vertikale Pixel Menüleiste.</p>
    <p>Den meisten ist das ein schlechterer Deal, als die Notch einfach zu <em>nutzen</em>. Wenn du dir je ein iPhone-artiges Dynamic Island für deinen Mac gewünscht hast — genau das geben dir Apps wie NotchNest.</p>
    <h2>Das Fazit</h2>
    <p>Die Notch ist ein kleines Stück Hardware-Engineering, das einen winzigen kosmetischen Kompromiss gegen eine viel bessere Kamera und etwas mehr Bildschirm tauschte. Sie bleibt vorerst; Gerüchte sagen, Apple ersetze sie irgendwann durch ein Punch-Hole (oder eine Kamera unter dem Display), aber momentan ist sie ein prägendes Merkmal moderner MacBooks. Der kluge Zug ist, sie anzunehmen — gib der Notch etwas zu tun.</p>""",
           "related": _related("de", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Englisch — die Antwort."))},
    "zh": {"title": "什么是 macOS 刘海？— NotchNest",
           "description": "新款 MacBook 顶部那道黑色小缺口。里面有什么、哪些 Mac 有、它有什么用——以及如何让它真正好用。",
           "og_title": "什么是 macOS 刘海？", "og_desc": "刘海是什么、哪些 Mac 有、它有什么用。",
           "jsonld_headline": "什么是 macOS 刘海？", "jsonld_desc": "解释 macOS 刘海：里面有什么、哪些 Mac 有，以及如何让它好用。",
           "kicker": KICK["basics"]["zh"], "h1": "什么是 macOS 刘海？",
           "lede": "新款 MacBook 顶部那道黑色小缺口。这里讲清里面有什么、哪些 Mac 有、它有什么用——以及如何让它真正好用。",
           "readtime": READ5["zh"], "crumb_this": "什么是 macOS 刘海？",
           "faq": [("哪些 Mac 有刘海？", "MacBook Pro 14 英寸和 16 英寸（2021 年起）以及 MacBook Air 13 英寸和 15 英寸（M2 及更新）。iMac、Mac mini、Mac Studio 和 Mac Pro 没有。"),
                   ("刘海和灵动岛是一回事吗？", "不是。灵动岛是 iPhone 的软件功能。Mac 刘海只是物理缺口——macOS 本身不在其中放置界面。NotchNest 之类的应用填补了这一空缺。"),
                   ("我能去掉刘海吗？", "Apple 不允许移除，但缩放的 16:10 分辨率会把顶部填成黑色并将其隐藏，代价是损失约 75 像素的菜单栏高度。")],
           "body": """<p><strong>macOS 刘海</strong>是新款 MacBook 屏幕顶部居中的小矩形缺口。它于 2021 年 10 月首次出现，当时 Apple 重新设计 MacBook Pro，配备 1080p FaceTime 高清摄像头。为在不加高边框的情况下容纳更大的摄像头，Apple 在屏幕顶部开了一个口——即刘海。</p>
    <p>刘海位于菜单栏<em>内部</em>。这是关键。Apple 并没有从你的应用里挤占屏幕空间；刘海占用的是菜单栏本就使用的区域。多数时候你只会注意到一道黑色缺口两侧的时钟和 Wi-Fi 图标。</p>
    <h2>哪些 Mac 有刘海？</h2>
    <p>截至 2026 年，以下机型带刘海：</p>
    <ul>
      <li><strong>MacBook Pro 14 英寸</strong>——M1 Pro/Max（2021）、M2 Pro/Max（2023）、M3 Pro/Max（2023）、M4 Pro/Max（2024）。</li>
      <li><strong>MacBook Pro 16 英寸</strong>——与 14 英寸相同的世代。</li>
      <li><strong>MacBook Air 13 英寸</strong>——M2（2022）、M3（2024）、M4（2025）。</li>
      <li><strong>MacBook Air 15 英寸</strong>——M2（2023）、M3（2024）、M4（2025）。</li>
    </ul>
    <p>iMac、Mac mini、Mac Studio 或 Mac Pro 都没有刘海——它们搭配外接显示器，而外接显示器没有刘海。</p>
    <h2>为什么会有它？</h2>
    <p>三个原因：</p>
    <ol>
      <li><strong>摄像头质量。</strong>Apple 想用与 iMac 相同的 1080p FaceTime 传感器。它比旧的 720p 摄像头在物理上更大，需要更多纵向空间。</li>
      <li><strong>更大屏幕。</strong>环绕摄像头切割，让 Apple 把像素一直推到机身顶部，因此两侧多出一行菜单栏空间。</li>
      <li><strong>与 iPhone 家族呼应。</strong>Apple 多年来致力于让每块屏幕设备感觉相关。Mac 上的刘海呼应了 iPhone 刘海（如今的灵动岛）的外观。</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>90 秒让你的刘海有用</h3>
        <p>NotchNest 把刘海变成日历、剪贴板、笔记、音乐和 AirDrop 的中枢。免费。</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>
    <h2>刘海和灵动岛是一回事吗？</h2>
    <p>不是。iPhone 的<em>灵动岛</em>是软件功能——一个主动动画的界面，承载实时活动（计时器、音乐、AirPods、地图）。Mac 刘海只是物理缺口。macOS 本身不在其中放置任何界面。</p>
    <p>这正是第三方应用填补的空缺。<a href="/zh/">NotchNest</a> 用<a href="/zh/learn/how-to-use-the-macbook-notch/">悬停触发的面板</a>包裹刘海：光标悬停，刘海便展开为一块玻璃质感的组件面板。硬件相同，体验截然不同。</p>
    <h2>刘海会碍事吗？</h2>
    <p>很少。macOS 会自动在其周围排布菜单栏图标。若你的菜单栏图标<em>多到</em>会与刘海冲突，落在其下方的图标会被隐藏，直到你点进菜单栏。像 Bartender 或 Ice 这样的应用可以压缩菜单栏——参见我们的<a href="/zh/">自定义 macOS 菜单栏</a>指南。</p>
    <h2>我能去掉它吗？</h2>
    <p>Apple 不允许移除，但你可以让屏幕表现得仿佛它不存在。<strong>显示所有分辨率 → 缩放</strong>提供 16:10 分辨率，把屏幕顶部填成黑色，将刘海藏在一条均匀的黑边后。代价是损失约 75 像素的菜单栏高度。</p>
    <p>多数人觉得这比直接<em>使用</em>刘海更不划算。如果你曾希望 Mac 有 iPhone 式的灵动岛，NotchNest 这类应用给你的正是如此。</p>
    <h2>要点</h2>
    <p>刘海是一小段硬件工程，用极小的外观妥协换来了好得多的摄像头和略多的屏幕。它短期内不会消失；有传闻称 Apple 最终会用打孔（或屏下摄像头）取代它，但目前它是现代 MacBook 的标志性特征。聪明之举是拥抱它——给刘海找点事做。</p>""",
           "related": _related("zh", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "英文——答案。"))},
    "ar": {"title": "ما هو نتش macOS؟ — NotchNest",
           "description": "الفتحة السوداء الصغيرة أعلى أجهزة الماك بوك الأحدث. ما بداخلها، وأي أجهزة ماك تملكها، وما فائدتها — وكيف تجعلها مفيدة فعلًا.",
           "og_title": "ما هو نتش macOS؟", "og_desc": "ما هو النتش، وأي أجهزة ماك تملكه، وما فائدته.",
           "jsonld_headline": "ما هو نتش macOS؟", "jsonld_desc": "شرح نتش macOS: ما بداخله، وأي أجهزة ماك تملكه، وكيف تجعله مفيدًا.",
           "kicker": KICK["basics"]["ar"], "h1": "ما هو نتش macOS؟",
           "lede": "الفتحة السوداء الصغيرة أعلى أجهزة الماك بوك الأحدث. إليك ما بداخلها، وأي أجهزة ماك تملكها، وما فائدتها — وكيف تجعلها مفيدة فعلًا.",
           "readtime": READ5["ar"], "crumb_this": "ما هو نتش macOS؟",
           "faq": [("أي أجهزة ماك تملك نتشًا؟", "MacBook Pro مقاس 14 و16 بوصة (من 2021) وMacBook Air مقاس 13 و15 بوصة (M2 وأحدث). أما iMac وMac mini وMac Studio وMac Pro فلا تملكه."),
                   ("هل النتش هو نفسه Dynamic Island؟", "لا. Dynamic Island ميزة برمجية في الآيفون. أما نتش الماك فمجرد فتحة مادية — لا يضع macOS نفسه أي واجهة فيها. تطبيقات مثل NotchNest تسدّ الفراغ."),
                   ("هل يمكنني التخلّص من النتش؟", "لا تتيح Apple إزالته، لكن دقة 16:10 المُقاسة تملأ الأعلى بالأسود وتخفيه، مقابل خسارة نحو 75 بكسل من ارتفاع شريط القوائم.")],
           "body": """<p><strong>نتش macOS</strong> هو الفتحة المستطيلة الصغيرة أعلى منتصف شاشات الماك بوك الأحدث. ظهر أول مرة في أكتوبر 2021 حين أعادت Apple تصميم MacBook Pro ليأتي بكاميرا FaceTime HD بدقة 1080p. ولاستيعاب الكاميرا الأكبر دون زيادة سماكة الإطار، ثقبت Apple فتحة في أعلى الشاشة — النتش.</p>
    <p>يقع النتش <em>داخل</em> شريط القوائم. هذه هي النقطة المهمة. لم تسرق Apple مساحة من تطبيقاتك؛ فالنتش يعيش في مساحة كان شريط القوائم يستخدمها أصلًا. في معظم الوقت لا تلاحظ سوى ساعة وأيقونة واي فاي على جانبَي فجوة سوداء.</p>
    <h2>أي أجهزة ماك تملك نتشًا؟</h2>
    <p>حتى 2026، يأتي النتش في هذه الطُرز:</p>
    <ul>
      <li><strong>MacBook Pro مقاس 14"</strong> — M1 Pro/Max (2021)، M2 Pro/Max (2023)، M3 Pro/Max (2023)، M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro مقاس 16"</strong> — الأجيال نفسها كمقاس 14".</li>
      <li><strong>MacBook Air مقاس 13"</strong> — M2 (2022)، M3 (2024)، M4 (2025).</li>
      <li><strong>MacBook Air مقاس 15"</strong> — M2 (2023)، M3 (2024)، M4 (2025).</li>
    </ul>
    <p>لا يملك iMac أو Mac mini أو Mac Studio أو Mac Pro نتشًا — فهي تُقرن بشاشات خارجية، والشاشات الخارجية لا تملك نتشًا.</p>
    <h2>لماذا هو موجود؟</h2>
    <p>ثلاثة أسباب:</p>
    <ol>
      <li><strong>جودة الكاميرا.</strong> أرادت Apple مستشعر FaceTime بدقة 1080p نفسه الموجود في iMac. وهو أكبر ماديًا من كاميرا 720p القديمة ويحتاج عمقًا رأسيًا أكبر.</li>
      <li><strong>شاشة أكبر.</strong> سمح القطع حول الكاميرا لـ Apple بدفع البكسلات إلى أعلى هيكل الحاسوب، ولهذا تحصل على صف إضافي من مساحة شريط القوائم على الجانبين.</li>
      <li><strong>شبه عائلي مع الآيفون.</strong> تعمل Apple منذ سنوات على جعل كل جهاز بشاشة يبدو متصلًا. نتش الماك يعكس مظهر نتش الآيفون (والآن Dynamic Island).</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>اجعل نتشك مفيدًا في 90 ثانية</h3>
        <p>يحوّل NotchNest النتش إلى مركز للتقويم والحافظة والملاحظات والموسيقى وAirDrop. مجانًا.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>
    <h2>هل النتش هو نفسه Dynamic Island؟</h2>
    <p>لا. <em>Dynamic Island</em> في الآيفون ميزة برمجية — واجهة متحركة نشطة تستضيف الأنشطة المباشرة (المؤقتات والموسيقى وAirPods والخرائط). أما نتش الماك فمجرد فتحة مادية. لا يضع macOS نفسه أي واجهة فيها.</p>
    <p>هذا هو الفراغ الذي تملؤه تطبيقات الطرف الثالث. يغلّف <a href="/ar/">NotchNest</a> النتش بـ<a href="/ar/learn/how-to-use-the-macbook-notch/">لوحة تُفعَّل بالتمرير</a>: مرّر المؤشر فينفتح النتش إلى سطح زجاجي للأدوات. العتاد نفسه، وإحساس مختلف تمامًا.</p>
    <h2>هل يعترض النتش الطريق؟</h2>
    <p>نادرًا. ينقل macOS أيقونات شريط القوائم حوله تلقائيًا. وإن كان لديك <em>كثير</em> من الأيقونات بحيث تصطدم بالنتش، تُخفى التي تقع تحته حتى تنقر داخل شريط القوائم. يمكن لتطبيق مثل Bartender أو Ice ضغط شريط القوائم — راجع دليلنا حول <a href="/ar/">تخصيص شريط قوائم macOS</a>.</p>
    <h2>هل يمكنني التخلّص منه؟</h2>
    <p>لا تتيح Apple إزالته، لكن يمكنك جعل الشاشة تتصرّف كأنه غير موجود. <strong>إظهار كل الدقات ← مُقاس</strong> يمنحك دقة 16:10 تملأ أعلى الشاشة بالأسود وتخفي النتش خلف شريط موحّد. مقابل ذلك تخسر نحو 75 بكسل رأسيًا من شريط القوائم.</p>
    <p>يرى معظم الناس أن هذا أسوأ من مجرد <em>استخدام</em> النتش. إن تمنّيت يومًا أن يملك ماكك Dynamic Island بأسلوب الآيفون، فهذا بالضبط ما تمنحه تطبيقات مثل NotchNest.</p>
    <h2>الخلاصة</h2>
    <p>النتش قطعة صغيرة من هندسة العتاد بادلت تنازلًا تجميليًا ضئيلًا بكاميرا أفضل بكثير وشاشة أكبر قليلًا. لن يذهب قريبًا؛ تشير الشائعات إلى أن Apple ستستبدله في النهاية بثقب (أو كاميرا تحت الشاشة)، لكنه الآن سمة مميزة لأجهزة الماك بوك الحديثة. التصرّف الذكي هو احتضانه — امنح النتش ما يفعله.</p>""",
           "related": _related("ar", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "إنجليزي — الجواب."))},
    "fr": {"title": "Qu'est-ce que l'encoche macOS ? — NotchNest",
           "description": "La petite découpe noire en haut des MacBook récents. Ce qu'elle contient, quels Mac en ont une, à quoi elle sert — et comment la rendre vraiment utile.",
           "og_title": "Qu'est-ce que l'encoche macOS ?", "og_desc": "Ce qu'est l'encoche, quels Mac en ont une et à quoi elle sert.",
           "jsonld_headline": "Qu'est-ce que l'encoche macOS ?", "jsonld_desc": "L'encoche macOS expliquée : ce qu'elle contient, quels Mac en ont une et comment la rendre utile.",
           "kicker": KICK["basics"]["fr"], "h1": "Qu'est-ce que l'encoche macOS ?",
           "lede": "La petite découpe noire en haut des MacBook récents. Voici ce qu'elle contient, quels Mac en ont une, à quoi elle sert — et comment la rendre vraiment utile.",
           "readtime": READ5["fr"], "crumb_this": "Qu'est-ce que l'encoche macOS ?",
           "faq": [("Quels Mac ont une encoche ?", "Les MacBook Pro 14\" et 16\" (depuis 2021) et les MacBook Air 13\" et 15\" (M2 et plus récents). Ni l'iMac, ni le Mac mini, ni le Mac Studio, ni le Mac Pro n'en ont."),
                   ("L'encoche est-elle la même chose que Dynamic Island ?", "Non. Dynamic Island est une fonction logicielle de l'iPhone. L'encoche du Mac n'est qu'une découpe physique — macOS n'y place aucune interface. Des apps comme NotchNest comblent le vide."),
                   ("Puis-je m'en débarrasser ?", "Apple ne permet pas de la retirer, mais une résolution 16:10 mise à l'échelle rembourre le haut en noir et la cache, au prix d'environ 75 pixels verticaux de barre des menus.")],
           "body": """<p>L'<strong>encoche macOS</strong> est la petite découpe rectangulaire en haut au centre des écrans MacBook récents. Elle est apparue en octobre 2021, quand Apple a repensé le MacBook Pro avec une caméra FaceTime HD 1080p. Pour loger la caméra plus grande sans épaissir la bordure, Apple a percé un trou en haut de l'écran — l'encoche.</p>
    <p>L'encoche se trouve <em>à l'intérieur</em> de la barre des menus. C'est le point important. Apple n'a pas volé de place à vos apps ; l'encoche occupe l'espace que la barre des menus utilisait déjà. La plupart du temps, vous ne voyez qu'une horloge et une icône Wi-Fi de part et d'autre d'un espace noir.</p>
    <h2>Quels Mac ont une encoche ?</h2>
    <p>En 2026, l'encoche équipe ces modèles :</p>
    <ul>
      <li><strong>MacBook Pro 14"</strong> — M1 Pro/Max (2021), M2 Pro/Max (2023), M3 Pro/Max (2023), M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro 16"</strong> — mêmes générations que le 14".</li>
      <li><strong>MacBook Air 13"</strong> — M2 (2022), M3 (2024), M4 (2025).</li>
      <li><strong>MacBook Air 15"</strong> — M2 (2023), M3 (2024), M4 (2025).</li>
    </ul>
    <p>Aucun iMac, Mac mini, Mac Studio ou Mac Pro n'a d'encoche — ils s'associent à des écrans externes, qui n'en ont pas.</p>
    <h2>Pourquoi est-elle là ?</h2>
    <p>Trois raisons :</p>
    <ol>
      <li><strong>Qualité de la caméra.</strong> Apple voulait le même capteur FaceTime 1080p que sur l'iMac. Il est physiquement plus grand que l'ancienne caméra 720p et demande plus de profondeur verticale.</li>
      <li><strong>Plus d'écran.</strong> Découper autour de la caméra a permis à Apple de pousser les pixels jusqu'en haut du châssis, d'où la rangée supplémentaire de barre des menus de chaque côté.</li>
      <li><strong>Air de famille iPhone.</strong> Apple mène depuis des années une campagne pour que chaque appareil à écran paraisse apparenté. L'encoche du Mac reprend le look de l'encoche (et désormais Dynamic Island) de l'iPhone.</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Rendez votre encoche utile en 90 secondes</h3>
        <p>NotchNest transforme l'encoche en centre pour calendrier, presse-papiers, notes, musique et AirDrop. Gratuit.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>
    <h2>L'encoche est-elle la même chose que Dynamic Island ?</h2>
    <p>Non. Le <em>Dynamic Island</em> de l'iPhone est une fonction logicielle — une interface animée en direct qui héberge les activités en direct (minuteurs, musique, AirPods, Plans). L'encoche du Mac n'est qu'une découpe physique. macOS lui-même n'y met aucune interface.</p>
    <p>C'est ce vide que comblent les apps tierces. <a href="/fr/">NotchNest</a> entoure l'encoche d'un <a href="/fr/learn/how-to-use-the-macbook-notch/">panneau activé au survol</a> : survolez avec le curseur et l'encoche se déploie en une surface de widgets en verre. Même matériel, ressenti totalement différent.</p>
    <h2>L'encoche gêne-t-elle ?</h2>
    <p>Rarement. macOS déplace automatiquement les icônes de la barre des menus autour d'elle. Si vous avez <em>tant</em> d'icônes qu'elles entreraient en collision avec l'encoche, celles qui passeraient dessous sont masquées jusqu'à ce que vous cliquiez dans la barre des menus. Une app comme Bartender ou Ice peut compacter la barre des menus — voyez notre guide sur <a href="/fr/">la personnalisation de la barre des menus macOS</a>.</p>
    <h2>Puis-je m'en débarrasser ?</h2>
    <p>Apple ne permet pas de la retirer, mais vous pouvez faire en sorte que l'écran se comporte comme si elle n'était pas là. <strong>Afficher toutes les résolutions → Mise à l'échelle</strong> vous donne une résolution 16:10 qui rembourre le haut en noir et cache l'encoche derrière une barre uniforme. En échange, vous perdez environ 75 pixels verticaux de barre des menus.</p>
    <p>La plupart des gens trouvent que c'est un moins bon marché que d'<em>utiliser</em> l'encoche. Si vous avez déjà rêvé d'un Dynamic Island façon iPhone sur votre Mac, c'est exactement ce que vous donnent des apps comme NotchNest.</p>
    <h2>À retenir</h2>
    <p>L'encoche est une petite prouesse d'ingénierie matérielle qui a troqué un minuscule compromis esthétique contre une bien meilleure caméra et un peu plus d'écran. Elle ne partira pas de sitôt ; des rumeurs suggèrent qu'Apple la remplacera à terme par un poinçon (ou une caméra sous l'écran), mais pour l'instant c'est une caractéristique déterminante des MacBook modernes. Le bon réflexe est de l'adopter — donnez à l'encoche quelque chose à faire.</p>""",
           "related": _related("fr", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Anglais — la réponse."))},
    "pt-BR": {"title": "O que é o notch do macOS? — NotchNest",
              "description": "O pequeno recorte preto no topo dos MacBooks mais novos. O que há nele, quais Macs têm, para que serve — e como torná-lo realmente útil.",
              "og_title": "O que é o notch do macOS?", "og_desc": "O que é o notch, quais Macs têm e para que serve.",
              "jsonld_headline": "O que é o notch do macOS?", "jsonld_desc": "O notch do macOS explicado: o que há nele, quais Macs têm e como torná-lo útil.",
              "kicker": KICK["basics"]["pt-BR"], "h1": "O que é o notch do macOS?",
              "lede": "O pequeno recorte preto no topo dos MacBooks mais novos. Veja o que há nele, quais Macs têm, para que serve — e como torná-lo realmente útil.",
              "readtime": READ5["pt-BR"], "crumb_this": "O que é o notch do macOS?",
              "faq": [("Quais Macs têm notch?", "MacBook Pro de 14\" e 16\" (a partir de 2021) e MacBook Air de 13\" e 15\" (M2 e mais novos). iMac, Mac mini, Mac Studio e Mac Pro não têm."),
                      ("O notch é o mesmo que o Dynamic Island?", "Não. O Dynamic Island é um recurso de software do iPhone. O notch do Mac é só um recorte físico — o macOS não coloca interface nele. Apps como o NotchNest preenchem a lacuna."),
                      ("Posso me livrar do notch?", "A Apple não permite removê-lo, mas uma resolução 16:10 escalada preenche o topo de preto e o esconde, ao custo de cerca de 75 pixels verticais de barra de menus.")],
              "body": """<p>O <strong>notch do macOS</strong> é o pequeno recorte retangular no topo central das telas dos MacBooks mais novos. Ele surgiu em outubro de 2021, quando a Apple redesenhou o MacBook Pro com uma câmera FaceTime HD de 1080p. Para acomodar a câmera maior sem engrossar a borda, a Apple abriu um furo no topo da tela — o notch.</p>
    <p>O notch fica <em>dentro</em> da barra de menus. Esse é o ponto importante. A Apple não roubou espaço de tela dos seus apps; o notch ocupa a área que a barra de menus já usava. Na maior parte do tempo, você só nota um relógio e um ícone de Wi-Fi dos dois lados de um vão preto.</p>
    <h2>Quais Macs têm notch?</h2>
    <p>Em 2026, o notch vem nestes modelos:</p>
    <ul>
      <li><strong>MacBook Pro de 14"</strong> — M1 Pro/Max (2021), M2 Pro/Max (2023), M3 Pro/Max (2023), M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro de 16"</strong> — mesmas gerações do 14".</li>
      <li><strong>MacBook Air de 13"</strong> — M2 (2022), M3 (2024), M4 (2025).</li>
      <li><strong>MacBook Air de 15"</strong> — M2 (2023), M3 (2024), M4 (2025).</li>
    </ul>
    <p>Nenhum iMac, Mac mini, Mac Studio ou Mac Pro tem notch — eles usam telas externas, que não têm.</p>
    <h2>Por que ele está aí?</h2>
    <p>Três motivos:</p>
    <ol>
      <li><strong>Qualidade da câmera.</strong> A Apple queria o mesmo sensor FaceTime de 1080p do iMac. Ele é fisicamente maior que a câmera 720p antiga e precisa de mais profundidade vertical.</li>
      <li><strong>Mais tela.</strong> Recortar ao redor da câmera permitiu à Apple empurrar os pixels até o topo do chassi, por isso você ganha uma fileira extra de barra de menus de cada lado.</li>
      <li><strong>Semelhança de família com o iPhone.</strong> Há anos a Apple busca fazer cada dispositivo com tela parecer relacionado. O notch no Mac espelha o visual do notch (e agora do Dynamic Island) do iPhone.</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Torne seu notch útil em 90 segundos</h3>
        <p>O NotchNest transforma o notch em uma central para calendário, área de transferência, notas, música e AirDrop. Grátis.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>
    <h2>O notch é o mesmo que o Dynamic Island?</h2>
    <p>Não. O <em>Dynamic Island</em> do iPhone é um recurso de software — uma interface animada que hospeda as Atividades ao Vivo (timers, música, AirPods, Mapas). O notch do Mac é só um recorte físico. O próprio macOS não coloca nenhuma interface nele.</p>
    <p>Essa é a lacuna que os apps de terceiros preenchem. O <a href="/pt-br/">NotchNest</a> envolve o notch em um <a href="/pt-br/learn/how-to-use-the-macbook-notch/">painel ativado ao passar o cursor</a>: passe o cursor e o notch se expande em uma superfície de widgets de vidro. Mesmo hardware, sensação totalmente diferente.</p>
    <h2>O notch atrapalha?</h2>
    <p>Raramente. O macOS desloca os ícones da barra de menus automaticamente ao redor dele. Se você tiver <em>tantos</em> ícones que colidiriam com o notch, os que ficariam embaixo são ocultados até você clicar na barra de menus. Um app como Bartender ou Ice pode compactar a barra de menus — veja nosso guia sobre <a href="/pt-br/">como personalizar a barra de menus do macOS</a>.</p>
    <h2>Posso me livrar dele?</h2>
    <p>A Apple não permite removê-lo, mas você pode fazer a tela se comportar como se ele não estivesse lá. <strong>Mostrar todas as resoluções → Escalada</strong> dá uma resolução 16:10 que preenche o topo de preto e esconde o notch atrás de uma barra uniforme. Em troca, você perde cerca de 75 pixels verticais de barra de menus.</p>
    <p>A maioria acha isso um negócio pior do que simplesmente <em>usar</em> o notch. Se você já quis um Dynamic Island estilo iPhone no seu Mac, é exatamente isso que apps como o NotchNest oferecem.</p>
    <h2>A conclusão</h2>
    <p>O notch é uma pequena peça de engenharia de hardware que trocou um compromisso estético mínimo por uma câmera muito melhor e um pouco mais de tela. Ele não vai a lugar nenhum tão cedo; rumores sugerem que a Apple acabará substituindo-o por um furo (ou câmera sob a tela), mas por ora é uma característica marcante dos MacBooks modernos. O movimento esperto é abraçá-lo — dê ao notch algo para fazer.</p>""",
              "related": _related("pt-BR", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglês — a resposta."))},
    "pt-PT": {"title": "O que é o notch do macOS? — NotchNest",
              "description": "O pequeno recorte preto no topo dos MacBooks mais recentes. O que há nele, que Macs têm, para que serve — e como torná-lo realmente útil.",
              "og_title": "O que é o notch do macOS?", "og_desc": "O que é o notch, que Macs têm e para que serve.",
              "jsonld_headline": "O que é o notch do macOS?", "jsonld_desc": "O notch do macOS explicado: o que há nele, que Macs têm e como torná-lo útil.",
              "kicker": KICK["basics"]["pt-PT"], "h1": "O que é o notch do macOS?",
              "lede": "O pequeno recorte preto no topo dos MacBooks mais recentes. Veja o que há nele, que Macs têm, para que serve — e como torná-lo realmente útil.",
              "readtime": READ5["pt-PT"], "crumb_this": "O que é o notch do macOS?",
              "faq": [("Que Macs têm notch?", "MacBook Pro de 14\" e 16\" (a partir de 2021) e MacBook Air de 13\" e 15\" (M2 e mais recentes). iMac, Mac mini, Mac Studio e Mac Pro não têm."),
                      ("O notch é o mesmo que o Dynamic Island?", "Não. O Dynamic Island é uma funcionalidade de software do iPhone. O notch do Mac é só um recorte físico — o macOS não coloca interface nele. Apps como o NotchNest preenchem a lacuna."),
                      ("Posso livrar-me do notch?", "A Apple não permite removê-lo, mas uma resolução 16:10 escalada preenche o topo a preto e esconde-o, ao custo de cerca de 75 pixels verticais de barra de menus.")],
              "body": """<p>O <strong>notch do macOS</strong> é o pequeno recorte retangular no topo central dos ecrãs dos MacBooks mais recentes. Surgiu em outubro de 2021, quando a Apple redesenhou o MacBook Pro com uma câmara FaceTime HD de 1080p. Para acomodar a câmara maior sem engrossar a moldura, a Apple abriu um furo no topo do ecrã — o notch.</p>
    <p>O notch fica <em>dentro</em> da barra de menus. Esse é o ponto importante. A Apple não roubou espaço de ecrã às suas apps; o notch ocupa a área que a barra de menus já usava. Na maioria do tempo, só repara num relógio e num ícone de Wi-Fi dos dois lados de um vão preto.</p>
    <h2>Que Macs têm notch?</h2>
    <p>Em 2026, o notch vem nestes modelos:</p>
    <ul>
      <li><strong>MacBook Pro de 14"</strong> — M1 Pro/Max (2021), M2 Pro/Max (2023), M3 Pro/Max (2023), M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro de 16"</strong> — as mesmas gerações do 14".</li>
      <li><strong>MacBook Air de 13"</strong> — M2 (2022), M3 (2024), M4 (2025).</li>
      <li><strong>MacBook Air de 15"</strong> — M2 (2023), M3 (2024), M4 (2025).</li>
    </ul>
    <p>Nenhum iMac, Mac mini, Mac Studio ou Mac Pro tem notch — usam ecrãs externos, que não têm.</p>
    <h2>Porque está lá?</h2>
    <p>Três razões:</p>
    <ol>
      <li><strong>Qualidade da câmara.</strong> A Apple queria o mesmo sensor FaceTime de 1080p do iMac. É fisicamente maior do que a câmara 720p antiga e precisa de mais profundidade vertical.</li>
      <li><strong>Mais ecrã.</strong> Recortar à volta da câmara permitiu à Apple empurrar os pixels até ao topo do chassis, por isso ganha uma fila extra de barra de menus de cada lado.</li>
      <li><strong>Semelhança de família com o iPhone.</strong> Há anos que a Apple procura fazer cada dispositivo com ecrã parecer relacionado. O notch no Mac espelha o visual do notch (e agora do Dynamic Island) do iPhone.</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Torne o seu notch útil em 90 segundos</h3>
        <p>O NotchNest transforma o notch numa central para calendário, área de transferência, notas, música e AirDrop. Gratuito.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>
    <h2>O notch é o mesmo que o Dynamic Island?</h2>
    <p>Não. O <em>Dynamic Island</em> do iPhone é uma funcionalidade de software — uma interface animada que aloja as Atividades Live (temporizadores, música, AirPods, Mapas). O notch do Mac é só um recorte físico. O próprio macOS não coloca nenhuma interface nele.</p>
    <p>Essa é a lacuna que as apps de terceiros preenchem. O <a href="/pt-pt/">NotchNest</a> envolve o notch num <a href="/pt-pt/learn/how-to-use-the-macbook-notch/">painel ativado ao passar o cursor</a>: passe o cursor e o notch expande-se numa superfície de widgets de vidro. O mesmo hardware, uma sensação totalmente diferente.</p>
    <h2>O notch atrapalha?</h2>
    <p>Raramente. O macOS desloca os ícones da barra de menus automaticamente à volta dele. Se tiver <em>tantos</em> ícones que colidiriam com o notch, os que ficariam por baixo são ocultados até clicar na barra de menus. Uma app como o Bartender ou o Ice pode compactar a barra de menus — veja o nosso guia sobre <a href="/pt-pt/">como personalizar a barra de menus do macOS</a>.</p>
    <h2>Posso livrar-me dele?</h2>
    <p>A Apple não permite removê-lo, mas pode fazer o ecrã comportar-se como se ele não estivesse lá. <strong>Mostrar todas as resoluções → Escalado</strong> dá uma resolução 16:10 que preenche o topo a preto e esconde o notch atrás de uma barra uniforme. Em troca, perde cerca de 75 pixels verticais de barra de menus.</p>
    <p>A maioria acha isto um pior negócio do que simplesmente <em>usar</em> o notch. Se alguma vez desejou um Dynamic Island estilo iPhone no seu Mac, é exatamente isso que apps como o NotchNest oferecem.</p>
    <h2>A conclusão</h2>
    <p>O notch é uma pequena peça de engenharia de hardware que trocou um compromisso estético mínimo por uma câmara muito melhor e um pouco mais de ecrã. Não vai a lado nenhum tão cedo; rumores sugerem que a Apple acabará por substituí-lo por um furo (ou câmara sob o ecrã), mas por agora é uma característica marcante dos MacBooks modernos. O movimento inteligente é aceitá-lo — dê ao notch algo para fazer.</p>""",
              "related": _related("pt-PT", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglês — a resposta."))},
    "es-MX": {"title": "¿Qué es el notch de macOS? — NotchNest",
              "description": "El pequeño recorte negro en la parte superior de los MacBook más nuevos. Qué hay dentro, qué Macs lo tienen, para qué sirve — y cómo hacerlo realmente útil.",
              "og_title": "¿Qué es el notch de macOS?", "og_desc": "Qué es el notch, qué Macs lo tienen y para qué sirve.",
              "jsonld_headline": "¿Qué es el notch de macOS?", "jsonld_desc": "El notch de macOS explicado: qué hay dentro, qué Macs lo tienen y cómo hacerlo útil.",
              "kicker": KICK["basics"]["es-MX"], "h1": "¿Qué es el notch de macOS?",
              "lede": "El pequeño recorte negro en la parte superior de los MacBook más nuevos. Aquí qué hay dentro, qué Macs lo tienen, para qué sirve — y cómo hacerlo realmente útil.",
              "readtime": READ5["es-MX"], "crumb_this": "¿Qué es el notch de macOS?",
              "faq": [("¿Qué Macs tienen notch?", "MacBook Pro de 14\" y 16\" (desde 2021) y MacBook Air de 13\" y 15\" (M2 y posteriores). Ni el iMac, ni el Mac mini, ni el Mac Studio, ni el Mac Pro lo tienen."),
                      ("¿El notch es lo mismo que el Dynamic Island?", "No. El Dynamic Island es una función de software del iPhone. El notch del Mac es solo un recorte físico — macOS no coloca ninguna interfaz ahí. Apps como NotchNest llenan el vacío."),
                      ("¿Puedo quitármelo?", "Apple no permite eliminarlo, pero una resolución 16:10 escalada rellena la parte superior de negro y lo oculta, a costa de unos 75 píxeles verticales de barra de menús.")],
              "body": """<p>El <strong>notch de macOS</strong> es el pequeño recorte rectangular en la parte superior central de las pantallas de los MacBook más nuevos. Apareció por primera vez en octubre de 2021, cuando Apple rediseñó el MacBook Pro con una cámara FaceTime HD de 1080p. Para alojar la cámara más grande sin engrosar el marco, Apple abrió un hueco en la parte superior de la pantalla — el notch.</p>
    <p>El notch está <em>dentro</em> de la barra de menús. Ese es el punto clave. Apple no le robó espacio de pantalla a tus apps; el notch ocupa el área que la barra de menús ya usaba. La mayor parte del tiempo solo notas un reloj y un icono de Wi-Fi a ambos lados de un hueco negro.</p>
    <h2>¿Qué Macs tienen notch?</h2>
    <p>En 2026, el notch viene en estos modelos:</p>
    <ul>
      <li><strong>MacBook Pro de 14"</strong> — M1 Pro/Max (2021), M2 Pro/Max (2023), M3 Pro/Max (2023), M4 Pro/Max (2024).</li>
      <li><strong>MacBook Pro de 16"</strong> — las mismas generaciones que el de 14".</li>
      <li><strong>MacBook Air de 13"</strong> — M2 (2022), M3 (2024), M4 (2025).</li>
      <li><strong>MacBook Air de 15"</strong> — M2 (2023), M3 (2024), M4 (2025).</li>
    </ul>
    <p>Ningún iMac, Mac mini, Mac Studio o Mac Pro tiene notch — usan pantallas externas, que no lo tienen.</p>
    <h2>¿Por qué está ahí?</h2>
    <p>Tres razones:</p>
    <ol>
      <li><strong>Calidad de cámara.</strong> Apple quería el mismo sensor FaceTime de 1080p del iMac. Es físicamente más grande que la cámara 720p antigua y necesita más profundidad vertical.</li>
      <li><strong>Más pantalla.</strong> Recortar alrededor de la cámara permitió a Apple llevar los píxeles hasta la parte superior del chasis, por eso ganas una fila extra de barra de menús a cada lado.</li>
      <li><strong>Parecido de familia con el iPhone.</strong> Apple lleva años buscando que cada dispositivo con pantalla se sienta emparentado. El notch en el Mac refleja el aspecto del notch (y ahora del Dynamic Island) del iPhone.</li>
    </ol>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Haz útil tu notch en 90 segundos</h3>
        <p>NotchNest convierte el notch en un centro para calendario, portapapeles, notas, música y AirDrop. Gratis.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>
    <h2>¿El notch es lo mismo que el Dynamic Island?</h2>
    <p>No. El <em>Dynamic Island</em> del iPhone es una función de software — una interfaz animada en vivo que aloja las Actividades en Vivo (temporizadores, música, AirPods, Mapas). El notch del Mac es solo un recorte físico. El propio macOS no coloca ninguna interfaz ahí.</p>
    <p>Ese es el vacío que llenan las apps de terceros. <a href="/es-mx/">NotchNest</a> envuelve el notch en un <a href="/es-mx/learn/how-to-use-the-macbook-notch/">panel activado al pasar el cursor</a>: pasa el cursor y el notch se expande en una superficie de widgets de vidrio. Mismo hardware, sensación totalmente distinta.</p>
    <h2>¿El notch estorba?</h2>
    <p>Rara vez. macOS reacomoda los iconos de la barra de menús automáticamente a su alrededor. Si tienes <em>tantos</em> iconos que chocarían con el notch, los que quedarían debajo se ocultan hasta que haces clic en la barra de menús. Una app como Bartender o Ice puede compactar la barra de menús — mira nuestra guía sobre <a href="/es-mx/">cómo personalizar la barra de menús de macOS</a>.</p>
    <h2>¿Puedo quitármelo?</h2>
    <p>Apple no permite eliminarlo, pero puedes hacer que la pantalla se comporte como si no estuviera. <strong>Mostrar todas las resoluciones → Escalada</strong> te da una resolución 16:10 que rellena la parte superior de negro y oculta el notch tras una barra uniforme. A cambio, pierdes unos 75 píxeles verticales de barra de menús.</p>
    <p>A la mayoría le parece peor trato que simplemente <em>usar</em> el notch. Si alguna vez deseaste un Dynamic Island estilo iPhone en tu Mac, eso es exactamente lo que te dan apps como NotchNest.</p>
    <h2>La conclusión</h2>
    <p>El notch es una pequeña pieza de ingeniería de hardware que cambió un mínimo compromiso estético por una cámara mucho mejor y algo más de pantalla. No se irá pronto; los rumores sugieren que Apple acabará reemplazándolo por un perforado (o cámara bajo la pantalla), pero por ahora es un rasgo distintivo de los MacBook modernos. La jugada inteligente es adoptarlo — dale al notch algo que hacer.</p>""",
              "related": _related("es-MX", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglés — la respuesta."))},
}


def _assemble(src):
    out = {}
    for loc, d in src.items():
        row = dict(C[loc])
        row.update(d)
        row["author_h3"] = C[loc]["author_h3"]
        row["author_bio"] = AUTHOR_LONG[loc]
        row["related_h2"] = RELATED_H2[loc]
        out[loc] = row
    return out


# ── does-the-mac-notch-actually-do-anything ─────────────────────────────────
DOES = {
    "de": {"title": "Macht die Mac-Notch überhaupt etwas? — NotchNest",
           "description": "Die ehrliche Antwort, ob die MacBook-Notch standardmäßig etwas tut, was Apple dahinter gesetzt hat und wie Drittanbieter-Apps sie nützlich machen.",
           "og_title": "Macht die Mac-Notch überhaupt etwas?", "og_desc": "Was die Notch standardmäßig tut und wie man ihr eine Aufgabe gibt.",
           "jsonld_headline": "Macht die Mac-Notch überhaupt etwas?", "jsonld_desc": "Was die MacBook-Notch standardmäßig tut, was drinsteckt und wie Apps sie nützlich machen.",
           "kicker": KICK["explainer"]["de"], "h1": "Macht die Mac-Notch überhaupt etwas?",
           "lede": "Apple liefert die Notch als dekorativen Raum. Hier die ehrliche Antwort, was sie ab Werk tut, was drinsteckt und wie du ihr eine echte Aufgabe gibst.",
           "readtime": READ5["de"], "crumb_this": "Macht die Notch etwas?",
           "faq": [("Hat die Mac-Notch Face ID?", "Nein. Die Notch enthält nur die 1080p-FaceTime-Kamera und einen Umgebungslichtsensor — kein TrueDepth-Array, kein Face ID. Touch ID auf der Tastatur deckt die Authentifizierung ab."),
                   ("Tut die Notch standardmäßig etwas?", "Kaum. macOS zeigt einen grünen Punkt bei aktiver Kamera, verschiebt Menüleisten-Icons um sie herum und kann Vollbildvideo polstern. Keine Widget-Oberfläche."),
                   ("Kann ich die Notch nützlich machen?", "Ja, mit einer Installation. Apps wie NotchNest fügen ein hover-aktiviertes Panel mit Kalender, KI-Zwischenablage, Notizen, Pomodoro, Musik und AirDrop hinzu.")],
           "body": """<p>Die kurze Antwort: Nein, die macOS-Notch tut standardmäßig nichts. Sie ist eine Aussparung, die eine Kamera hält. macOS zeichnet die Menüleiste um sie herum und lässt den Rest als schwarzen Raum.</p>
    <p>Das ist 2026 eine seltsame Antwort, wo das iPhone die Kamera-Aussparung seit drei Jahren in das nützlichste UI-Element des Telefons verwandelt (Dynamic Island). Also schauen wir uns an, was tatsächlich drinsteckt, was sie könnte und was du tun kannst.</p>
    <h2>Was steckt in der Notch?</h2>
    <ul>
      <li><strong>1080p-FaceTime-HD-Kamera.</strong> Der Grund für die Notch. Größerer Sensor als die 720p-Kamera davor — besser bei wenig Licht, schärfer.</li>
      <li><strong>Umgebungslichtsensor.</strong> Passt True Tone und Displayhelligkeit an.</li>
      <li><strong>Das war's.</strong> Kein TrueDepth-Array, kein Face ID, kein Infrarot, kein LiDAR.</li>
    </ul>
    <p>Das fehlende Face ID ist die meistgestellte Frage und die enttäuschendste Antwort. Apple hat die Hardware. Sie liefern sie nur nicht am Mac aus — wohl weil Touch ID auf der Tastatur die meisten Authentifizierungsbedürfnisse abdeckt.</p>
    <h2>Was macht macOS mit der Notch?</h2>
    <p>Fast nichts. Insgesamt drei Dinge:</p>
    <ul>
      <li>Ein grüner Punkt am rechten Rand der Notch leuchtet, wenn die Kamera aktiv ist.</li>
      <li>Es leitet die Menüleiste um sie herum. Icons, die darunter landen würden, werden versteckt, bis du in die Menüleiste klickst.</li>
      <li>Es polstert sie bei Vollbildvideo. macOS kann den oberen Rand von Vollbildinhalten optional letterboxen, damit er nicht von der Notch geschnitten wird.</li>
    </ul>
    <p>Es gibt keine Widget-Oberfläche. Kein Tap-Ziel. Kein Drag-Ziel. Kein Hover-Verhalten. Die Notch ist für Systemzwecke ein höfliches Loch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Gib deiner Notch in 90 Sekunden eine Aufgabe</h3>
        <p>NotchNest fügt der leeren Notch Kalender, KI-Zwischenablage, Notizen, Pomodoro, Musik und AirDrop hinzu. Kostenlos.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>
    <h2>Warum hat Apple keine UI in die Notch gesetzt?</h2>
    <p>Ein paar wahrscheinliche Gründe:</p>
    <ul>
      <li><strong>Der Cursor.</strong> Das Dynamic Island des iPhones funktioniert, weil dein Finger es berührt. Am Mac müsstest du den Cursor zur Notch bewegen — und macOS hat dafür schon ein Kontrollzentrum.</li>
      <li><strong>Auffindbarkeit.</strong> Eine neue interaktive Zone ohne sichtbaren Hinweis ist schwer zu vermitteln. Die meisten würden sie nie finden.</li>
      <li><strong>Mehrere Displays.</strong> Die Notch existiert nur auf dem eingebauten Laptop-Display. UI, die nur auf einem Bildschirm funktioniert, wäre inkonsistent.</li>
    </ul>
    <p>Ob das gute Gründe sind, hängt davon ab, wie sehr du den verschwendeten Platz schätzt. Drittanbieter-Entwickler sind klar anderer Meinung — siehe die besten macOS-Notch-Apps — und haben die interaktive Schicht gebaut, die Apple nicht liefert.</p>
    <h2>Kann die Notch nützlich sein?</h2>
    <p>Ja, mit einer Installation. Apps wie NotchNest fügen ein hover-aktiviertes Panel hinzu: Bewege den Cursor zur Notch und sie klappt zu einer Glass-Widget-Oberfläche auf. Ein kleiner UX-Trick, der das Auffindbarkeitsproblem löst (du lernst die Hover-Geste mit der Zeit) und Platz nutzt, der leer war.</p>
    <p>Was du dort unterbringen kannst:</p>
    <ul>
      <li>Heutiger Kalender mit KI-generierten Meeting-Briefings</li>
      <li>KI-Zwischenablage-Verlauf mit Umformulieren und Zusammenfassen</li>
      <li>Schnellnotizen (mit KI-Verfeinerung, iCloud-Sync)</li>
      <li>Pomodoro-Timer mit Pausenzyklen</li>
      <li>Now Playing für Spotify oder Apple Music</li>
      <li>Drag-to-AirDrop und Datei-Tray für Dateien in Arbeit</li>
      <li>Kamera-Spiegel für Ein-Tipp-Webcam-Vorschau</li>
      <li>Lesezeichen-Shelf für Ein-Klick-Seitenstart</li>
    </ul>
    <h2>Wo ist der Haken?</h2>
    <p>Ehrlich, kaum einer. Notch-Apps leben in der Menüleiste, schlafen im Leerlauf und nutzen einstellige MB RAM. Kein messbarer Akkueinfluss. Der Haken ist, dass du dich erinnern musst, dass die Notch interaktiv ist — sobald du das tust, nutzt du sie ständig.</p>
    <h2>Das Fazit</h2>
    <p>Ab Werk tut die Mac-Notch nichts, außer eine Kamera zu halten. Das ist die wahrheitsgemäße Antwort. Aber die Hardware ist da, der Bildschirmplatz ist da, und ein kostenloser Download behebt das Problem. Wenn du deine Notch die letzten Jahre ignoriert hast, sind zehn Minuten deiner Zeit es wert.</p>""",
           "related": _related("de", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Übersicht 2026."))},
    "zh": {"title": "Mac 刘海到底有没有用？— NotchNest",
           "description": "关于 MacBook 刘海默认是否有用、Apple 在它后面放了什么，以及第三方应用如何让它有用的直接答案。",
           "og_title": "Mac 刘海到底有没有用？", "og_desc": "刘海默认做什么，以及如何给它派活。",
           "jsonld_headline": "Mac 刘海到底有没有用？", "jsonld_desc": "MacBook 刘海默认做什么、里面有什么，以及应用如何让它有用。",
           "kicker": KICK["explainer"]["zh"], "h1": "Mac 刘海到底有没有用？",
           "lede": "Apple 把刘海当作装饰空间。这里给出诚实答案：它开箱即用时做什么、里面有什么，以及如何给它派上真正的活。",
           "readtime": READ5["zh"], "crumb_this": "刘海有用吗？",
           "faq": [("Mac 刘海有 Face ID 吗？", "没有。刘海只包含 1080p FaceTime 摄像头和一个环境光传感器——没有 TrueDepth 阵列，没有 Face ID。键盘上的触控 ID 负责身份验证。"),
                   ("刘海默认会做什么吗？", "几乎不会。macOS 在摄像头启用时亮起绿点、在其周围排布菜单栏图标、并可为全屏视频加边。没有组件界面。"),
                   ("我能让刘海有用吗？", "能，装一个应用即可。NotchNest 之类的应用会加入悬停触发的面板，含日历、AI 剪贴板、笔记、番茄钟、音乐和 AirDrop。")],
           "body": """<p>简短答案：不，macOS 刘海默认什么都不做。它是一个容纳摄像头的缺口。macOS 在它周围绘制菜单栏，其余留作黑色空间。</p>
    <p>放在 2026 年，这是个奇怪的答案——毕竟三年来 iPhone 一直把摄像头缺口变成手机上最有用的界面元素（灵动岛）。那么我们来拆解它里面究竟有什么、它能做什么，以及你能做什么。</p>
    <h2>刘海里有什么？</h2>
    <ul>
      <li><strong>1080p FaceTime 高清摄像头。</strong>刘海存在的原因。传感器比之前的 720p 摄像头更大——弱光更好、更清晰。</li>
      <li><strong>环境光传感器。</strong>调节原彩显示与屏幕亮度。</li>
      <li><strong>就这些。</strong>没有 TrueDepth 阵列，没有 Face ID，没有红外，没有 LiDAR。</li>
    </ul>
    <p>没有 Face ID 是被问得最多、也最令人失望的答案。Apple 有这套硬件，只是选择不在 Mac 上提供——大概因为键盘上的触控 ID 已覆盖大多数身份验证需求。</p>
    <h2>macOS 拿刘海做什么？</h2>
    <p>几乎没有。总共三件事：</p>
    <ul>
      <li>摄像头启用时，在刘海右缘亮起一个绿点。</li>
      <li>把菜单栏绕它排布。会落在刘海下方的图标会被隐藏，直到你点进菜单栏。</li>
      <li>在全屏视频时为其加边。macOS 可选地为全屏内容顶部加黑边，以免被刘海裁切。</li>
    </ul>
    <p>没有组件界面。没有点按目标。没有拖拽目标。没有悬停行为。就系统而言，刘海是一个礼貌的洞。</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>90 秒给你的刘海派个活</h3>
        <p>NotchNest 为空刘海加入日历、AI 剪贴板、笔记、番茄钟、音乐和 AirDrop。免费。</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>
    <h2>Apple 为何不在刘海里放界面？</h2>
    <p>几个可能的原因：</p>
    <ul>
      <li><strong>光标。</strong>iPhone 的灵动岛好用是因为手指能触摸它。在 Mac 上你得把光标移到刘海——而 macOS 已有控制中心承担此事。</li>
      <li><strong>可发现性。</strong>一个没有屏上提示的新交互区很难教会用户。大多数人永远不会发现它。</li>
      <li><strong>多显示器。</strong>刘海只存在于笔记本内建屏幕上。只在一块屏幕上生效的界面会不一致。</li>
    </ul>
    <p>这些是不是好理由，取决于你多在意这块浪费的空间。第三方开发者显然不认同——参见最佳 macOS 刘海应用——并构建了 Apple 不做的交互层。</p>
    <h2>刘海能变得有用吗？</h2>
    <p>能，装一个即可。NotchNest 之类的应用加入悬停触发面板：把光标移到刘海，它便展开为玻璃质感的组件面板。这是个小小的 UX 妙招，解决了可发现性问题（你终会学会悬停手势），并利用了原本闲置的空间。</p>
    <p>你能往里放什么：</p>
    <ul>
      <li>今日日历，含 AI 生成的会议摘要</li>
      <li>AI 剪贴板历史，含改写与总结</li>
      <li>快速笔记（含 AI 润色，同步到 iCloud）</li>
      <li>番茄钟，含休息循环</li>
      <li>Spotify 或 Apple Music 的“正在播放”</li>
      <li>拖拽 AirDrop 与文件托盘，处理进行中的文件</li>
      <li>摄像头镜像，一键预览摄像头</li>
      <li>书签架，一键打开网站</li>
    </ul>
    <h2>有什么代价？</h2>
    <p>说实话，几乎没有。刘海应用住在菜单栏，空闲时休眠，占用个位数 MB 内存。没有可测的电池影响。代价是你得记住刘海是可交互的——一旦记住，你就会不断用它。</p>
    <h2>结论</h2>
    <p>开箱即用时，Mac 刘海除了容纳摄像头什么都不做。这是实话。但硬件在那儿、屏幕空间在那儿，一次免费下载就能解决问题。如果过去几年你一直忽视刘海，值得花十分钟。</p>""",
           "related": _related("zh", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "英文——2026 盘点。"))},
    "ar": {"title": "هل يفعل نتش الماك أي شيء فعلًا؟ — NotchNest",
           "description": "الجواب الصريح عمّا إذا كان نتش الماك بوك يفعل شيئًا افتراضيًا، وما وضعته Apple خلفه، وكيف تجعله تطبيقات الطرف الثالث مفيدًا.",
           "og_title": "هل يفعل نتش الماك أي شيء فعلًا؟", "og_desc": "ماذا يفعل النتش افتراضيًا وكيف تمنحه مهمة.",
           "jsonld_headline": "هل يفعل نتش الماك أي شيء فعلًا؟", "jsonld_desc": "ماذا يفعل نتش الماك بوك افتراضيًا، وما بداخله، وكيف تجعله التطبيقات مفيدًا.",
           "kicker": KICK["explainer"]["ar"], "h1": "هل يفعل نتش الماك أي شيء فعلًا؟",
           "lede": "تقدّم Apple النتش كمساحة زخرفية. إليك الجواب الصريح عمّا يفعله جاهزًا، وما بداخله، وكيف تمنحه مهمة حقيقية.",
           "readtime": READ5["ar"], "crumb_this": "هل يفعل النتش شيئًا؟",
           "faq": [("هل يملك نتش الماك Face ID؟", "لا. يحتوي النتش على كاميرا FaceTime بدقة 1080p ومستشعر ضوء محيط فقط — لا مصفوفة TrueDepth ولا Face ID. يغطّي Touch ID في لوحة المفاتيح المصادقة."),
                   ("هل يفعل النتش شيئًا افتراضيًا؟", "بالكاد. يُظهر macOS نقطة خضراء عند تشغيل الكاميرا، وينقل أيقونات شريط القوائم حوله، ويمكنه إضافة حواف للفيديو بملء الشاشة. لا سطح أدوات."),
                   ("هل يمكنني جعل النتش مفيدًا؟", "نعم، بتثبيت واحد. تضيف تطبيقات مثل NotchNest لوحة تُفعَّل بالتمرير تضم التقويم والحافظة بالذكاء الاصطناعي والملاحظات وبومودورو والموسيقى وAirDrop.")],
           "body": """<p>الجواب المختصر: لا، لا يفعل نتش macOS أي شيء افتراضيًا. إنه فتحة تحمل كاميرا. يرسم macOS شريط القوائم حوله ويترك الباقي مساحة سوداء.</p>
    <p>هذا جواب غريب في 2026، إذ ظلّ الآيفون ثلاث سنوات يحوّل فتحة الكاميرا إلى أنفع عنصر واجهة في الهاتف (Dynamic Island). فلنفكّك ما بداخله فعلًا، وما يمكنه فعله، وما يمكنك أنت فعله.</p>
    <h2>ماذا داخل النتش؟</h2>
    <ul>
      <li><strong>كاميرا FaceTime HD بدقة 1080p.</strong> سبب وجود النتش. مستشعر أكبر من كاميرا 720p السابقة — أفضل في الإضاءة المنخفضة وأوضح.</li>
      <li><strong>مستشعر الضوء المحيط.</strong> يضبط True Tone وسطوع الشاشة.</li>
      <li><strong>هذا كل شيء.</strong> لا مصفوفة TrueDepth ولا Face ID ولا أشعة تحت حمراء ولا LiDAR.</li>
    </ul>
    <p>غياب Face ID هو أكثر سؤال يُطرح وأكثر جواب يخيّب. تملك Apple العتاد، لكنها امتنعت عن تقديمه في الماك — غالبًا لأن Touch ID في لوحة المفاتيح يغطّي معظم احتياجات المصادقة.</p>
    <h2>ماذا يفعل macOS بالنتش؟</h2>
    <p>لا شيء تقريبًا. ثلاثة أشياء إجمالًا:</p>
    <ul>
      <li>يُضيء نقطة خضراء على الحافة اليمنى للنتش عند تشغيل الكاميرا.</li>
      <li>يوجّه شريط القوائم حوله. تُخفى الأيقونات التي ستقع تحته حتى تنقر داخل شريط القوائم.</li>
      <li>يضيف حوافًا في الفيديو بملء الشاشة. يمكن لـ macOS اختياريًا إضافة حاشية سوداء أعلى المحتوى لئلّا يقصّه النتش.</li>
    </ul>
    <p>لا سطح أدوات. لا هدف نقر. لا هدف سحب. لا سلوك تمرير. النتش، لأغراض النظام، ثقب مهذّب.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>امنح نتشك مهمة في 90 ثانية</h3>
        <p>يضيف NotchNest إلى النتش الفارغ التقويم والحافظة بالذكاء الاصطناعي والملاحظات وبومودورو والموسيقى وAirDrop. مجانًا.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>
    <h2>لماذا لم تضع Apple واجهة في النتش؟</h2>
    <p>بضعة أسباب محتملة:</p>
    <ul>
      <li><strong>المؤشر.</strong> يعمل Dynamic Island في الآيفون لأن إصبعك يلمسه. في الماك ستحتاج لتحريك المؤشر إلى النتش — ولدى macOS مركز تحكّم لذلك أصلًا.</li>
      <li><strong>سهولة الاكتشاف.</strong> منطقة تفاعلية جديدة بلا أي إشارة على الشاشة يصعب تعليمها. لن يجدها معظم المستخدمين أبدًا.</li>
      <li><strong>الشاشات المتعددة.</strong> يوجد النتش فقط على شاشة اللابتوب المدمجة. واجهة تعمل على شاشة واحدة فقط ستكون غير متسقة.</li>
    </ul>
    <p>كون هذه أسبابًا وجيهة يعتمد على مقدار تقديرك للمساحة المهدرة. يخالف مطوّرو الطرف الثالث بوضوح — راجع أفضل تطبيقات نتش macOS — وقد بنوا الطبقة التفاعلية التي لن تقدّمها Apple.</p>
    <h2>هل يمكن أن يكون النتش مفيدًا؟</h2>
    <p>نعم، بتثبيت واحد. تضيف تطبيقات مثل NotchNest لوحة تُفعَّل بالتمرير: حرّك المؤشر إلى النتش فينفتح إلى سطح زجاجي للأدوات. حيلة تجربة استخدام صغيرة تحلّ مشكلة الاكتشاف (تتعلّم إيماءة التمرير مع الوقت) وتستغلّ مساحة كانت فارغة.</p>
    <p>ما يمكنك وضعه هناك:</p>
    <ul>
      <li>تقويم اليوم مع ملخصات اجتماعات مولّدة بالذكاء الاصطناعي</li>
      <li>سجل حافظة بالذكاء الاصطناعي مع إعادة صياغة وتلخيص</li>
      <li>ملاحظات سريعة (مع تحسين بالذكاء الاصطناعي، ومزامنة iCloud)</li>
      <li>مؤقت بومودورو مع دورات استراحة</li>
      <li>«قيد التشغيل» لـ Spotify أو Apple Music</li>
      <li>السحب إلى AirDrop ودرج الملفات للملفات قيد العمل</li>
      <li>مرآة الكاميرا لمعاينة بلمسة واحدة</li>
      <li>رف إشارات مرجعية لفتح المواقع بنقرة</li>
    </ul>
    <h2>ما المقابل؟</h2>
    <p>بصراحة، قليل جدًا. تعيش تطبيقات النتش في شريط القوائم، وتنام عند الخمول، وتستخدم بضعة ميغابايت من الذاكرة. لا تأثير ملموس على البطارية. المقابل أن تتذكّر أن النتش تفاعلي — وحين تفعل، تبدأ باستخدامه باستمرار.</p>
    <h2>الخلاصة</h2>
    <p>جاهزًا من العلبة، لا يفعل نتش الماك شيئًا سوى حمل كاميرا. هذا الجواب الصادق. لكن العتاد موجود، ومساحة الشاشة موجودة، وتنزيل مجاني واحد يحلّ المشكلة. إن كنت تتجاهل نتشك السنوات الأخيرة، فهو يستحق عشر دقائق من وقتك.</p>""",
           "related": _related("ar", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "إنجليزي — اختيارات 2026."))},
    "fr": {"title": "L'encoche du Mac sert-elle vraiment à quelque chose ? — NotchNest",
           "description": "La réponse franche : l'encoche du MacBook fait-elle quelque chose par défaut, qu'y a-t-il derrière, et comment les apps tierces la rendent utile.",
           "og_title": "L'encoche du Mac sert-elle à quelque chose ?", "og_desc": "Ce que fait l'encoche par défaut et comment lui donner un rôle.",
           "jsonld_headline": "L'encoche du Mac sert-elle vraiment à quelque chose ?", "jsonld_desc": "Ce que fait l'encoche du MacBook par défaut, ce qu'elle contient et comment les apps la rendent utile.",
           "kicker": KICK["explainer"]["fr"], "h1": "L'encoche du Mac sert-elle vraiment à quelque chose ?",
           "lede": "Apple livre l'encoche comme espace décoratif. Voici la réponse honnête sur ce qu'elle fait d'origine, ce qu'elle contient, et comment lui donner un vrai rôle.",
           "readtime": READ5["fr"], "crumb_this": "L'encoche sert-elle à quelque chose ?",
           "faq": [("L'encoche du Mac a-t-elle Face ID ?", "Non. L'encoche ne contient que la caméra FaceTime 1080p et un capteur de luminosité — pas de bloc TrueDepth, pas de Face ID. Touch ID sur le clavier couvre l'authentification."),
                   ("L'encoche fait-elle quelque chose par défaut ?", "À peine. macOS affiche un point vert quand la caméra est active, déplace les icônes de la barre des menus autour, et peut rembourrer la vidéo plein écran. Aucune surface de widgets."),
                   ("Puis-je rendre l'encoche utile ?", "Oui, avec une installation. Des apps comme NotchNest ajoutent un panneau activé au survol avec calendrier, presse-papiers IA, notes, Pomodoro, musique et AirDrop.")],
           "body": """<p>La réponse courte : non, l'encoche macOS ne fait rien par défaut. C'est une découpe qui loge une caméra. macOS dessine la barre des menus autour d'elle et laisse le reste en espace noir.</p>
    <p>C'est une réponse étrange en 2026, alors que l'iPhone transforme depuis trois ans la découpe de la caméra en l'élément d'interface le plus utile du téléphone (Dynamic Island). Décomposons donc ce qu'il y a vraiment dedans, ce qu'elle pourrait faire, et ce que vous pouvez y faire.</p>
    <h2>Qu'y a-t-il dans l'encoche ?</h2>
    <ul>
      <li><strong>Caméra FaceTime HD 1080p.</strong> La raison d'être de l'encoche. Capteur plus grand que la caméra 720p précédente — meilleur en basse lumière, plus net.</li>
      <li><strong>Capteur de luminosité ambiante.</strong> Ajuste True Tone et la luminosité de l'écran.</li>
      <li><strong>C'est tout.</strong> Pas de bloc TrueDepth, pas de Face ID, pas d'infrarouge, pas de LiDAR.</li>
    </ul>
    <p>L'absence de Face ID est la question la plus posée et la réponse la plus décevante. Apple a le matériel. Ils ont juste choisi de ne pas le proposer sur Mac — sans doute parce que Touch ID sur le clavier couvre déjà l'essentiel de l'authentification.</p>
    <h2>Que fait macOS de l'encoche ?</h2>
    <p>Presque rien. Trois choses en tout :</p>
    <ul>
      <li>Un point vert s'allume au bord droit de l'encoche quand la caméra est active.</li>
      <li>Il fait passer la barre des menus autour. Les icônes qui atterriraient dessous sont masquées jusqu'à ce que vous cliquiez dans la barre des menus.</li>
      <li>Il la rembourre en vidéo plein écran. macOS peut, en option, ajouter des bandes en haut du contenu plein écran pour qu'il ne soit pas coupé par l'encoche.</li>
    </ul>
    <p>Pas de surface de widgets. Pas de cible de tap. Pas de cible de glisser. Pas de comportement au survol. Pour le système, l'encoche est un trou poli.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Donnez un rôle à votre encoche en 90 secondes</h3>
        <p>NotchNest ajoute à l'encoche vide calendrier, presse-papiers IA, notes, Pomodoro, musique et AirDrop. Gratuit.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>
    <h2>Pourquoi Apple n'a-t-il pas mis d'interface dans l'encoche ?</h2>
    <p>Quelques raisons probables :</p>
    <ul>
      <li><strong>Le curseur.</strong> Le Dynamic Island de l'iPhone marche parce que votre doigt le touche. Sur Mac, il faudrait amener le curseur à l'encoche — et macOS a déjà un Centre de contrôle pour ça.</li>
      <li><strong>La découvrabilité.</strong> Une nouvelle zone interactive sans repère à l'écran est difficile à enseigner. La plupart ne la trouveraient jamais.</li>
      <li><strong>Plusieurs écrans.</strong> L'encoche n'existe que sur l'écran intégré du portable. Une interface ne marchant que sur un écran serait incohérente.</li>
    </ul>
    <p>Que ce soient de bonnes raisons dépend de la valeur que vous accordez à l'espace gâché. Les développeurs tiers sont clairement d'un autre avis — voyez les meilleures apps d'encoche macOS — et ont bâti la couche interactive qu'Apple refuse.</p>
    <h2>L'encoche peut-elle être utile ?</h2>
    <p>Oui, avec une installation. Des apps comme NotchNest ajoutent un panneau activé au survol : amenez le curseur à l'encoche et elle se déploie en une surface de widgets en verre. Une petite astuce d'UX qui règle le problème de découvrabilité (vous finissez par apprendre le geste de survol) et utilise un espace qui restait vide.</p>
    <p>Ce que vous pouvez y mettre :</p>
    <ul>
      <li>Le calendrier du jour avec des briefings de réunion générés par IA</li>
      <li>L'historique du presse-papiers IA avec reformulation et résumé</li>
      <li>Des notes rapides (avec affinage IA, sync iCloud)</li>
      <li>Un minuteur Pomodoro avec cycles de pause</li>
      <li>Now Playing pour Spotify ou Apple Music</li>
      <li>Glisser-vers-AirDrop et bac à fichiers pour les fichiers en cours</li>
      <li>Un miroir caméra pour un aperçu webcam en un tap</li>
      <li>Une étagère de favoris pour lancer des sites en un clic</li>
    </ul>
    <h2>Le hic ?</h2>
    <p>Honnêtement, très peu. Les apps d'encoche vivent dans la barre des menus, se mettent en veille au repos et utilisent quelques Mo de RAM. Aucun impact mesurable sur la batterie. Le hic, c'est qu'il faut se souvenir que l'encoche est interactive — une fois que c'est le cas, vous l'utilisez constamment.</p>
    <h2>Le verdict</h2>
    <p>D'origine, l'encoche du Mac ne fait rien de plus que loger une caméra. C'est la réponse honnête. Mais le matériel est là, l'espace écran est là, et un téléchargement gratuit règle le problème. Si vous ignorez votre encoche depuis quelques années, elle vaut dix minutes de votre temps.</p>""",
           "related": _related("fr", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Anglais — sélection 2026."))},
    "pt-BR": {"title": "O notch do Mac faz alguma coisa? — NotchNest",
              "description": "A resposta direta: o notch do MacBook faz algo por padrão, o que a Apple pôs atrás dele e como os apps de terceiros o tornam útil.",
              "og_title": "O notch do Mac faz alguma coisa?", "og_desc": "O que o notch faz por padrão e como dar um papel a ele.",
              "jsonld_headline": "O notch do Mac faz alguma coisa?", "jsonld_desc": "O que o notch do MacBook faz por padrão, o que há dentro e como os apps o tornam útil.",
              "kicker": KICK["explainer"]["pt-BR"], "h1": "O notch do Mac faz alguma coisa?",
              "lede": "A Apple entrega o notch como espaço decorativo. Aqui está a resposta honesta sobre o que ele faz de fábrica, o que há dentro e como dar a ele um papel de verdade.",
              "readtime": READ5["pt-BR"], "crumb_this": "O notch faz algo?",
              "faq": [("O notch do Mac tem Face ID?", "Não. O notch contém só a câmera FaceTime de 1080p e um sensor de luz ambiente — sem conjunto TrueDepth, sem Face ID. O Touch ID no teclado cobre a autenticação."),
                      ("O notch faz algo por padrão?", "Quase nada. O macOS mostra um ponto verde com a câmera ativa, desloca os ícones da barra de menus ao redor e pode adicionar bordas ao vídeo em tela cheia. Nenhuma superfície de widgets."),
                      ("Posso tornar o notch útil?", "Sim, com uma instalação. Apps como o NotchNest adicionam um painel ativado ao passar o cursor com calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop.")],
              "body": """<p>A resposta curta: não, o notch do macOS não faz nada por padrão. É um recorte que abriga uma câmera. O macOS desenha a barra de menus ao redor dele e deixa o resto como espaço preto.</p>
    <p>É uma resposta estranha em 2026, já que o iPhone há três anos transforma o recorte da câmera no elemento de interface mais útil do telefone (Dynamic Island). Então vamos destrinchar o que há de fato lá dentro, o que ele poderia fazer e o que você pode fazer.</p>
    <h2>O que há dentro do notch?</h2>
    <ul>
      <li><strong>Câmera FaceTime HD de 1080p.</strong> O motivo de o notch existir. Sensor maior que a câmera 720p anterior — melhor com pouca luz, mais nítido.</li>
      <li><strong>Sensor de luz ambiente.</strong> Ajusta o True Tone e o brilho da tela.</li>
      <li><strong>É só isso.</strong> Sem conjunto TrueDepth, sem Face ID, sem infravermelho, sem LiDAR.</li>
    </ul>
    <p>A falta de Face ID é a pergunta mais feita e a resposta mais decepcionante. A Apple tem o hardware. Ela só optou por não trazê-lo ao Mac — provavelmente porque o Touch ID no teclado já cobre a maior parte das necessidades de autenticação.</p>
    <h2>O que o macOS faz com o notch?</h2>
    <p>Quase nada. Três coisas, no total:</p>
    <ul>
      <li>Acende um ponto verde na borda direita do notch quando a câmera está ativa.</li>
      <li>Desvia a barra de menus ao redor dele. Ícones que ficariam embaixo são ocultados até você clicar na barra de menus.</li>
      <li>Adiciona bordas no vídeo em tela cheia. O macOS pode, opcionalmente, colocar tarjas no topo do conteúdo em tela cheia para não ser cortado pelo notch.</li>
    </ul>
    <p>Não há superfície de widgets. Nenhum alvo de toque. Nenhum alvo de arraste. Nenhum comportamento ao passar o cursor. Para o sistema, o notch é um buraco educado.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Dê um papel ao seu notch em 90 segundos</h3>
        <p>O NotchNest adiciona ao notch vazio calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop. Grátis.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>
    <h2>Por que a Apple não pôs interface no notch?</h2>
    <p>Alguns motivos prováveis:</p>
    <ul>
      <li><strong>O cursor.</strong> O Dynamic Island do iPhone funciona porque o seu dedo o toca. No Mac, você precisaria levar o cursor até o notch — e o macOS já tem uma Central de Controle para isso.</li>
      <li><strong>Descoberta.</strong> Uma nova zona interativa sem indicação na tela é difícil de ensinar. A maioria nunca a encontraria.</li>
      <li><strong>Vários monitores.</strong> O notch só existe na tela embutida do laptop. Uma interface que só funcionasse em uma tela seria inconsistente.</li>
    </ul>
    <p>Se esses são bons motivos depende de quanto você valoriza o espaço desperdiçado. Os desenvolvedores de terceiros claramente discordam — veja os melhores apps de notch macOS — e construíram a camada interativa que a Apple não faz.</p>
    <h2>O notch pode ser útil?</h2>
    <p>Sim, com uma instalação. Apps como o NotchNest adicionam um painel ativado ao passar o cursor: leve o cursor ao notch e ele se expande em uma superfície de widgets de vidro. Um pequeno truque de UX que resolve o problema de descoberta (você acaba aprendendo o gesto de passar o cursor) e usa um espaço que estava vazio.</p>
    <p>O que você pode colocar lá:</p>
    <ul>
      <li>O calendário de hoje com briefings de reunião gerados por IA</li>
      <li>Histórico da área de transferência com IA, com reformular e resumir</li>
      <li>Notas rápidas (com refinamento por IA, sincronia com iCloud)</li>
      <li>Timer Pomodoro com ciclos de pausa</li>
      <li>Now Playing para Spotify ou Apple Music</li>
      <li>Arrastar para AirDrop e bandeja de arquivos para arquivos em andamento</li>
      <li>Espelho da câmera para prévia da webcam com um toque</li>
      <li>Prateleira de favoritos para abrir sites com um clique</li>
    </ul>
    <h2>Qual é a pegadinha?</h2>
    <p>Sinceramente, muito pouca. Apps de notch vivem na barra de menus, dormem quando ociosos e usam poucos MB de RAM. Não há impacto perceptível na bateria. A pegadinha é que você precisa lembrar que o notch é interativo — e, quando lembra, passa a usá-lo o tempo todo.</p>
    <h2>O veredito</h2>
    <p>De fábrica, o notch do Mac não faz nada além de abrigar uma câmera. Essa é a resposta honesta. Mas o hardware está lá, o espaço de tela está lá, e um download grátis resolve o problema. Se você vem ignorando o seu notch nos últimos anos, ele vale dez minutos do seu tempo.</p>""",
              "related": _related("pt-BR", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "pt-PT": {"title": "O notch do Mac faz alguma coisa? — NotchNest",
              "description": "A resposta direta: o notch do MacBook faz algo por predefinição, o que a Apple pôs atrás dele e como as apps de terceiros o tornam útil.",
              "og_title": "O notch do Mac faz alguma coisa?", "og_desc": "O que o notch faz por predefinição e como dar-lhe um papel.",
              "jsonld_headline": "O notch do Mac faz alguma coisa?", "jsonld_desc": "O que o notch do MacBook faz por predefinição, o que há dentro e como as apps o tornam útil.",
              "kicker": KICK["explainer"]["pt-PT"], "h1": "O notch do Mac faz alguma coisa?",
              "lede": "A Apple entrega o notch como espaço decorativo. Aqui está a resposta honesta sobre o que ele faz de origem, o que há dentro e como dar-lhe um papel a sério.",
              "readtime": READ5["pt-PT"], "crumb_this": "O notch faz algo?",
              "faq": [("O notch do Mac tem Face ID?", "Não. O notch contém apenas a câmara FaceTime de 1080p e um sensor de luz ambiente — sem conjunto TrueDepth, sem Face ID. O Touch ID no teclado cobre a autenticação."),
                      ("O notch faz algo por predefinição?", "Quase nada. O macOS mostra um ponto verde com a câmara ativa, desloca os ícones da barra de menus à volta e pode adicionar barras ao vídeo em ecrã inteiro. Nenhuma superfície de widgets."),
                      ("Posso tornar o notch útil?", "Sim, com uma instalação. Apps como o NotchNest adicionam um painel ativado ao passar o cursor com calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop.")],
              "body": """<p>A resposta curta: não, o notch do macOS não faz nada por predefinição. É um recorte que aloja uma câmara. O macOS desenha a barra de menus à volta dele e deixa o resto como espaço preto.</p>
    <p>É uma resposta estranha em 2026, já que o iPhone há três anos transforma o recorte da câmara no elemento de interface mais útil do telefone (Dynamic Island). Vamos então destrinçar o que há de facto lá dentro, o que poderia fazer e o que pode fazer.</p>
    <h2>O que há dentro do notch?</h2>
    <ul>
      <li><strong>Câmara FaceTime HD de 1080p.</strong> A razão de o notch existir. Sensor maior do que a câmara 720p anterior — melhor com pouca luz, mais nítido.</li>
      <li><strong>Sensor de luz ambiente.</strong> Ajusta o True Tone e o brilho do ecrã.</li>
      <li><strong>É só isto.</strong> Sem conjunto TrueDepth, sem Face ID, sem infravermelhos, sem LiDAR.</li>
    </ul>
    <p>A falta de Face ID é a pergunta mais feita e a resposta mais dececionante. A Apple tem o hardware. Apenas optou por não o trazer ao Mac — provavelmente porque o Touch ID no teclado já cobre a maior parte das necessidades de autenticação.</p>
    <h2>O que o macOS faz com o notch?</h2>
    <p>Quase nada. Três coisas, no total:</p>
    <ul>
      <li>Acende um ponto verde na margem direita do notch quando a câmara está ativa.</li>
      <li>Desvia a barra de menus à volta dele. Ícones que ficariam por baixo são ocultados até clicar na barra de menus.</li>
      <li>Adiciona barras no vídeo em ecrã inteiro. O macOS pode, opcionalmente, colocar tarjas no topo do conteúdo em ecrã inteiro para não ser cortado pelo notch.</li>
    </ul>
    <p>Não há superfície de widgets. Nenhum alvo de toque. Nenhum alvo de arrasto. Nenhum comportamento ao passar o cursor. Para o sistema, o notch é um buraco educado.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Dê um papel ao seu notch em 90 segundos</h3>
        <p>O NotchNest adiciona ao notch vazio calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop. Gratuito.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>
    <h2>Porque não pôs a Apple interface no notch?</h2>
    <p>Algumas razões prováveis:</p>
    <ul>
      <li><strong>O cursor.</strong> O Dynamic Island do iPhone funciona porque o seu dedo lhe toca. No Mac, teria de levar o cursor até ao notch — e o macOS já tem um Centro de Controlo para isso.</li>
      <li><strong>Descoberta.</strong> Uma nova zona interativa sem indicação no ecrã é difícil de ensinar. A maioria nunca a encontraria.</li>
      <li><strong>Vários ecrãs.</strong> O notch só existe no ecrã integrado do portátil. Uma interface que só funcionasse num ecrã seria inconsistente.</li>
    </ul>
    <p>Se são boas razões depende de quanto valoriza o espaço desperdiçado. Os programadores de terceiros discordam claramente — veja as melhores apps de notch macOS — e construíram a camada interativa que a Apple não faz.</p>
    <h2>O notch pode ser útil?</h2>
    <p>Sim, com uma instalação. Apps como o NotchNest adicionam um painel ativado ao passar o cursor: leve o cursor ao notch e ele expande-se numa superfície de widgets de vidro. Um pequeno truque de UX que resolve o problema de descoberta (acaba por aprender o gesto de passar o cursor) e usa um espaço que estava vazio.</p>
    <p>O que pode pôr lá:</p>
    <ul>
      <li>O calendário de hoje com briefings de reunião gerados por IA</li>
      <li>Histórico da área de transferência com IA, com reformular e resumir</li>
      <li>Notas rápidas (com aperfeiçoamento por IA, sincronização com iCloud)</li>
      <li>Temporizador Pomodoro com ciclos de pausa</li>
      <li>Now Playing para Spotify ou Apple Music</li>
      <li>Arrastar para AirDrop e tabuleiro de ficheiros para ficheiros em curso</li>
      <li>Espelho da câmara para pré-visualização com um toque</li>
      <li>Prateleira de favoritos para abrir sites com um clique</li>
    </ul>
    <h2>Qual é o senão?</h2>
    <p>Honestamente, muito pouco. As apps de notch vivem na barra de menus, adormecem quando inativas e usam poucos MB de RAM. Não há impacto percetível na bateria. O senão é que tem de se lembrar de que o notch é interativo — e, quando se lembra, passa a usá-lo a toda a hora.</p>
    <h2>O veredito</h2>
    <p>De origem, o notch do Mac não faz nada além de alojar uma câmara. Essa é a resposta honesta. Mas o hardware está lá, o espaço de ecrã está lá, e uma transferência gratuita resolve o problema. Se anda a ignorar o seu notch nos últimos anos, ele vale dez minutos do seu tempo.</p>""",
              "related": _related("pt-PT", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "es-MX": {"title": "¿El notch del Mac hace algo? — NotchNest",
              "description": "La respuesta directa: ¿el notch del MacBook hace algo por defecto?, qué puso Apple detrás y cómo las apps de terceros lo hacen útil.",
              "og_title": "¿El notch del Mac hace algo?", "og_desc": "Qué hace el notch por defecto y cómo darle un papel.",
              "jsonld_headline": "¿El notch del Mac hace algo?", "jsonld_desc": "Qué hace el notch del MacBook por defecto, qué hay dentro y cómo las apps lo hacen útil.",
              "kicker": KICK["explainer"]["es-MX"], "h1": "¿El notch del Mac hace algo?",
              "lede": "Apple entrega el notch como espacio decorativo. Aquí está la respuesta honesta sobre qué hace de fábrica, qué hay dentro y cómo darle un papel de verdad.",
              "readtime": READ5["es-MX"], "crumb_this": "¿El notch hace algo?",
              "faq": [("¿El notch del Mac tiene Face ID?", "No. El notch solo contiene la cámara FaceTime de 1080p y un sensor de luz ambiental — sin conjunto TrueDepth, sin Face ID. El Touch ID del teclado cubre la autenticación."),
                      ("¿El notch hace algo por defecto?", "Casi nada. macOS muestra un punto verde con la cámara activa, reacomoda los iconos de la barra de menús a su alrededor y puede añadir barras al video en pantalla completa. Ninguna superficie de widgets."),
                      ("¿Puedo hacer útil el notch?", "Sí, con una instalación. Apps como NotchNest añaden un panel activado al pasar el cursor con calendario, portapapeles con IA, notas, Pomodoro, música y AirDrop.")],
              "body": """<p>La respuesta corta: no, el notch de macOS no hace nada por defecto. Es un recorte que aloja una cámara. macOS dibuja la barra de menús a su alrededor y deja el resto como espacio negro.</p>
    <p>Es una respuesta rara en 2026, dado que el iPhone lleva tres años convirtiendo el recorte de la cámara en el elemento de interfaz más útil del teléfono (Dynamic Island). Así que desglosemos qué hay de verdad ahí dentro, qué podría hacer y qué puedes hacer tú.</p>
    <h2>¿Qué hay dentro del notch?</h2>
    <ul>
      <li><strong>Cámara FaceTime HD de 1080p.</strong> La razón de que exista el notch. Sensor más grande que la cámara 720p anterior — mejor con poca luz, más nítido.</li>
      <li><strong>Sensor de luz ambiental.</strong> Ajusta True Tone y el brillo de la pantalla.</li>
      <li><strong>Eso es todo.</strong> Sin conjunto TrueDepth, sin Face ID, sin infrarrojos, sin LiDAR.</li>
    </ul>
    <p>La falta de Face ID es la pregunta más frecuente y la respuesta más decepcionante. Apple tiene el hardware. Solo optó por no traerlo al Mac — probablemente porque el Touch ID del teclado ya cubre la mayoría de las necesidades de autenticación.</p>
    <h2>¿Qué hace macOS con el notch?</h2>
    <p>Casi nada. Tres cosas, en total:</p>
    <ul>
      <li>Enciende un punto verde en el borde derecho del notch cuando la cámara está activa.</li>
      <li>Desvía la barra de menús a su alrededor. Los iconos que quedarían debajo se ocultan hasta que haces clic en la barra de menús.</li>
      <li>Lo rellena en video de pantalla completa. macOS puede, de forma opcional, poner barras en la parte superior del contenido para que no lo corte el notch.</li>
    </ul>
    <p>No hay superficie de widgets. Ningún objetivo de toque. Ningún objetivo de arrastre. Ningún comportamiento al pasar el cursor. Para el sistema, el notch es un hueco educado.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Dale un papel a tu notch en 90 segundos</h3>
        <p>NotchNest añade al notch vacío calendario, portapapeles con IA, notas, Pomodoro, música y AirDrop. Gratis.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>
    <h2>¿Por qué Apple no puso interfaz en el notch?</h2>
    <p>Algunas razones probables:</p>
    <ul>
      <li><strong>El cursor.</strong> El Dynamic Island del iPhone funciona porque tu dedo lo toca. En el Mac tendrías que llevar el cursor al notch — y macOS ya tiene un Centro de Control para eso.</li>
      <li><strong>Descubribilidad.</strong> Una nueva zona interactiva sin señal en pantalla es difícil de enseñar. La mayoría nunca la encontraría.</li>
      <li><strong>Varias pantallas.</strong> El notch solo existe en la pantalla integrada del portátil. Una interfaz que solo funcionara en una pantalla sería inconsistente.</li>
    </ul>
    <p>Si esas son buenas razones depende de cuánto valores el espacio desperdiciado. Los desarrolladores de terceros claramente no están de acuerdo — mira las mejores apps de notch macOS — y construyeron la capa interactiva que Apple no hace.</p>
    <h2>¿Puede el notch ser útil?</h2>
    <p>Sí, con una instalación. Apps como NotchNest añaden un panel activado al pasar el cursor: lleva el cursor al notch y se expande en una superficie de widgets de vidrio. Un pequeño truco de UX que resuelve el problema de descubribilidad (con el tiempo aprendes el gesto) y aprovecha un espacio que estaba vacío.</p>
    <p>Lo que puedes poner ahí:</p>
    <ul>
      <li>El calendario de hoy con briefings de reuniones generados por IA</li>
      <li>Historial del portapapeles con IA, con reformular y resumir</li>
      <li>Notas rápidas (con refinamiento por IA, sincronía con iCloud)</li>
      <li>Temporizador Pomodoro con ciclos de descanso</li>
      <li>Now Playing para Spotify o Apple Music</li>
      <li>Arrastrar a AirDrop y bandeja de archivos para archivos en curso</li>
      <li>Espejo de cámara para vista previa de la webcam con un toque</li>
      <li>Estante de favoritos para abrir sitios con un clic</li>
    </ul>
    <h2>¿Cuál es el truco?</h2>
    <p>Honestamente, muy poco. Las apps de notch viven en la barra de menús, duermen al estar inactivas y usan unos pocos MB de RAM. No hay impacto medible en la batería. El truco es que tienes que recordar que el notch es interactivo — y, una vez que lo haces, empiezas a usarlo constantemente.</p>
    <h2>El veredicto</h2>
    <p>De fábrica, el notch del Mac no hace nada más que alojar una cámara. Esa es la respuesta honesta. Pero el hardware está ahí, el espacio de pantalla está ahí, y una descarga gratis resuelve el problema. Si has estado ignorando tu notch los últimos años, vale diez minutos de tu tiempo.</p>""",
              "related": _related("es-MX", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglés — selección 2026."))},
}


# ── notch-nest-vs-boring-notch-vs-notchdrop (3-way, has a table) ─────────────
BV_TH = {"de": "Funktion", "zh": "功能", "ar": "الميزة", "fr": "Fonctionnalité", "pt-BR": "Recurso", "pt-PT": "Funcionalidade", "es-MX": "Función"}
BV_FEAT = {
    "de": ["Vertrieb", "Preis", "Von Apple sandboxed", "Kalender-Widget", "KI-Zwischenablage", "Schnellnotizen", "Pomodoro-Timer", "Spotify / Apple Music", "Drag-to-AirDrop / Datei-Tray", "Kamera-Spiegel", "AirPods-Akku", "Lesezeichen-Shelf", "Apple Intelligence (auf dem Gerät)", "Läuft ohne Notch", "Lokalisierung"],
    "zh": ["分发", "价格", "Apple 沙盒", "日历组件", "AI 剪贴板", "快速笔记", "番茄钟", "Spotify / Apple Music", "拖拽 AirDrop / 文件托盘", "摄像头镜像", "AirPods 电量", "书签架", "Apple Intelligence（本地）", "无刘海也可用", "本地化"],
    "ar": ["التوزيع", "السعر", "معزول من Apple", "أداة التقويم", "حافظة الذكاء الاصطناعي", "ملاحظات سريعة", "مؤقت بومودورو", "Spotify / Apple Music", "السحب إلى AirDrop / درج الملفات", "مرآة الكاميرا", "بطارية AirPods", "رف الإشارات", "Apple Intelligence (على الجهاز)", "يعمل بدون نتش", "التوطين"],
    "fr": ["Distribution", "Prix", "Bac à sable Apple", "Widget calendrier", "Presse-papiers IA", "Notes rapides", "Minuteur Pomodoro", "Spotify / Apple Music", "Glisser vers AirDrop / Bac à fichiers", "Miroir caméra", "Batterie AirPods", "Étagère de favoris", "Apple Intelligence (sur l'appareil)", "Fonctionne sans encoche", "Localisation"],
    "pt-BR": ["Distribuição", "Preço", "Sandbox da Apple", "Widget de calendário", "Área com IA", "Notas rápidas", "Timer Pomodoro", "Spotify / Apple Music", "Arrastar para AirDrop / Bandeja", "Espelho da câmera", "Bateria dos AirPods", "Prateleira de favoritos", "Apple Intelligence (no dispositivo)", "Funciona sem notch", "Localização"],
    "pt-PT": ["Distribuição", "Preço", "Sandbox da Apple", "Widget de calendário", "Área com IA", "Notas rápidas", "Temporizador Pomodoro", "Spotify / Apple Music", "Arrastar para AirDrop / Tabuleiro", "Espelho da câmara", "Bateria dos AirPods", "Prateleira de favoritos", "Apple Intelligence (no dispositivo)", "Funciona sem notch", "Localização"],
    "es-MX": ["Distribución", "Precio", "Sandbox de Apple", "Widget de calendario", "Portapapeles con IA", "Notas rápidas", "Temporizador Pomodoro", "Spotify / Apple Music", "Arrastrar a AirDrop / Bandeja", "Espejo de cámara", "Batería de AirPods", "Estante de favoritos", "Apple Intelligence (en el dispositivo)", "Funciona sin notch", "Localización"],
}
_YNP = {  # (yes, no, partial-ish base words)
    "de": ("Ja", "Nein"), "zh": ("是", "否"), "ar": ("نعم", "لا"), "fr": ("Oui", "Non"),
    "pt-BR": ("Sim", "Não"), "pt-PT": ("Sim", "Não"), "es-MX": ("Sí", "No"),
}
def _c3(loc):
    y, n = _YNP[loc]
    T = {"de": ["Mac App Store", "GitHub (direkt)", "Direkt / Setapp", "Kostenlos", "Kostenlos + Bezahlstufe", "Teilweise", f"{y} (KI-Briefings)", f"{y} (KI-Verfeinerung)", f"{y} (Spezialität)", "Über Bluetooth-Menü", f"{y} (Top-Bar)", "Eingeschränkt", "Viele Sprachen", "nur EN", "EN + einige"],
         "zh": ["Mac App Store", "GitHub（直接）", "直接 / Setapp", "免费", "免费 + 付费档", "部分", f"{y}（AI 摘要）", f"{y}（AI 润色）", f"{y}（其专长）", "经蓝牙菜单", f"{y}（顶栏）", "有限", "多语言", "仅英文", "英文 + 少量"],
         "ar": ["Mac App Store", "GitHub (مباشر)", "مباشر / Setapp", "مجانًا", "مجاني + مستوى مدفوع", "جزئي", f"{y} (ملخصات ذكية)", f"{y} (تحسين ذكي)", f"{y} (تخصصه)", "عبر قائمة البلوتوث", f"{y} (شريط علوي)", "محدود", "لغات كثيرة", "الإنجليزية فقط", "إنجليزي + قليل"],
         "fr": ["Mac App Store", "GitHub (direct)", "Direct / Setapp", "Gratuit", "Gratuit + niveau payant", "Partiel", f"{y} (briefings IA)", f"{y} (affinage IA)", f"{y} (spécialité)", "Via menu Bluetooth", f"{y} (barre haute)", "Limité", "Plusieurs langues", "EN uniquement", "EN + quelques-unes"],
         "pt-BR": ["Mac App Store", "GitHub (direto)", "Direto / Setapp", "Grátis", "Grátis + nível pago", "Parcial", f"{y} (briefings IA)", f"{y} (refino IA)", f"{y} (especialidade)", "Via menu Bluetooth", f"{y} (barra superior)", "Limitado", "Vários idiomas", "só EN", "EN + alguns"],
         "pt-PT": ["Mac App Store", "GitHub (direto)", "Direto / Setapp", "Gratuito", "Gratuito + nível pago", "Parcial", f"{y} (briefings IA)", f"{y} (aperfeiçoamento IA)", f"{y} (especialidade)", "Via menu Bluetooth", f"{y} (barra superior)", "Limitado", "Vários idiomas", "só EN", "EN + alguns"],
         "es-MX": ["Mac App Store", "GitHub (directo)", "Directo / Setapp", "Gratis", "Gratis + nivel de pago", "Parcial", f"{y} (briefings IA)", f"{y} (refinado IA)", f"{y} (especialidad)", "Vía menú Bluetooth", f"{y} (barra superior)", "Limitado", "Varios idiomas", "solo EN", "EN + algunos"]}[loc]
    mas, gh, setapp, free, freepaid, partial, ycal, yqn, yspec, bt, ytop, limited, manylang, enonly, enfew = T
    return [
        (mas, gh, setapp), (free, free, freepaid), (y, n, partial), (ycal, n, n), (y, n, n), (yqn, n, n),
        (y, n, n), (y, yspec, n), (y, n, yspec), (y, n, n), (bt, y, n), (y, n, n), (y, n, n),
        (ytop, limited, y), (manylang, enonly, enfew),
    ]
BV_META = {
    "de": {"title": "NotchNest vs. Boring Notch vs. NotchDrop (2026) — NotchNest", "description": "Direkter Vergleich der drei beliebtesten macOS-Notch-Apps 2026: NotchNest, Boring Notch und NotchDrop. Funktionen, Preis, KI, Performance.", "og_title": "NotchNest vs. Boring Notch vs. NotchDrop", "og_desc": "Die drei meistinstallierten Notch-Apps im direkten Vergleich.", "jsonld_headline": "NotchNest vs. Boring Notch vs. NotchDrop (2026)", "jsonld_desc": "Feature-Vergleich der drei meistinstallierten macOS-Notch-Apps 2026.", "h1": "NotchNest vs. Boring Notch vs. NotchDrop", "lede": "Ein Feature-Vergleich der drei meistinstallierten macOS-Notch-Apps 2026 — was jede am besten kann, wo sie sich überschneiden und welche zu deinem Workflow passt.", "crumb_this": "NotchNest vs. Boring Notch vs. NotchDrop", "readtime": READ6["de"],
           "faq": [("Welche Notch-App ist die beste?", "Für den breitesten Funktionsumfang NotchNest — zehn Widgets, sandboxed, mit On-Device-KI. Für reine Mediensteuerung Boring Notch, für reine Datei-Tray NotchDrop."), ("Kann ich alle drei zusammen nutzen?", "Technisch ja, aber sie konkurrieren um dieselbe Hover-Region und lösen ständig das falsche Panel aus. Wähl eine."), ("Welche ist sandboxed?", "Nur NotchNest (Mac App Store). Boring Notch ist ein GitHub-Direkt-Download; NotchDrop ist teilweise abgedeckt.")]},
    "zh": {"title": "NotchNest 对比 Boring Notch 对比 NotchDrop（2026）— NotchNest", "description": "2026 年三款最热门 macOS 刘海应用的直接对比：NotchNest、Boring Notch 和 NotchDrop。功能、价格、AI、性能。", "og_title": "NotchNest 对比 Boring Notch 对比 NotchDrop", "og_desc": "三款安装量最高的刘海应用直接对比。", "jsonld_headline": "NotchNest 对比 Boring Notch 对比 NotchDrop（2026）", "jsonld_desc": "2026 年三款安装量最高的 macOS 刘海应用功能对比。", "h1": "NotchNest 对比 Boring Notch 对比 NotchDrop", "lede": "2026 年三款安装量最高的 macOS 刘海应用逐项功能对比——各自最擅长什么、哪里重叠，以及哪个更契合你的工作流。", "crumb_this": "NotchNest 对比 Boring Notch 对比 NotchDrop", "readtime": READ6["zh"],
           "faq": [("哪款刘海应用最好？", "论功能最全是 NotchNest——十个组件、沙盒、本地 AI。只要媒体控制选 Boring Notch，只要文件托盘选 NotchDrop。"), ("我能同时用三款吗？", "技术上可以，但它们争夺同一悬停区域，会不断触发错误面板。选一个。"), ("哪款是沙盒的？", "只有 NotchNest（Mac App Store）。Boring Notch 是 GitHub 直接下载；NotchDrop 部分覆盖。")]},
    "ar": {"title": "NotchNest في مواجهة Boring Notch وNotchDrop (2026) — NotchNest", "description": "مقارنة مباشرة لأشهر ثلاثة تطبيقات نتش لنظام macOS في 2026: NotchNest وBoring Notch وNotchDrop. الميزات والسعر والذكاء الاصطناعي والأداء.", "og_title": "NotchNest في مواجهة Boring Notch وNotchDrop", "og_desc": "أكثر ثلاثة تطبيقات نتش تثبيتًا في مقارنة مباشرة.", "jsonld_headline": "NotchNest في مواجهة Boring Notch وNotchDrop (2026)", "jsonld_desc": "مقارنة ميزات أكثر ثلاثة تطبيقات نتش macOS تثبيتًا في 2026.", "h1": "NotchNest في مواجهة Boring Notch وNotchDrop", "lede": "مقارنة ميزة بميزة لأكثر ثلاثة تطبيقات نتش macOS تثبيتًا في 2026 — ما تجيده كل واحدة، وأين تتقاطع، وأيها يناسب سير عملك.", "crumb_this": "NotchNest في مواجهة Boring Notch وNotchDrop", "readtime": READ6["ar"],
           "faq": [("أي تطبيق نتش هو الأفضل؟", "لأوسع مجموعة ميزات: NotchNest — عشر أدوات، معزول، بذكاء اصطناعي على الجهاز. للتحكم بالوسائط فقط: Boring Notch؛ ولدرج الملفات فقط: NotchDrop."), ("هل يمكنني استخدام الثلاثة معًا؟", "تقنيًا نعم، لكنها تتنافس على منطقة التمرير نفسها وتفتح اللوحة الخطأ باستمرار. اختر واحدًا."), ("أيها معزول؟", "NotchNest فقط (Mac App Store). Boring Notch تنزيل مباشر من GitHub؛ وNotchDrop مغطّى جزئيًا.")]},
    "fr": {"title": "NotchNest vs Boring Notch vs NotchDrop (2026) — NotchNest", "description": "Comparatif direct des trois apps d'encoche macOS les plus populaires en 2026 : NotchNest, Boring Notch et NotchDrop. Fonctions, prix, IA, performances.", "og_title": "NotchNest vs Boring Notch vs NotchDrop", "og_desc": "Les trois apps d'encoche les plus installées, comparées.", "jsonld_headline": "NotchNest vs Boring Notch vs NotchDrop (2026)", "jsonld_desc": "Comparatif des fonctionnalités des trois apps d'encoche macOS les plus installées en 2026.", "h1": "NotchNest vs Boring Notch vs NotchDrop", "lede": "Un comparatif fonctionnalité par fonctionnalité des trois apps d'encoche macOS les plus installées en 2026 — ce que chacune fait de mieux, où elles se recoupent et laquelle correspond à votre workflow.", "crumb_this": "NotchNest vs Boring Notch vs NotchDrop", "readtime": READ6["fr"],
           "faq": [("Quelle app d'encoche est la meilleure ?", "Pour l'éventail le plus large : NotchNest — dix widgets, en bac à sable, avec IA sur l'appareil. Pour la seule commande média : Boring Notch ; pour le seul bac à fichiers : NotchDrop."), ("Puis-je utiliser les trois ensemble ?", "Techniquement oui, mais elles se disputent la même zone de survol et déclenchent sans cesse le mauvais panneau. Choisissez-en une."), ("Laquelle est en bac à sable ?", "NotchNest seule (Mac App Store). Boring Notch est un téléchargement direct GitHub ; NotchDrop est partiellement couvert.")]},
    "pt-BR": {"title": "NotchNest vs Boring Notch vs NotchDrop (2026) — NotchNest", "description": "Comparativo direto dos três apps de notch macOS mais populares em 2026: NotchNest, Boring Notch e NotchDrop. Recursos, preço, IA, desempenho.", "og_title": "NotchNest vs Boring Notch vs NotchDrop", "og_desc": "Os três apps de notch mais instalados, comparados.", "jsonld_headline": "NotchNest vs Boring Notch vs NotchDrop (2026)", "jsonld_desc": "Comparativo de recursos dos três apps de notch macOS mais instalados em 2026.", "h1": "NotchNest vs Boring Notch vs NotchDrop", "lede": "Um comparativo recurso a recurso dos três apps de notch macOS mais instalados em 2026 — o que cada um faz de melhor, onde se sobrepõem e qual combina com o seu fluxo.", "crumb_this": "NotchNest vs Boring Notch vs NotchDrop", "readtime": READ6["pt-BR"],
              "faq": [("Qual app de notch é o melhor?", "Para o conjunto mais amplo: NotchNest — dez widgets, em sandbox, com IA no dispositivo. Só para controle de mídia: Boring Notch; só para bandeja de arquivos: NotchDrop."), ("Posso usar os três juntos?", "Tecnicamente sim, mas disputam a mesma região de hover e abrem o painel errado o tempo todo. Escolha um."), ("Qual é em sandbox?", "Só o NotchNest (Mac App Store). O Boring Notch é download direto do GitHub; o NotchDrop é parcialmente coberto.")]},
    "pt-PT": {"title": "NotchNest vs Boring Notch vs NotchDrop (2026) — NotchNest", "description": "Comparação direta das três apps de notch macOS mais populares em 2026: NotchNest, Boring Notch e NotchDrop. Funcionalidades, preço, IA, desempenho.", "og_title": "NotchNest vs Boring Notch vs NotchDrop", "og_desc": "As três apps de notch mais instaladas, comparadas.", "jsonld_headline": "NotchNest vs Boring Notch vs NotchDrop (2026)", "jsonld_desc": "Comparação de funcionalidades das três apps de notch macOS mais instaladas em 2026.", "h1": "NotchNest vs Boring Notch vs NotchDrop", "lede": "Uma comparação funcionalidade a funcionalidade das três apps de notch macOS mais instaladas em 2026 — o que cada uma faz melhor, onde se sobrepõem e qual combina com o seu fluxo.", "crumb_this": "NotchNest vs Boring Notch vs NotchDrop", "readtime": READ6["pt-PT"],
              "faq": [("Qual app de notch é a melhor?", "Para o conjunto mais amplo: NotchNest — dez widgets, em sandbox, com IA no dispositivo. Só para controlo de multimédia: Boring Notch; só para tabuleiro de ficheiros: NotchDrop."), ("Posso usar as três juntas?", "Tecnicamente sim, mas disputam a mesma região de hover e abrem o painel errado a toda a hora. Escolha uma."), ("Qual é em sandbox?", "Só o NotchNest (Mac App Store). O Boring Notch é transferência direta do GitHub; o NotchDrop é parcialmente coberto.")]},
    "es-MX": {"title": "NotchNest vs Boring Notch vs NotchDrop (2026) — NotchNest", "description": "Comparativa directa de las tres apps de notch macOS más populares en 2026: NotchNest, Boring Notch y NotchDrop. Funciones, precio, IA, rendimiento.", "og_title": "NotchNest vs Boring Notch vs NotchDrop", "og_desc": "Las tres apps de notch más instaladas, comparadas.", "jsonld_headline": "NotchNest vs Boring Notch vs NotchDrop (2026)", "jsonld_desc": "Comparativa de funciones de las tres apps de notch macOS más instaladas en 2026.", "h1": "NotchNest vs Boring Notch vs NotchDrop", "lede": "Una comparativa función por función de las tres apps de notch macOS más instaladas en 2026 — qué hace mejor cada una, dónde se solapan y cuál encaja con tu flujo.", "crumb_this": "NotchNest vs Boring Notch vs NotchDrop", "readtime": READ6["es-MX"],
              "faq": [("¿Qué app de notch es la mejor?", "Para el conjunto más amplio: NotchNest — diez widgets, en sandbox, con IA en el dispositivo. Solo para control de medios: Boring Notch; solo para bandeja de archivos: NotchDrop."), ("¿Puedo usar las tres juntas?", "Técnicamente sí, pero compiten por la misma región de hover y abren el panel equivocado todo el tiempo. Elige una."), ("¿Cuál está en sandbox?", "Solo NotchNest (Mac App Store). Boring Notch es descarga directa de GitHub; NotchDrop está parcialmente cubierto.")]},
}
BV_PRE = {
    "de": """<p>Die Notch-App-Kategorie ist klein, aber deutlich. Drei Apps dominieren Mac-App-Store-Suchen und GitHub-Stars:</p>
    <ul>
      <li><strong>NotchNest</strong> — der Produktivitäts-Hub. Kalender, KI-Zwischenablage, Notizen, Pomodoro, Musik, AirDrop, Spiegel, Lesezeichen.</li>
      <li><strong>Boring Notch</strong> — der Medien-Controller und Animator. Now Playing, AirPods-Akku, dezente Dynamic-Island-artige Animationen.</li>
      <li><strong>NotchDrop</strong> — das Drag-and-Drop-Tray. Dateien auf die Notch ziehen, woanders wieder rausziehen.</li>
    </ul>
    <p>So schneiden sie ab.</p>
    <h2>Feature-Vergleich</h2>
    """,
    "zh": """<p>刘海应用类别虽小却分明。三款应用主导着 Mac App Store 搜索和 GitHub 星标：</p>
    <ul>
      <li><strong>NotchNest</strong>——生产力中枢。日历、AI 剪贴板、笔记、番茄钟、音乐、AirDrop、镜像、书签。</li>
      <li><strong>Boring Notch</strong>——媒体控制器与动画师。正在播放、AirPods 电量、含蓄的灵动岛式动画。</li>
      <li><strong>NotchDrop</strong>——拖放托盘。把文件拖到刘海，再拖到别处。</li>
    </ul>
    <p>来看看它们的表现。</p>
    <h2>功能对比</h2>
    """,
    "ar": """<p>فئة تطبيقات النتش صغيرة لكنها متمايزة. تهيمن ثلاثة تطبيقات على عمليات البحث في Mac App Store ونجوم GitHub:</p>
    <ul>
      <li><strong>NotchNest</strong> — مركز الإنتاجية. تقويم وحافظة بالذكاء الاصطناعي وملاحظات وبومودورو وموسيقى وAirDrop ومرآة وإشارات مرجعية.</li>
      <li><strong>Boring Notch</strong> — متحكّم الوسائط والرسوم. «قيد التشغيل» وبطارية AirPods ورسوم خفيفة بأسلوب Dynamic Island.</li>
      <li><strong>NotchDrop</strong> — درج السحب والإفلات. اسحب الملفات إلى النتش ثم أخرجها إلى مكان آخر.</li>
    </ul>
    <p>وإليك كيف تتقارن.</p>
    <h2>مقارنة الميزات</h2>
    """,
    "fr": """<p>La catégorie des apps d'encoche est petite mais distincte. Trois apps dominent les recherches sur le Mac App Store et les étoiles GitHub :</p>
    <ul>
      <li><strong>NotchNest</strong> — le hub de productivité. Calendrier, presse-papiers IA, notes, Pomodoro, musique, AirDrop, miroir, favoris.</li>
      <li><strong>Boring Notch</strong> — le contrôleur média et l'animateur. Now Playing, batterie AirPods, animations subtiles façon Dynamic Island.</li>
      <li><strong>NotchDrop</strong> — le bac glisser-déposer. Déposez des fichiers sur l'encoche, ressortez-les ailleurs.</li>
    </ul>
    <p>Voici comment elles se comparent.</p>
    <h2>Comparatif des fonctionnalités</h2>
    """,
    "pt-BR": """<p>A categoria de apps de notch é pequena, mas distinta. Três apps dominam as buscas na Mac App Store e as estrelas no GitHub:</p>
    <ul>
      <li><strong>NotchNest</strong> — a central de produtividade. Calendário, área com IA, notas, Pomodoro, música, AirDrop, espelho, favoritos.</li>
      <li><strong>Boring Notch</strong> — o controlador de mídia e animador. Now Playing, bateria dos AirPods, animações sutis estilo Dynamic Island.</li>
      <li><strong>NotchDrop</strong> — a bandeja de arrastar e soltar. Solte arquivos no notch, arraste-os para outro lugar.</li>
    </ul>
    <p>Veja como se comparam.</p>
    <h2>Comparativo de recursos</h2>
    """,
    "pt-PT": """<p>A categoria de apps de notch é pequena, mas distinta. Três apps dominam as pesquisas na Mac App Store e as estrelas no GitHub:</p>
    <ul>
      <li><strong>NotchNest</strong> — a central de produtividade. Calendário, área com IA, notas, Pomodoro, música, AirDrop, espelho, favoritos.</li>
      <li><strong>Boring Notch</strong> — o controlador de multimédia e animador. Now Playing, bateria dos AirPods, animações subtis ao estilo Dynamic Island.</li>
      <li><strong>NotchDrop</strong> — o tabuleiro de arrastar e largar. Largue ficheiros no notch, arraste-os para outro lado.</li>
    </ul>
    <p>Veja como se comparam.</p>
    <h2>Comparação de funcionalidades</h2>
    """,
    "es-MX": """<p>La categoría de apps de notch es pequeña pero distinta. Tres apps dominan las búsquedas en la Mac App Store y las estrellas de GitHub:</p>
    <ul>
      <li><strong>NotchNest</strong> — el centro de productividad. Calendario, portapapeles con IA, notas, Pomodoro, música, AirDrop, espejo, favoritos.</li>
      <li><strong>Boring Notch</strong> — el controlador de medios y animador. Now Playing, batería de AirPods, animaciones sutiles estilo Dynamic Island.</li>
      <li><strong>NotchDrop</strong> — la bandeja de arrastrar y soltar. Suelta archivos en el notch, arrástralos a otro lugar.</li>
    </ul>
    <p>Así se comparan.</p>
    <h2>Comparativa de funciones</h2>
    """,
}
BV_POST = {
    "de": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>NotchNest kostenlos holen</h3><p>Zehn Widgets, eine Notch, On-Device-Apple-Intelligence. macOS 14 oder neuer.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>
    <h2>Wann welche wählen</h2>
    <h3>Wähle NotchNest, wenn…</h3>
    <p>…du eine Notch-App willst, die alles macht. Kalender am Morgen, Zwischenablage-Suche mittags, Schnellnotizen bei einer Idee, Pomodoro nachmittags, Musik beim Fokussieren, AirDrop zum iPhone. Eine Installation, ein Menüleisten-Slot. Außerdem: dir sind App-Store-Sandboxing und Privatsphäre wichtig — NotchNest ist Apple-notarisiert und läuft vollständig auf dem Gerät, auch die KI.</p>
    <h3>Wähle Boring Notch, wenn…</h3>
    <p>…du den Großteil des Tages in Musik oder Video verbringst und einen schönen Dynamic-Island-artigen Medien-Controller willst. Boring Notch ist eine exzellente Einzweck-App — nur weißt du, dass du tauschst: kein Kalender, keine Notizen, keine KI, kein AirDrop, kein Sandbox.</p>
    <h3>Wähle NotchDrop, wenn…</h3>
    <p>…du den ganzen Tag Dateien zwischen Apps und Geräten bewegst. NotchDrops Tray-Modell ist das sauberste der Kategorie. Willst du aber auch einen Kalender in der Notch, installierst du eine zweite App.</p>
    <h2>Kann ich sie zusammen laufen lassen?</h2>
    <p>Technisch ja. macOS lässt alle drei gleichzeitig laufen. In der Praxis wird es chaotisch — sie kämpfen um dieselbe Hover-Region und du löst ständig das falsche Panel aus. Wähl eine. Das Nächste an „alle drei" in einer App ist NotchNest, das Medien-Controller und Datei-Tray neben seinen Produktivitäts-Widgets bündelt.</p>
    <h2>Die ehrliche Zusammenfassung</h2>
    <p>Boring Notch und NotchDrop sind jeweils exzellent in einer Sache. NotchNest will in zehn Dingen in einer Notch gut sein. Liebst du ein fokussiertes Einzweck-Tool schon, behalt es. Willst du, dass die Notch die halbe Menüleiste ersetzt, installiere NotchNest.</p>
    """,
    "zh": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>免费获取 NotchNest</h3><p>十个组件，一个刘海，本地 Apple Intelligence。macOS 14 或更新。</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>
    <h2>各自何时选</h2>
    <h3>选 NotchNest，如果……</h3>
    <p>……你想要一款样样都行的刘海应用。早上看日历、中午搜剪贴板、灵感来了记快速笔记、下午番茄钟、专注时放音乐、发文件到 iPhone 用 AirDrop。一次安装，一个菜单栏位。此外：你在意 App Store 沙盒与隐私——NotchNest 经 Apple 公证，完全在本地运行，连 AI 也是。</p>
    <h3>选 Boring Notch，如果……</h3>
    <p>……你一天大部分时间在音乐或视频里，想要一个漂亮的灵动岛式媒体控制器。Boring Notch 是出色的单一用途应用——只是要知道你在取舍：没有日历、没有笔记、没有 AI、没有 AirDrop、没有沙盒。</p>
    <h3>选 NotchDrop，如果……</h3>
    <p>……你整天在应用和设备间搬文件。NotchDrop 的托盘模型是同类里最干净的。但若你也想在刘海里放个日历，那就得再装第二个应用。</p>
    <h2>我能同时运行它们吗？</h2>
    <p>技术上可以。macOS 乐意同时运行三款。但实际会很乱——它们争夺同一悬停区域，你会不断触发错误面板。选一个。最接近“三合一”的单一应用是 NotchNest，它在生产力组件之外还捆绑了媒体控制器和文件托盘。</p>
    <h2>诚实的总结</h2>
    <p>Boring Notch 和 NotchDrop 各自把一件事做得出色。NotchNest 力求在一个刘海里把十件事都做好。如果你已经钟爱某个专注的单一用途工具，就留着。如果你想让刘海取代半条菜单栏，装 NotchNest。</p>
    """,
    "ar": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>احصل على NotchNest مجانًا</h3><p>عشر أدوات، نتش واحد، Apple Intelligence على الجهاز. macOS 14 أو أحدث.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>
    <h2>متى تختار كلًّا منها</h2>
    <h3>اختر NotchNest إن…</h3>
    <p>…أردت تطبيق نتش يفعل كل شيء. تقويم في الصباح، وبحث في الحافظة ظهرًا، وملاحظة سريعة عند فكرة، وبومودورو بعد الظهر، وموسيقى أثناء التركيز، وAirDrop إلى آيفونك. تثبيت واحد، مكان واحد في شريط القوائم. كذلك: تهتم بعزل App Store والخصوصية — NotchNest موثّق من Apple ويعمل بالكامل على الجهاز، حتى ميزات الذكاء الاصطناعي.</p>
    <h3>اختر Boring Notch إن…</h3>
    <p>…قضيت معظم يومك في الموسيقى أو الفيديو، وأردت متحكّم وسائط جميلًا بأسلوب Dynamic Island. Boring Notch تطبيق أحادي الغرض ممتاز — فقط اعلم أنك تبادل: لا تقويم ولا ملاحظات ولا ذكاء اصطناعي ولا AirDrop ولا عزل.</p>
    <h3>اختر NotchDrop إن…</h3>
    <p>…كنت تنقل الملفات بين التطبيقات والأجهزة طوال اليوم. نموذج درج NotchDrop هو الأنظف في الفئة. لكن إن أردت أيضًا تقويمًا في النتش، فستثبّت تطبيقًا ثانيًا.</p>
    <h2>هل يمكنني تشغيلها معًا؟</h2>
    <p>تقنيًا نعم. يشغّل macOS الثلاثة معًا بلا مشكلة. لكن عمليًا تصبح فوضى — تتنافس على منطقة التمرير نفسها وتفتح اللوحة الخطأ باستمرار. اختر واحدًا. أقرب شيء إلى «الثلاثة معًا» في تطبيق واحد هو NotchNest الذي يجمع متحكّم وسائط ودرج ملفات إلى جانب أدوات إنتاجيته.</p>
    <h2>الخلاصة الصادقة</h2>
    <p>Boring Notch وNotchDrop ممتازان كلٌّ في شيء واحد. أما NotchNest فيهدف إلى الإتقان في عشرة أشياء داخل نتش واحد. إن كنت تحبّ أداة أحادية الغرض مركّزة، احتفظ بها. وإن أردت أن يحلّ النتش محلّ نصف شريط القوائم، فثبّت NotchNest.</p>
    """,
    "fr": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Obtenez NotchNest gratuitement</h3><p>Dix widgets, une encoche, Apple Intelligence sur l'appareil. macOS 14 ou plus récent.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>
    <h2>Quand choisir chacune</h2>
    <h3>Choisissez NotchNest si…</h3>
    <p>…vous voulez une app d'encoche qui fait tout. Calendrier le matin, recherche du presse-papiers à midi, notes rapides quand une idée surgit, Pomodoro l'après-midi, musique pour vous concentrer, AirDrop vers votre iPhone. Une installation, un emplacement de barre des menus. Aussi : le bac à sable App Store et la confidentialité comptent pour vous — NotchNest est notarisé Apple et tourne entièrement sur l'appareil, IA comprise.</p>
    <h3>Choisissez Boring Notch si…</h3>
    <p>…vous passez l'essentiel de la journée dans la musique ou la vidéo et voulez un beau contrôleur média façon Dynamic Island. Boring Notch est une excellente app mono-usage — sachez juste que vous échangez : pas de calendrier, pas de notes, pas d'IA, pas d'AirDrop, pas de bac à sable.</p>
    <h3>Choisissez NotchDrop si…</h3>
    <p>…vous déplacez des fichiers entre apps et appareils toute la journée. Le modèle de bac de NotchDrop est le plus propre de la catégorie. Mais si vous voulez aussi un calendrier dans l'encoche, vous installez une deuxième app.</p>
    <h2>Puis-je les faire tourner ensemble ?</h2>
    <p>Techniquement, oui. macOS fait volontiers tourner les trois en même temps. En pratique, ça devient le bazar — elles se disputent la même zone de survol et vous déclenchez le mauvais panneau en permanence. Choisissez-en une. Le plus proche des « trois à la fois » dans une seule app, c'est NotchNest, qui réunit un contrôleur média et un bac à fichiers avec ses widgets de productivité.</p>
    <h2>Le résumé honnête</h2>
    <p>Boring Notch et NotchDrop excellent chacune dans une chose. NotchNest vise à être bonne en dix choses dans une encoche. Si vous adorez déjà un outil mono-usage focalisé, gardez-le. Si vous voulez que l'encoche remplace la moitié de votre barre des menus, installez NotchNest.</p>
    """,
    "pt-BR": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Baixe o NotchNest grátis</h3><p>Dez widgets, um notch, Apple Intelligence no dispositivo. macOS 14 ou mais recente.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>
    <h2>Quando escolher cada um</h2>
    <h3>Escolha o NotchNest se…</h3>
    <p>…você quer um app de notch que faça tudo. Calendário de manhã, busca na área de transferência ao meio-dia, notas rápidas quando surge uma ideia, Pomodoro à tarde, música para focar, AirDrop para o iPhone. Uma instalação, um espaço na barra de menus. Além disso: você se importa com sandbox da App Store e privacidade — o NotchNest é notarizado pela Apple e roda totalmente no dispositivo, inclusive a IA.</p>
    <h3>Escolha o Boring Notch se…</h3>
    <p>…você passa a maior parte do dia em música ou vídeo e quer um belo controlador de mídia estilo Dynamic Island. O Boring Notch é um excelente app de propósito único — só saiba que você troca: sem calendário, sem notas, sem IA, sem AirDrop, sem sandbox.</p>
    <h3>Escolha o NotchDrop se…</h3>
    <p>…você move arquivos entre apps e dispositivos o dia todo. O modelo de bandeja do NotchDrop é o mais limpo da categoria. Mas se você também quer um calendário no notch, vai instalar um segundo app.</p>
    <h2>Posso rodar os três juntos?</h2>
    <p>Tecnicamente, sim. O macOS roda os três ao mesmo tempo. Na prática vira bagunça — eles disputam a mesma região de hover e você abre o painel errado o tempo todo. Escolha um. O mais próximo de "os três" num único app é o NotchNest, que reúne um controlador de mídia e uma bandeja de arquivos ao lado dos widgets de produtividade.</p>
    <h2>O resumo honesto</h2>
    <p>Boring Notch e NotchDrop são excelentes cada um em uma coisa. O NotchNest quer ser bom em dez coisas em um notch. Se você já ama uma ferramenta focada de propósito único, fique com ela. Se quer que o notch substitua metade da sua barra de menus, instale o NotchNest.</p>
    """,
    "pt-PT": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Obtenha o NotchNest grátis</h3><p>Dez widgets, um notch, Apple Intelligence no dispositivo. macOS 14 ou mais recente.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>
    <h2>Quando escolher cada uma</h2>
    <h3>Escolha o NotchNest se…</h3>
    <p>…quer uma app de notch que faça tudo. Calendário de manhã, pesquisa na área de transferência ao meio-dia, notas rápidas quando surge uma ideia, Pomodoro à tarde, música para se focar, AirDrop para o iPhone. Uma instalação, um espaço na barra de menus. Além disso: importa-se com sandbox da App Store e privacidade — o NotchNest é notarizado pela Apple e corre totalmente no dispositivo, incluindo a IA.</p>
    <h3>Escolha o Boring Notch se…</h3>
    <p>…passa a maior parte do dia em música ou vídeo e quer um belo controlador de multimédia ao estilo Dynamic Island. O Boring Notch é uma excelente app de propósito único — só saiba que troca: sem calendário, sem notas, sem IA, sem AirDrop, sem sandbox.</p>
    <h3>Escolha o NotchDrop se…</h3>
    <p>…move ficheiros entre apps e dispositivos o dia todo. O modelo de tabuleiro do NotchDrop é o mais limpo da categoria. Mas se também quer um calendário no notch, vai instalar uma segunda app.</p>
    <h2>Posso correr as três juntas?</h2>
    <p>Tecnicamente, sim. O macOS corre as três ao mesmo tempo. Na prática torna-se confuso — disputam a mesma região de hover e abre o painel errado a toda a hora. Escolha uma. O mais próximo de "as três" numa única app é o NotchNest, que reúne um controlador de multimédia e um tabuleiro de ficheiros ao lado dos widgets de produtividade.</p>
    <h2>O resumo honesto</h2>
    <p>Boring Notch e NotchDrop são excelentes cada uma numa coisa. O NotchNest quer ser bom em dez coisas num notch. Se já adora uma ferramenta focada de propósito único, fique com ela. Se quer que o notch substitua metade da sua barra de menus, instale o NotchNest.</p>
    """,
    "es-MX": """<div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Obtén NotchNest gratis</h3><p>Diez widgets, un notch, Apple Intelligence en el dispositivo. macOS 14 o posterior.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>
    <h2>Cuándo elegir cada una</h2>
    <h3>Elige NotchNest si…</h3>
    <p>…quieres una app de notch que lo haga todo. Calendario en la mañana, búsqueda del portapapeles al mediodía, notas rápidas cuando llega una idea, Pomodoro en la tarde, música para concentrarte, AirDrop a tu iPhone. Una instalación, un espacio en la barra de menús. Además: te importa el sandbox de la App Store y la privacidad — NotchNest está notarizado por Apple y corre por completo en el dispositivo, incluida la IA.</p>
    <h3>Elige Boring Notch si…</h3>
    <p>…pasas la mayor parte del día en música o video y quieres un hermoso controlador de medios estilo Dynamic Island. Boring Notch es una excelente app de un solo propósito — solo ten en cuenta que cambias: sin calendario, sin notas, sin IA, sin AirDrop, sin sandbox.</p>
    <h3>Elige NotchDrop si…</h3>
    <p>…mueves archivos entre apps y dispositivos todo el día. El modelo de bandeja de NotchDrop es el más limpio de la categoría. Pero si además quieres un calendario en el notch, instalarás una segunda app.</p>
    <h2>¿Puedo usarlas juntas?</h2>
    <p>Técnicamente, sí. macOS corre las tres a la vez sin problema. En la práctica se vuelve un desorden — compiten por la misma región de hover y abres el panel equivocado todo el tiempo. Elige una. Lo más cercano a "las tres" en una sola app es NotchNest, que reúne un controlador de medios y una bandeja de archivos junto a sus widgets de productividad.</p>
    <h2>El resumen honesto</h2>
    <p>Boring Notch y NotchDrop son excelentes cada una en una cosa. NotchNest busca ser bueno en diez cosas en un notch. Si ya amas una herramienta enfocada de un solo propósito, quédatela. Si quieres que el notch reemplace la mitad de tu barra de menús, instala NotchNest.</p>
    """,
}
BVBVD = {}
for _loc in _LOCS:
    _m = dict(BV_META[_loc])
    _m["kicker"] = KICK["comparison"][_loc]
    _m["body"] = BV_PRE[_loc] + _table3(_loc, BV_TH[_loc], BV_FEAT[_loc], _c3(_loc)) + "\n    " + BV_POST[_loc]
    _m["related"] = _related(_loc, ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "EN — 2026."))
    BVBVD[_loc] = _m


# ── how-to-hide-the-notch-on-mac ────────────────────────────────────────────
HIDE = {
    "de": {"title": "Notch auf dem Mac verstecken — NotchNest", "description": "Drei Wege, die MacBook-Notch in macOS zu verstecken — skalierte Auflösung, schwarze Menüleiste und Drittanbieter-Apps. Plus die bessere Alternative: sie nützlich machen.",
           "og_title": "Notch auf dem Mac verstecken", "og_desc": "Alle Wege, die Notch zu verstecken — und die bessere Alternative.",
           "jsonld_headline": "Notch auf dem Mac verstecken", "jsonld_desc": "Alle Methoden, die MacBook-Notch zu verstecken, und warum du sie vielleicht besser nutzt.",
           "kicker": KICK["guide"]["de"], "h1": "Notch auf dem Mac verstecken",
           "lede": "Magst du die Notch nicht? Du kannst sie in ein paar Klicks verstecken — oder etwas Klügeres damit machen. Hier alle Optionen, geordnet.",
           "readtime": READ5["de"], "crumb_this": "Notch verstecken",
           "faq": [("Kann man die MacBook-Notch ganz entfernen?", "Nein — die Notch ist physische Hardware, die die Kamera beherbergt. Du kannst sie nur visuell verstecken, per skalierter Auflösung oder schwarzer Menüleiste, beide umkehrbar."),
                   ("Verliert man beim Verstecken Bildschirmplatz?", "Ja. Verstecken per skalierter Auflösung oder schwarzem Balken entfernt etwa 74 vertikale Pixel Menüleiste. Die Notch zu nutzen behält alle Pixel."),
                   ("Welche App versteckt die Mac-Notch am besten?", "TopNotch ist die beliebteste kostenlose Tarn-App. Viele bevorzugen aber NotchNest, das die Notch nützlich macht, statt sie zu verstecken."),
                   ("Hilft das Verstecken bei Akku oder Performance?", "Nein. Die Notch hat keine Performance-Kosten. Verstecken ist rein kosmetisch.")],
           "body": """<p>Die MacBook-Notch spaltet die Gemüter. Wenn sie dich stört, geben dir macOS und ein paar kostenlose Tools mehrere Wege, sie verschwinden zu lassen. Hier jede Methode, von einer eingebauten Einstellung bis zu Drittanbieter-Apps — und warum du sie vielleicht gar nicht verstecken willst.</p>
    <h2>Methode 1 — Skalierte Auflösung (eingebaut, ohne Apps)</h2>
    <p>macOS kann den oberen Bildschirmrand letterboxen, sodass die Notch hinter einem gleichmäßigen schwarzen Balken verschwindet:</p>
    <ol>
      <li>Öffne <strong>Systemeinstellungen → Displays</strong>.</li>
      <li>Halte <strong>Option</strong> und klicke <strong>Skaliert</strong>, um alle Auflösungen zu zeigen.</li>
      <li>Wähle eine als „nicht Vollbild" markierte Auflösung — macOS polstert die Menüleiste schwarz und versteckt die Notch.</li>
    </ol>
    <p>Nachteil: du verlierst rund 74 vertikale Pixel Menüleiste. Alles rutscht leicht nach unten. Kostenlos und umkehrbar.</p>
    <h2>Methode 2 — Trick mit schwarzem Menüleisten-Hintergrund</h2>
    <p>Hat dein Hintergrundbild oben einen schwarzen Streifen, fügt sich die Notch visuell ein, während du die volle Auflösung behältst. Apps wie TopNotch automatisieren das, indem sie dein Wallpaper abtasten und den Menüleisten-Hintergrund schwärzen. Kostenlos, und du behältst deine Pixel.</p>
    <h2>Methode 3 — Drittanbieter-Notch-Tools</h2>
    <p>Tools wie TopNotch und Forehead existieren rein zur Tarnung der Notch. Sie sind leichtgewichtig und machen eine Sache gut. Aber sie verstecken die Notch nur — sie geben diesem Bildschirmbereich keinen Zweck.</p>
    <h2>Die bessere Option: die Notch nützlich machen</h2>
    <p>Die Notch zu verstecken beseitigt ein kosmetisches Ärgernis, verschwendet aber die Hardware. Die Notch sitzt in Platz, den die Menüleiste ohnehin belegt, kostet dich also nichts — außer du blendest sie aus, was tatsächlich nutzbare Pixel entfernt.</p>
    <p>Eine Notch-App wie NotchNest geht den umgekehrten Weg: Hover die Notch und sie klappt zu einem Produktivitäts-Panel auf — Kalender, KI-Zwischenablage, Schnellnotizen, Pomodoro, Musiksteuerung und Drag-to-AirDrop. Du bemerkst die Notch nicht mehr, weil sie etwas tut. Probier den interaktiven Notch-Playground, um sie ohne Installation zu sehen.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Mach deine Notch nützlich</h3><p>NotchNest bringt zehn Tools in die Notch deines MacBooks. Kostenlos im Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>
    <h2>Wie du die Notch zurückholst</h2>
    <p>Jede Methode oben ist umkehrbar. Setz deine Auflösung in Displays auf <strong>Standard</strong> zurück oder beende die Tarn-App. Es werden keine Systemdateien geändert.</p>""",
           "related": _related("de", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Übersicht 2026."))},
    "zh": {"title": "如何在 Mac 上隐藏刘海 — NotchNest", "description": "在 macOS 上隐藏 MacBook 刘海的三种方法——缩放分辨率、黑色菜单栏和第三方应用。以及更好的选择：让它有用。",
           "og_title": "如何在 Mac 上隐藏刘海", "og_desc": "隐藏刘海的所有方法——以及更好的选择。",
           "jsonld_headline": "如何在 Mac 上隐藏刘海", "jsonld_desc": "隐藏 MacBook 刘海的所有方法，以及为何你也许更该用它。",
           "kicker": KICK["guide"]["zh"], "h1": "如何在 Mac 上隐藏刘海",
           "lede": "不喜欢刘海？几下点击就能隐藏——或者用它做点更聪明的事。这里是所有选项，按优劣排序。",
           "readtime": READ5["zh"], "crumb_this": "隐藏刘海",
           "faq": [("能彻底移除 MacBook 刘海吗？", "不能——刘海是容纳摄像头的物理硬件。你只能用缩放分辨率或黑色菜单栏在视觉上隐藏它，两者都可还原。"),
                   ("隐藏刘海会损失屏幕空间吗？", "会。用缩放分辨率或黑边隐藏会去掉约 74 像素的菜单栏高度。使用刘海（而非隐藏）则保留全部像素。"),
                   ("隐藏 Mac 刘海最好的应用是哪款？", "TopNotch 是最热门的免费遮盖应用。但很多用户更偏好 NotchNest——它让刘海变得有用，而不是隐藏。"),
                   ("隐藏刘海对电池或性能有帮助吗？", "没有。刘海没有性能开销。隐藏纯属外观。")],
           "body": """<p>MacBook 刘海让人褒贬不一。如果它让你困扰，macOS 和几款免费工具提供了多种让它消失的方法。这里列出每种方法，从内建设置到第三方应用——以及为何你也许根本不该隐藏它。</p>
    <h2>方法一 — 缩放分辨率（内建，无需应用）</h2>
    <p>macOS 可为屏幕顶部加黑边，让刘海藏在一条均匀的黑条后：</p>
    <ol>
      <li>打开<strong>系统设置 → 显示器</strong>。</li>
      <li>按住 <strong>Option</strong> 并点击<strong>缩放</strong>以显示所有分辨率。</li>
      <li>选一个标注为“非全屏”的分辨率——macOS 会把菜单栏区域填黑，隐藏刘海。</li>
    </ol>
    <p>代价：你会损失约 74 像素的菜单栏高度。一切略微下移。免费且可还原。</p>
    <h2>方法二 — 黑色菜单栏壁纸技巧</h2>
    <p>如果壁纸顶端有一条黑带，刘海在视觉上就会融入，同时保留完整分辨率。TopNotch 之类的应用会采样你的壁纸并把菜单栏背景填黑，实现自动化。免费，且保留像素。</p>
    <h2>方法三 — 第三方刘海工具</h2>
    <p>TopNotch 和 Forehead 之类的工具纯粹用于遮盖刘海。它们轻量，把一件事做好。但它们只隐藏刘海——不会给那块屏幕区域任何用途。</p>
    <h2>更好的选择：让刘海有用</h2>
    <p>隐藏刘海消除了一个外观上的烦恼，却浪费了硬件。刘海占用的是菜单栏本就占据的空间，因此对你没有任何代价——除非你把它涂黑，那反而会去掉可用像素。</p>
    <p>NotchNest 这样的刘海应用采取相反思路：悬停刘海，它便展开为生产力面板——日历、AI 剪贴板、快速笔记、番茄钟、音乐控制和拖拽 AirDrop。你不再注意刘海，因为它在做事。试试交互式刘海演示，不安装即可体验。</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>让你的刘海有用</h3><p>NotchNest 把十个工具放进 MacBook 刘海。在 Mac App Store 免费。</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>
    <h2>如何恢复刘海</h2>
    <p>以上每种方法都可还原。在“显示器”里把分辨率设回<strong>默认</strong>，或退出遮盖应用。不会更改任何系统文件。</p>""",
           "related": _related("zh", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "英文——2026 盘点。"))},
    "ar": {"title": "كيفية إخفاء النتش على الماك — NotchNest", "description": "ثلاث طرق لإخفاء نتش الماك بوك في macOS — دقة مُقاسة، وشريط قوائم أسود، وتطبيقات طرف ثالث. إضافةً إلى البديل الأفضل: اجعله مفيدًا.",
           "og_title": "كيفية إخفاء النتش على الماك", "og_desc": "كل طرق إخفاء النتش — والبديل الأفضل.",
           "jsonld_headline": "كيفية إخفاء النتش على الماك", "jsonld_desc": "كل طرق إخفاء نتش الماك بوك، ولماذا قد يكون استخدامه أفضل.",
           "kicker": KICK["guide"]["ar"], "h1": "كيفية إخفاء النتش على الماك",
           "lede": "لا يعجبك النتش؟ يمكنك إخفاؤه بنقرتين — أو فعل شيء أذكى به. إليك كل الخيارات مرتّبة.",
           "readtime": READ5["ar"], "crumb_this": "إخفاء النتش",
           "faq": [("هل يمكن إزالة نتش الماك بوك تمامًا؟", "لا — النتش عتاد مادي يحتضن الكاميرا. يمكنك إخفاؤه بصريًا فقط بدقة مُقاسة أو شريط قوائم أسود، وكلاهما قابل للتراجع."),
                   ("هل يخسر إخفاء النتش مساحة شاشة؟", "نعم. الإخفاء بدقة مُقاسة أو شريط أسود يزيل نحو 74 بكسل من ارتفاع شريط القوائم. استخدام النتش يحفظ كل البكسلات."),
                   ("ما أفضل تطبيق لإخفاء نتش الماك؟", "TopNotch أشهر تطبيق تمويه مجاني. لكن كثيرين يفضّلون NotchNest الذي يجعل النتش مفيدًا بدل إخفائه."),
                   ("هل يساعد إخفاء النتش في البطارية أو الأداء؟", "لا. لا كلفة أداء للنتش. الإخفاء تجميلي بحت.")],
           "body": """<p>يقسم نتش الماك بوك الناس. إن كان يزعجك، يمنحك macOS وبضعة أدوات مجانية عدة طرق لإخفائه. إليك كل طريقة، من إعداد مدمج إلى تطبيقات طرف ثالث — ولماذا قد لا ترغب بإخفائه أصلًا.</p>
    <h2>الطريقة 1 — دقة مُقاسة (مدمجة، بلا تطبيقات)</h2>
    <p>يمكن لـ macOS إضافة حاشية سوداء أعلى الشاشة ليختفي النتش خلف شريط أسود موحّد:</p>
    <ol>
      <li>افتح <strong>إعدادات النظام ← الشاشات</strong>.</li>
      <li>اضغط <strong>Option</strong> وانقر <strong>مُقاس</strong> لإظهار كل الدقات.</li>
      <li>اختر دقة موسومة بأنها «لا تستخدم كامل الشاشة» — يملأ macOS منطقة شريط القوائم بالأسود ويخفي النتش.</li>
    </ol>
    <p>المقابل: تخسر نحو 74 بكسل رأسيًا من شريط القوائم. ينزل كل شيء قليلًا. مجاني وقابل للتراجع.</p>
    <h2>الطريقة 2 — حيلة خلفية شريط قوائم سوداء</h2>
    <p>إن كان لخلفيتك شريط أسود في الأعلى، يندمج النتش بصريًا مع بقاء الدقة الكاملة. تؤتمت تطبيقات مثل TopNotch ذلك بأخذ عيّنة من خلفيتك وتسويد خلفية شريط القوائم. مجاني، وتحتفظ ببكسلاتك.</p>
    <h2>الطريقة 3 — أدوات نتش من طرف ثالث</h2>
    <p>أدوات مثل TopNotch وForehead موجودة بحتًا لتمويه النتش. خفيفة وتُتقن مهمة واحدة. لكنها تخفي النتش فقط — لا تمنح تلك المساحة أي غرض.</p>
    <h2>الخيار الأفضل: اجعل النتش مفيدًا</h2>
    <p>إخفاء النتش يزيل إزعاجًا تجميليًا لكنه يهدر العتاد. يقع النتش في مساحة يشغلها شريط القوائم أصلًا، فلا يكلّفك شيئًا — إلا إن سوّدته، فذلك يزيل بكسلات قابلة للاستخدام فعلًا.</p>
    <p>يتّبع تطبيق نتش مثل NotchNest النهج المعاكس: مرّر المؤشر فوق النتش فينفتح إلى لوحة إنتاجية — تقويم وحافظة بالذكاء الاصطناعي وملاحظات سريعة وبومودورو والتحكم بالموسيقى والسحب إلى AirDrop. تتوقف عن ملاحظة النتش لأنه يفعل شيئًا. جرّب عرض النتش التفاعلي لرؤيته دون تثبيت أي شيء.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>اجعل نتشك مفيدًا</h3><p>يضع NotchNest عشر أدوات في نتش الماك بوك. مجانًا على Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>
    <h2>كيف تعيد النتش</h2>
    <p>كل طريقة أعلاه قابلة للتراجع. أعد ضبط الدقة إلى <strong>الافتراضي</strong> في الشاشات، أو أغلق تطبيق التمويه. لا تُغيَّر أي ملفات نظام.</p>""",
           "related": _related("ar", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "إنجليزي — اختيارات 2026."))},
    "fr": {"title": "Comment masquer l'encoche sur Mac — NotchNest", "description": "Trois façons de masquer l'encoche du MacBook sous macOS — résolution mise à l'échelle, barre des menus noire et apps tierces. Plus la meilleure alternative : la rendre utile.",
           "og_title": "Comment masquer l'encoche sur Mac", "og_desc": "Toutes les façons de masquer l'encoche — et la meilleure alternative.",
           "jsonld_headline": "Comment masquer l'encoche sur Mac", "jsonld_desc": "Toutes les méthodes pour masquer l'encoche du MacBook, et pourquoi mieux vaut peut-être l'utiliser.",
           "kicker": KICK["guide"]["fr"], "h1": "Comment masquer l'encoche sur Mac",
           "lede": "Vous n'aimez pas l'encoche ? Vous pouvez la masquer en quelques clics — ou en faire quelque chose de plus malin. Voici toutes les options, classées.",
           "readtime": READ5["fr"], "crumb_this": "Masquer l'encoche",
           "faq": [("Peut-on retirer complètement l'encoche du MacBook ?", "Non — l'encoche est du matériel qui loge la caméra. Vous ne pouvez la masquer que visuellement, par une résolution mise à l'échelle ou une barre des menus noire, deux méthodes réversibles."),
                   ("Masquer l'encoche fait-il perdre de l'espace écran ?", "Oui. La masquer via une résolution mise à l'échelle ou une barre noire retire environ 74 pixels verticaux de barre des menus. Utiliser l'encoche garde tous vos pixels."),
                   ("Quelle est la meilleure app pour masquer l'encoche du Mac ?", "TopNotch est l'app de camouflage gratuite la plus populaire. Mais beaucoup préfèrent NotchNest, qui rend l'encoche utile au lieu de la masquer."),
                   ("Masquer l'encoche aide-t-il la batterie ou les performances ?", "Non. L'encoche n'a aucun coût de performance. La masquer est purement esthétique.")],
           "body": """<p>L'encoche du MacBook divise. Si elle vous dérange, macOS et quelques outils gratuits offrent plusieurs façons de la faire disparaître. Voici chaque méthode, d'un réglage intégré aux apps tierces — et pourquoi vous ne voudrez peut-être pas la masquer du tout.</p>
    <h2>Méthode 1 — Résolution mise à l'échelle (intégrée, sans app)</h2>
    <p>macOS peut ajouter des bandes en haut de l'écran pour que l'encoche se cache derrière une barre noire uniforme :</p>
    <ol>
      <li>Ouvrez <strong>Réglages Système → Moniteurs</strong>.</li>
      <li>Maintenez <strong>Option</strong> et cliquez <strong>Mise à l'échelle</strong> pour révéler toutes les résolutions.</li>
      <li>Choisissez une résolution marquée comme « n'utilisant pas tout l'écran » — macOS rembourre la barre des menus en noir et masque l'encoche.</li>
    </ol>
    <p>Compromis : vous perdez environ 74 pixels verticaux de barre des menus. Tout descend légèrement. Gratuit et réversible.</p>
    <h2>Méthode 2 — L'astuce du fond noir de barre des menus</h2>
    <p>Si votre fond d'écran a une bande noire tout en haut, l'encoche se fond visuellement tout en gardant la pleine résolution. Des apps comme TopNotch automatisent cela en échantillonnant votre fond et en noircissant l'arrière-plan de la barre des menus. Gratuit, et vous gardez vos pixels.</p>
    <h2>Méthode 3 — Utilitaires d'encoche tiers</h2>
    <p>Des outils comme TopNotch et Forehead existent uniquement pour camoufler l'encoche. Ils sont légers et font bien une chose. Mais ils ne font que masquer l'encoche — ils ne donnent aucun but à cette zone d'écran.</p>
    <h2>La meilleure option : rendre l'encoche utile</h2>
    <p>Masquer l'encoche supprime un désagrément esthétique mais gâche le matériel. L'encoche occupe un espace que la barre des menus utilise déjà, elle ne vous coûte donc rien — sauf si vous la noircissez, ce qui retire réellement des pixels utilisables.</p>
    <p>Une app d'encoche comme NotchNest prend le parti inverse : survolez l'encoche et elle se déploie en un panneau de productivité — calendrier, presse-papiers IA, notes rapides, Pomodoro, contrôle de la musique et glisser-vers-AirDrop. Vous cessez de remarquer l'encoche parce qu'elle fait quelque chose. Essayez le terrain de jeu interactif de l'encoche pour la voir sans rien installer.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Rendez votre encoche utile</h3><p>NotchNest met dix outils dans l'encoche de votre MacBook. Gratuit sur le Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>
    <h2>Comment faire revenir l'encoche</h2>
    <p>Chaque méthode ci-dessus est réversible. Remettez votre résolution sur <strong>Par défaut</strong> dans Moniteurs, ou quittez l'app de camouflage. Aucun fichier système n'est modifié.</p>""",
           "related": _related("fr", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Anglais — sélection 2026."))},
    "pt-BR": {"title": "Como esconder o notch no Mac — NotchNest", "description": "Três formas de esconder o notch do MacBook no macOS — resolução escalada, barra de menus preta e apps de terceiros. Além da melhor alternativa: torná-lo útil.",
              "og_title": "Como esconder o notch no Mac", "og_desc": "Todas as formas de esconder o notch — e a melhor alternativa.",
              "jsonld_headline": "Como esconder o notch no Mac", "jsonld_desc": "Todos os métodos para esconder o notch do MacBook, e por que talvez seja melhor usá-lo.",
              "kicker": KICK["guide"]["pt-BR"], "h1": "Como esconder o notch no Mac",
              "lede": "Não curte o notch? Você pode escondê-lo em alguns cliques — ou fazer algo mais esperto com ele. Aqui estão todas as opções, ranqueadas.",
              "readtime": READ5["pt-BR"], "crumb_this": "Esconder o notch",
              "faq": [("Dá para remover totalmente o notch do MacBook?", "Não — o notch é hardware físico que abriga a câmera. Você só pode escondê-lo visualmente com uma resolução escalada ou barra de menus preta, ambos reversíveis."),
                      ("Esconder o notch perde espaço de tela?", "Sim. Escondê-lo com resolução escalada ou barra preta remove cerca de 74 pixels verticais da barra de menus. Usar o notch mantém todos os pixels."),
                      ("Qual o melhor app para esconder o notch do Mac?", "O TopNotch é o app de camuflagem gratuito mais popular. Mas muitos preferem o NotchNest, que torna o notch útil em vez de escondê-lo."),
                      ("Esconder o notch ajuda na bateria ou desempenho?", "Não. O notch não tem custo de desempenho. Escondê-lo é puramente estético.")],
              "body": """<p>O notch do MacBook divide as pessoas. Se ele te incomoda, o macOS e algumas ferramentas grátis dão vários jeitos de fazê-lo sumir. Aqui está cada método, de um ajuste embutido a apps de terceiros — e por que você talvez nem queira escondê-lo.</p>
    <h2>Método 1 — Resolução escalada (embutido, sem apps)</h2>
    <p>O macOS pode colocar tarjas no topo da tela para o notch se esconder atrás de uma barra preta uniforme:</p>
    <ol>
      <li>Abra <strong>Ajustes do Sistema → Monitores</strong>.</li>
      <li>Segure <strong>Option</strong> e clique em <strong>Escalada</strong> para revelar todas as resoluções.</li>
      <li>Escolha uma resolução marcada como "não usa a tela inteira" — o macOS preenche a área da barra de menus de preto, escondendo o notch.</li>
    </ol>
    <p>Contrapartida: você perde cerca de 74 pixels verticais da barra de menus. Tudo desce um pouco. Grátis e reversível.</p>
    <h2>Método 2 — O truque do papel de parede com barra preta</h2>
    <p>Se o seu papel de parede tem uma faixa preta bem no topo, o notch se mistura visualmente enquanto você mantém a resolução total. Apps como o TopNotch automatizam isso amostrando o seu papel de parede e escurecendo o fundo da barra de menus. Grátis, e você mantém os pixels.</p>
    <h2>Método 3 — Utilitários de notch de terceiros</h2>
    <p>Ferramentas como TopNotch e Forehead existem só para camuflar o notch. São leves e fazem uma coisa bem. Mas só escondem o notch — não dão nenhum propósito àquela área de tela.</p>
    <h2>A melhor opção: tornar o notch útil</h2>
    <p>Esconder o notch elimina um incômodo estético, mas desperdiça o hardware. O notch ocupa um espaço que a barra de menus já usa, então não te custa nada — a menos que você o apague, o que aí sim remove pixels usáveis.</p>
    <p>Um app de notch como o NotchNest faz o contrário: passe o cursor no notch e ele se expande em um painel de produtividade — calendário, área de transferência com IA, notas rápidas, Pomodoro, controles de música e arrastar para AirDrop. Você para de notar o notch porque ele está fazendo algo. Teste o playground interativo do notch para vê-lo sem instalar nada.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Grátis na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>
    <h2>Como trazer o notch de volta</h2>
    <p>Todos os métodos acima são reversíveis. Volte a resolução para <strong>Padrão</strong> em Monitores, ou saia do app de camuflagem. Nenhum arquivo de sistema é alterado.</p>""",
              "related": _related("pt-BR", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "pt-PT": {"title": "Como esconder o notch no Mac — NotchNest", "description": "Três formas de esconder o notch do MacBook no macOS — resolução escalada, barra de menus preta e apps de terceiros. Além da melhor alternativa: torná-lo útil.",
              "og_title": "Como esconder o notch no Mac", "og_desc": "Todas as formas de esconder o notch — e a melhor alternativa.",
              "jsonld_headline": "Como esconder o notch no Mac", "jsonld_desc": "Todos os métodos para esconder o notch do MacBook, e porque talvez seja melhor usá-lo.",
              "kicker": KICK["guide"]["pt-PT"], "h1": "Como esconder o notch no Mac",
              "lede": "Não gosta do notch? Pode escondê-lo em alguns cliques — ou fazer algo mais inteligente com ele. Aqui estão todas as opções, ordenadas.",
              "readtime": READ5["pt-PT"], "crumb_this": "Esconder o notch",
              "faq": [("Dá para remover totalmente o notch do MacBook?", "Não — o notch é hardware físico que aloja a câmara. Só pode escondê-lo visualmente com uma resolução escalada ou barra de menus preta, ambos reversíveis."),
                      ("Esconder o notch perde espaço de ecrã?", "Sim. Escondê-lo com resolução escalada ou barra preta remove cerca de 74 pixels verticais da barra de menus. Usar o notch mantém todos os pixels."),
                      ("Qual a melhor app para esconder o notch do Mac?", "O TopNotch é a app de camuflagem gratuita mais popular. Mas muitos preferem o NotchNest, que torna o notch útil em vez de o esconder."),
                      ("Esconder o notch ajuda na bateria ou desempenho?", "Não. O notch não tem custo de desempenho. Escondê-lo é puramente estético.")],
              "body": """<p>O notch do MacBook divide as pessoas. Se o incomoda, o macOS e algumas ferramentas gratuitas dão várias formas de o fazer desaparecer. Aqui está cada método, de uma definição integrada a apps de terceiros — e porque talvez nem o queira esconder.</p>
    <h2>Método 1 — Resolução escalada (integrado, sem apps)</h2>
    <p>O macOS pode colocar tarjas no topo do ecrã para o notch se esconder atrás de uma barra preta uniforme:</p>
    <ol>
      <li>Abra <strong>Definições do Sistema → Monitores</strong>.</li>
      <li>Mantenha <strong>Option</strong> e clique em <strong>Escalado</strong> para revelar todas as resoluções.</li>
      <li>Escolha uma resolução marcada como "não usa o ecrã inteiro" — o macOS preenche a área da barra de menus a preto, escondendo o notch.</li>
    </ol>
    <p>Contrapartida: perde cerca de 74 pixels verticais da barra de menus. Tudo desce um pouco. Gratuito e reversível.</p>
    <h2>Método 2 — O truque do fundo de ecrã com barra preta</h2>
    <p>Se o seu fundo de ecrã tem uma faixa preta no topo, o notch mistura-se visualmente enquanto mantém a resolução total. Apps como o TopNotch automatizam isto amostrando o seu fundo e escurecendo o fundo da barra de menus. Gratuito, e mantém os pixels.</p>
    <h2>Método 3 — Utilitários de notch de terceiros</h2>
    <p>Ferramentas como TopNotch e Forehead existem só para camuflar o notch. São leves e fazem uma coisa bem. Mas só escondem o notch — não dão nenhum propósito àquela área de ecrã.</p>
    <h2>A melhor opção: tornar o notch útil</h2>
    <p>Esconder o notch elimina um incómodo estético, mas desperdiça o hardware. O notch ocupa um espaço que a barra de menus já usa, por isso não lhe custa nada — a menos que o apague, o que aí sim remove pixels utilizáveis.</p>
    <p>Uma app de notch como o NotchNest faz o contrário: passe o cursor no notch e ele expande-se num painel de produtividade — calendário, área de transferência com IA, notas rápidas, Pomodoro, controlos de música e arrastar para AirDrop. Deixa de reparar no notch porque ele está a fazer algo. Experimente o playground interativo do notch para o ver sem instalar nada.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne o seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Gratuito na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>
    <h2>Como trazer o notch de volta</h2>
    <p>Todos os métodos acima são reversíveis. Volte a resolução para <strong>Predefinição</strong> em Monitores, ou saia da app de camuflagem. Nenhum ficheiro de sistema é alterado.</p>""",
              "related": _related("pt-PT", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "es-MX": {"title": "Cómo ocultar el notch en Mac — NotchNest", "description": "Tres formas de ocultar el notch del MacBook en macOS — resolución escalada, barra de menús negra y apps de terceros. Más la mejor alternativa: hacerlo útil.",
              "og_title": "Cómo ocultar el notch en Mac", "og_desc": "Todas las formas de ocultar el notch — y la mejor alternativa.",
              "jsonld_headline": "Cómo ocultar el notch en Mac", "jsonld_desc": "Todos los métodos para ocultar el notch del MacBook, y por qué quizá sea mejor usarlo.",
              "kicker": KICK["guide"]["es-MX"], "h1": "Cómo ocultar el notch en Mac",
              "lede": "¿No te gusta el notch? Puedes ocultarlo en un par de clics — o hacer algo más inteligente con él. Aquí están todas las opciones, ordenadas.",
              "readtime": READ5["es-MX"], "crumb_this": "Ocultar el notch",
              "faq": [("¿Se puede eliminar por completo el notch del MacBook?", "No — el notch es hardware físico que aloja la cámara. Solo puedes ocultarlo visualmente con una resolución escalada o una barra de menús negra, ambos reversibles."),
                      ("¿Ocultar el notch pierde espacio de pantalla?", "Sí. Ocultarlo con una resolución escalada o barra negra quita unos 74 píxeles verticales de la barra de menús. Usar el notch conserva todos los píxeles."),
                      ("¿Cuál es la mejor app para ocultar el notch del Mac?", "TopNotch es la app de camuflaje gratis más popular. Pero muchos prefieren NotchNest, que hace útil el notch en lugar de ocultarlo."),
                      ("¿Ocultar el notch ayuda a la batería o el rendimiento?", "No. El notch no tiene costo de rendimiento. Ocultarlo es puramente estético.")],
              "body": """<p>El notch del MacBook divide a la gente. Si te molesta, macOS y unas cuantas herramientas gratis te dan varias formas de hacerlo desaparecer. Aquí está cada método, desde un ajuste integrado hasta apps de terceros — y por qué quizá no quieras ocultarlo en absoluto.</p>
    <h2>Método 1 — Resolución escalada (integrado, sin apps)</h2>
    <p>macOS puede poner barras en la parte superior de la pantalla para que el notch se oculte tras una barra negra uniforme:</p>
    <ol>
      <li>Abre <strong>Configuración del Sistema → Pantallas</strong>.</li>
      <li>Mantén <strong>Opción</strong> y haz clic en <strong>Escalada</strong> para revelar todas las resoluciones.</li>
      <li>Elige una resolución marcada como "no usa toda la pantalla" — macOS rellena el área de la barra de menús de negro, ocultando el notch.</li>
    </ol>
    <p>Contrapartida: pierdes unos 74 píxeles verticales de barra de menús. Todo baja un poco. Gratis y reversible.</p>
    <h2>Método 2 — El truco del fondo con barra negra</h2>
    <p>Si tu fondo de pantalla tiene una franja negra arriba, el notch se mezcla visualmente mientras conservas la resolución completa. Apps como TopNotch lo automatizan muestreando tu fondo y oscureciendo el fondo de la barra de menús. Gratis, y conservas tus píxeles.</p>
    <h2>Método 3 — Utilidades de notch de terceros</h2>
    <p>Herramientas como TopNotch y Forehead existen solo para camuflar el notch. Son ligeras y hacen una cosa bien. Pero solo ocultan el notch — no le dan ningún propósito a esa área de pantalla.</p>
    <h2>La mejor opción: hacer útil el notch</h2>
    <p>Ocultar el notch elimina una molestia estética, pero desperdicia el hardware. El notch ocupa un espacio que la barra de menús ya usa, así que no te cuesta nada — a menos que lo pongas en negro, lo que sí quita píxeles utilizables.</p>
    <p>Una app de notch como NotchNest hace lo contrario: pasa el cursor por el notch y se expande en un panel de productividad — calendario, portapapeles con IA, notas rápidas, Pomodoro, controles de música y arrastrar a AirDrop. Dejas de notar el notch porque está haciendo algo. Prueba el playground interactivo del notch para verlo sin instalar nada.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Haz útil tu notch</h3><p>NotchNest pone diez herramientas en el notch de tu MacBook. Gratis en el Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>
    <h2>Cómo recuperar el notch</h2>
    <p>Todos los métodos anteriores son reversibles. Vuelve tu resolución a <strong>Predeterminada</strong> en Pantallas, o cierra la app de camuflaje. No se modifica ningún archivo del sistema.</p>""",
              "related": _related("es-MX", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglés — selección 2026."))},
}


# ── what-is-dynamic-island-on-mac ───────────────────────────────────────────
DYN = {
    "de": {"title": "Gibt es Dynamic Island auf dem Mac? — NotchNest", "description": "Hat der Mac ein Dynamic Island wie das iPhone? Was macOS mit der Notch tut und nicht tut, und wie du Dynamic-Island-artige Funktionen auf dem Mac bekommst.",
           "og_title": "Gibt es Dynamic Island auf dem Mac?", "og_desc": "Notch vs. Dynamic Island — und wie du das Erlebnis trotzdem bekommst.",
           "jsonld_headline": "Gibt es Dynamic Island auf dem Mac?", "jsonld_desc": "Der Unterschied zwischen Mac-Notch und iPhone-Dynamic-Island, und wie man das Erlebnis auf den Mac holt.",
           "kicker": KICK["explainer"]["de"], "h1": "Gibt es Dynamic Island auf dem Mac?",
           "lede": "Der Mac hat eine Notch, aber kein eingebautes Dynamic Island. Hier der Unterschied — und wie du das Erlebnis trotzdem bekommst.",
           "readtime": READ5["de"], "crumb_this": "Dynamic Island auf dem Mac?",
           "faq": [("Hat der Mac ein Dynamic Island?", "Nicht eingebaut. Der Mac hat eine Notch, aber macOS platziert keine interaktive UI darin. Drittanbieter-Apps wie NotchNest fügen Dynamic-Island-artige Funktionen hinzu."),
                   ("Ist die Mac-Notch dasselbe wie Dynamic Island?", "Nein. Dynamic Island ist eine aktive, animierte iPhone-UI für Live-Aktivitäten. Die Mac-Notch ist eine passive Hardware-Aussparung für die Kamera ohne eingebaute Interaktivität."),
                   ("Wie bekomme ich Dynamic-Island-Funktionen auf meinem MacBook?", "Installiere eine Notch-App wie NotchNest, die die Notch in ein Hover-Panel für Kalender, Zwischenablage, Notizen, Musik, Pomodoro und AirDrop verwandelt."),
                   ("Fügt Apple Dynamic Island zu macOS hinzu?", "Es gibt keinen angekündigten Plan. Vorerst sind Drittanbieter-Apps der einzige Weg, die Mac-Notch interaktiv zu machen.")],
           "body": """<p>Das Dynamic Island des iPhones verwandelt die Kamera-Aussparung in eine lebendige UI für Timer, Musik, Anrufe und Live-Aktivitäten. Viele Mac-Besitzer fragen: Macht macOS dasselbe mit seiner Notch? Standardmäßig nicht — aber du kannst es hinzufügen.</p>
    <h2>Notch vs. Dynamic Island</h2>
    <ul>
      <li><strong>iPhone Dynamic Island</strong> — eine aktive, animierte Software-UI, die Live-Aktivitäten hostet und sich bei Berührung ausdehnt.</li>
      <li><strong>Mac-Notch</strong> — eine passive Hardware-Aussparung. macOS zeichnet die Menüleiste um sie und zeigt einen grünen Kamera-Punkt. Keine interaktive UI.</li>
    </ul>
    <p>Ab Werk ist die Mac-Notch also nur ein Loch für die Kamera. Siehe „Macht die Mac-Notch überhaupt etwas" für die volle Aufschlüsselung.</p>
    <h2>Warum hat Apple keines hinzugefügt?</h2>
    <p>Das Cursor-Modell unterscheidet sich von Touch, Auffindbarkeit ist ohne sichtbaren Hinweis schwerer, und die Notch existiert nur auf dem eingebauten Display. Wie auch immer der Grund — Apple liefert Stand macOS Tahoe keine Notch-UI.</p>
    <h2>Wie du Dynamic Island auf den Mac holst</h2>
    <p>Drittanbieter-Apps füllen die Lücke. NotchNest umhüllt die Notch mit einem hover-aktivierten Panel — Kalender, KI-Zwischenablage, Schnellnotizen, Pomodoro, Musiksteuerung und Drag-to-AirDrop — das Nächste an einem Mac-Dynamic-Island, plus viel mehr. Erst fühlen? Öffne den interaktiven Notch-Playground im Browser. Andere Apps fokussieren speziell auf medienartige Animationen; siehe unseren Vergleich NotchNest vs. Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Mach deine Notch nützlich</h3><p>NotchNest bringt zehn Tools in die Notch deines MacBooks. Kostenlos im Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>""",
           "related": _related("de", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Englisch — die Antwort."))},
    "zh": {"title": "Mac 上有灵动岛吗？— NotchNest", "description": "Mac 有没有像 iPhone 那样的灵动岛？macOS 对刘海做什么、不做什么，以及如何在 Mac 上获得灵动岛式功能。",
           "og_title": "Mac 上有灵动岛吗？", "og_desc": "刘海对比灵动岛——以及如何照样获得这种体验。",
           "jsonld_headline": "Mac 上有灵动岛吗？", "jsonld_desc": "Mac 刘海与 iPhone 灵动岛的区别，以及如何在 Mac 上获得该体验。",
           "kicker": KICK["explainer"]["zh"], "h1": "Mac 上有灵动岛吗？",
           "lede": "Mac 有刘海，但没有内建灵动岛。这里讲清区别——以及如何照样获得那种体验。",
           "readtime": READ5["zh"], "crumb_this": "Mac 上有灵动岛吗？",
           "faq": [("Mac 有灵动岛吗？", "没有内建。Mac 有刘海，但 macOS 不在其中放置交互界面。NotchNest 之类的第三方应用可加入灵动岛式功能。"),
                   ("Mac 刘海和灵动岛是一回事吗？", "不是。灵动岛是 iPhone 上用于实时活动的主动动画界面。Mac 刘海是容纳摄像头的被动硬件缺口，没有内建交互。"),
                   ("如何在我的 MacBook 上获得灵动岛功能？", "安装 NotchNest 这样的刘海应用，把刘海变成日历、剪贴板、笔记、音乐、番茄钟和 AirDrop 的悬停面板。"),
                   ("Apple 会给 macOS 加灵动岛吗？", "没有已公布的计划。目前第三方应用是让 Mac 刘海可交互的唯一途径。")],
           "body": """<p>iPhone 的灵动岛把摄像头缺口变成计时器、音乐、通话和实时活动的活界面。很多 Mac 用户会问：macOS 对刘海也这么做吗？默认不会——但你可以加上。</p>
    <h2>刘海对比灵动岛</h2>
    <ul>
      <li><strong>iPhone 灵动岛</strong>——主动、有动画的软件界面，承载实时活动并在触摸时展开。</li>
      <li><strong>Mac 刘海</strong>——被动的硬件缺口。macOS 在其周围绘制菜单栏并显示绿色摄像头点。没有交互界面。</li>
    </ul>
    <p>所以开箱即用时，Mac 刘海只是摄像头的一个洞。完整拆解参见“Mac 刘海到底有没有用”。</p>
    <h2>Apple 为何没加？</h2>
    <p>光标模型不同于触摸，没有屏上提示则更难被发现，而且刘海只存在于内建屏幕上。无论原因如何，截至 macOS Tahoe，Apple 未提供任何刘海界面。</p>
    <h2>如何在 Mac 上获得灵动岛</h2>
    <p>第三方应用填补了空缺。NotchNest 用悬停触发面板包裹刘海——日历、AI 剪贴板、快速笔记、番茄钟、音乐控制和拖拽 AirDrop——这是最接近 Mac 灵动岛的东西，还远不止。想先感受？在浏览器里打开交互式刘海演示。其他应用则专注媒体式动画；参见我们的 NotchNest 对比 Boring Notch。</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>让你的刘海有用</h3><p>NotchNest 把十个工具放进 MacBook 刘海。在 Mac App Store 免费。</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>""",
           "related": _related("zh", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "英文——答案。"))},
    "ar": {"title": "هل يوجد Dynamic Island على الماك؟ — NotchNest", "description": "هل يملك الماك Dynamic Island مثل الآيفون؟ ما يفعله macOS وما لا يفعله بالنتش، وكيف تحصل على ميزات بأسلوب Dynamic Island على الماك.",
           "og_title": "هل يوجد Dynamic Island على الماك؟", "og_desc": "النتش مقابل Dynamic Island — وكيف تحصل على التجربة رغم ذلك.",
           "jsonld_headline": "هل يوجد Dynamic Island على الماك؟", "jsonld_desc": "الفرق بين نتش الماك وDynamic Island في الآيفون، وكيف تجلب التجربة إلى الماك.",
           "kicker": KICK["explainer"]["ar"], "h1": "هل يوجد Dynamic Island على الماك؟",
           "lede": "يملك الماك نتشًا لكن بلا Dynamic Island مدمج. إليك الفرق — وكيف تحصل على التجربة رغم ذلك.",
           "readtime": READ5["ar"], "crumb_this": "Dynamic Island على الماك؟",
           "faq": [("هل يملك الماك Dynamic Island؟", "ليس مدمجًا. يملك الماك نتشًا لكن macOS لا يضع فيه واجهة تفاعلية. تطبيقات الطرف الثالث مثل NotchNest تضيف وظائف بأسلوب Dynamic Island."),
                   ("هل نتش الماك هو نفسه Dynamic Island؟", "لا. Dynamic Island واجهة آيفون نشطة متحركة للأنشطة المباشرة. أما نتش الماك ففتحة عتاد سلبية للكاميرا بلا تفاعل مدمج."),
                   ("كيف أحصل على ميزات Dynamic Island على الماك بوك؟", "ثبّت تطبيق نتش مثل NotchNest يحوّل النتش إلى لوحة تمرير للتقويم والحافظة والملاحظات والموسيقى وبومودورو وAirDrop."),
                   ("هل ستضيف Apple ‏Dynamic Island إلى macOS؟", "لا خطة معلنة. حاليًا تطبيقات الطرف الثالث هي الطريق الوحيد لجعل نتش الماك تفاعليًا.")],
           "body": """<p>يحوّل Dynamic Island في الآيفون فتحة الكاميرا إلى واجهة حية للمؤقتات والموسيقى والمكالمات والأنشطة المباشرة. يسأل كثير من مالكي الماك: هل يفعل macOS الشيء نفسه بنتشه؟ ليس افتراضيًا — لكن يمكنك إضافته.</p>
    <h2>النتش مقابل Dynamic Island</h2>
    <ul>
      <li><strong>Dynamic Island في الآيفون</strong> — واجهة برمجية نشطة متحركة تستضيف الأنشطة المباشرة وتتوسّع عند اللمس.</li>
      <li><strong>نتش الماك</strong> — فتحة عتاد سلبية. يرسم macOS شريط القوائم حولها ويُظهر نقطة كاميرا خضراء. لا واجهة تفاعلية.</li>
    </ul>
    <p>فجاهزًا من العلبة، نتش الماك مجرد ثقب للكاميرا. راجع «هل يفعل نتش الماك شيئًا» للتفصيل الكامل.</p>
    <h2>لماذا لم تضفه Apple؟</h2>
    <p>نموذج المؤشر يختلف عن اللمس، والاكتشاف أصعب دون إشارة على الشاشة، والنتش موجود فقط على الشاشة المدمجة. أيًّا كان السبب، لا تقدّم Apple أي واجهة نتش حتى macOS Tahoe.</p>
    <h2>كيف تجلب Dynamic Island إلى الماك</h2>
    <p>تملأ تطبيقات الطرف الثالث الفراغ. يغلّف NotchNest النتش بلوحة تُفعَّل بالتمرير — تقويم وحافظة بالذكاء الاصطناعي وملاحظات سريعة وبومودورو والتحكم بالموسيقى والسحب إلى AirDrop — وهو أقرب شيء إلى Dynamic Island للماك، وأكثر بكثير. تريد أن تجرّبه أولًا؟ افتح عرض النتش التفاعلي في متصفحك. تركّز تطبيقات أخرى على رسوم بأسلوب الوسائط تحديدًا؛ راجع مقارنتنا NotchNest في مواجهة Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>اجعل نتشك مفيدًا</h3><p>يضع NotchNest عشر أدوات في نتش الماك بوك. مجانًا على Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>""",
           "related": _related("ar", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "إنجليزي — الجواب."))},
    "fr": {"title": "Y a-t-il un Dynamic Island sur Mac ? — NotchNest", "description": "Le Mac a-t-il un Dynamic Island comme l'iPhone ? Ce que macOS fait et ne fait pas avec l'encoche, et comment obtenir des fonctions façon Dynamic Island sur Mac.",
           "og_title": "Y a-t-il un Dynamic Island sur Mac ?", "og_desc": "Encoche vs Dynamic Island — et comment obtenir l'expérience quand même.",
           "jsonld_headline": "Y a-t-il un Dynamic Island sur Mac ?", "jsonld_desc": "La différence entre l'encoche du Mac et le Dynamic Island de l'iPhone, et comment amener l'expérience sur Mac.",
           "kicker": KICK["explainer"]["fr"], "h1": "Y a-t-il un Dynamic Island sur Mac ?",
           "lede": "Le Mac a une encoche mais pas de Dynamic Island intégré. Voici la différence — et comment obtenir l'expérience quand même.",
           "readtime": READ5["fr"], "crumb_this": "Dynamic Island sur Mac ?",
           "faq": [("Le Mac a-t-il un Dynamic Island ?", "Pas en natif. Le Mac a une encoche mais macOS n'y met aucune interface interactive. Des apps tierces comme NotchNest ajoutent des fonctions façon Dynamic Island."),
                   ("L'encoche du Mac est-elle la même chose que Dynamic Island ?", "Non. Dynamic Island est une interface iPhone active et animée pour les activités en direct. L'encoche du Mac est une découpe matérielle passive pour la caméra, sans interactivité intégrée."),
                   ("Comment obtenir les fonctions Dynamic Island sur mon MacBook ?", "Installez une app d'encoche comme NotchNest, qui transforme l'encoche en panneau au survol pour calendrier, presse-papiers, notes, musique, Pomodoro et AirDrop."),
                   ("Apple ajoutera-t-il Dynamic Island à macOS ?", "Aucun plan annoncé. Pour l'instant, les apps tierces sont le seul moyen de rendre l'encoche du Mac interactive.")],
           "body": """<p>Le Dynamic Island de l'iPhone transforme la découpe de la caméra en interface vivante pour minuteurs, musique, appels et activités en direct. Beaucoup de propriétaires de Mac demandent : macOS fait-il de même avec son encoche ? Pas par défaut — mais vous pouvez l'ajouter.</p>
    <h2>Encoche vs Dynamic Island</h2>
    <ul>
      <li><strong>Dynamic Island iPhone</strong> — une interface logicielle active et animée qui héberge les activités en direct et se déploie au toucher.</li>
      <li><strong>Encoche du Mac</strong> — une découpe matérielle passive. macOS dessine la barre des menus autour et affiche un point vert de caméra. Aucune interface interactive.</li>
    </ul>
    <p>Donc d'origine, l'encoche du Mac n'est qu'un trou pour la caméra. Voyez « l'encoche du Mac sert-elle vraiment à quelque chose » pour le détail complet.</p>
    <h2>Pourquoi Apple n'en a-t-il pas ajouté ?</h2>
    <p>Le modèle du curseur diffère du toucher, la découvrabilité est plus difficile sans repère à l'écran, et l'encoche n'existe que sur l'écran intégré. Quelle que soit la raison, Apple ne livre aucune interface d'encoche jusqu'à macOS Tahoe.</p>
    <h2>Comment obtenir Dynamic Island sur Mac</h2>
    <p>Les apps tierces comblent le vide. NotchNest entoure l'encoche d'un panneau activé au survol — calendrier, presse-papiers IA, notes rapides, Pomodoro, contrôle de la musique et glisser-vers-AirDrop — ce qui est le plus proche d'un Dynamic Island Mac, et bien plus. Envie de l'essayer d'abord ? Ouvrez le terrain de jeu interactif de l'encoche dans votre navigateur. D'autres apps se concentrent sur les animations façon média ; voyez notre comparatif NotchNest vs Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Rendez votre encoche utile</h3><p>NotchNest met dix outils dans l'encoche de votre MacBook. Gratuit sur le Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>""",
           "related": _related("fr", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Anglais — la réponse."))},
    "pt-BR": {"title": "Existe Dynamic Island no Mac? — NotchNest", "description": "O Mac tem Dynamic Island como o iPhone? O que o macOS faz e não faz com o notch, e como ter recursos estilo Dynamic Island no Mac.",
              "og_title": "Existe Dynamic Island no Mac?", "og_desc": "Notch vs Dynamic Island — e como ter a experiência mesmo assim.",
              "jsonld_headline": "Existe Dynamic Island no Mac?", "jsonld_desc": "A diferença entre o notch do Mac e o Dynamic Island do iPhone, e como trazer a experiência ao Mac.",
              "kicker": KICK["explainer"]["pt-BR"], "h1": "Existe Dynamic Island no Mac?",
              "lede": "O Mac tem notch, mas não tem Dynamic Island embutido. Aqui está a diferença — e como ter a experiência mesmo assim.",
              "readtime": READ5["pt-BR"], "crumb_this": "Dynamic Island no Mac?",
              "faq": [("O Mac tem Dynamic Island?", "Não de fábrica. O Mac tem notch, mas o macOS não coloca nenhuma interface interativa nele. Apps de terceiros como o NotchNest adicionam funcionalidades estilo Dynamic Island."),
                      ("O notch do Mac é o mesmo que o Dynamic Island?", "Não. O Dynamic Island é uma interface ativa e animada do iPhone para Atividades ao Vivo. O notch do Mac é um recorte de hardware passivo para a câmera, sem interatividade embutida."),
                      ("Como ter recursos do Dynamic Island no meu MacBook?", "Instale um app de notch como o NotchNest, que transforma o notch em um painel ao passar o cursor para calendário, área de transferência, notas, música, Pomodoro e AirDrop."),
                      ("A Apple vai adicionar Dynamic Island ao macOS?", "Não há plano anunciado. Por ora, apps de terceiros são a única forma de tornar o notch do Mac interativo.")],
              "body": """<p>O Dynamic Island do iPhone transforma o recorte da câmera em uma interface viva para timers, música, chamadas e Atividades ao Vivo. Muitos donos de Mac perguntam: o macOS faz o mesmo com o notch? Não por padrão — mas você pode adicionar.</p>
    <h2>Notch vs Dynamic Island</h2>
    <ul>
      <li><strong>Dynamic Island do iPhone</strong> — uma interface de software ativa e animada que hospeda Atividades ao Vivo e se expande ao toque.</li>
      <li><strong>Notch do Mac</strong> — um recorte de hardware passivo. O macOS desenha a barra de menus ao redor e mostra um ponto verde de câmera. Nenhuma interface interativa.</li>
    </ul>
    <p>Então, de fábrica, o notch do Mac é só um buraco para a câmera. Veja "o notch do Mac faz alguma coisa" para o detalhamento completo.</p>
    <h2>Por que a Apple não adicionou um?</h2>
    <p>O modelo do cursor difere do toque, a descoberta é mais difícil sem uma indicação na tela, e o notch só existe na tela embutida. Seja qual for o motivo, a Apple não entrega nenhuma interface de notch até o macOS Tahoe.</p>
    <h2>Como ter Dynamic Island no Mac</h2>
    <p>Apps de terceiros preenchem a lacuna. O NotchNest envolve o notch em um painel ativado ao passar o cursor — calendário, área de transferência com IA, notas rápidas, Pomodoro, controles de música e arrastar para AirDrop — o mais próximo de um Dynamic Island no Mac, e muito mais. Quer sentir primeiro? Abra o playground interativo do notch no navegador. Outros apps focam em animações estilo mídia especificamente; veja o comparativo NotchNest vs Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Grátis na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-BR", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglês — a resposta."))},
    "pt-PT": {"title": "Existe Dynamic Island no Mac? — NotchNest", "description": "O Mac tem Dynamic Island como o iPhone? O que o macOS faz e não faz com o notch, e como ter funcionalidades ao estilo Dynamic Island no Mac.",
              "og_title": "Existe Dynamic Island no Mac?", "og_desc": "Notch vs Dynamic Island — e como ter a experiência mesmo assim.",
              "jsonld_headline": "Existe Dynamic Island no Mac?", "jsonld_desc": "A diferença entre o notch do Mac e o Dynamic Island do iPhone, e como trazer a experiência ao Mac.",
              "kicker": KICK["explainer"]["pt-PT"], "h1": "Existe Dynamic Island no Mac?",
              "lede": "O Mac tem notch, mas não tem Dynamic Island integrado. Aqui está a diferença — e como ter a experiência mesmo assim.",
              "readtime": READ5["pt-PT"], "crumb_this": "Dynamic Island no Mac?",
              "faq": [("O Mac tem Dynamic Island?", "Não de origem. O Mac tem notch, mas o macOS não coloca nenhuma interface interativa nele. Apps de terceiros como o NotchNest adicionam funcionalidades ao estilo Dynamic Island."),
                      ("O notch do Mac é o mesmo que o Dynamic Island?", "Não. O Dynamic Island é uma interface ativa e animada do iPhone para Atividades Live. O notch do Mac é um recorte de hardware passivo para a câmara, sem interatividade integrada."),
                      ("Como ter funcionalidades do Dynamic Island no meu MacBook?", "Instale uma app de notch como o NotchNest, que transforma o notch num painel ao passar o cursor para calendário, área de transferência, notas, música, Pomodoro e AirDrop."),
                      ("A Apple vai adicionar Dynamic Island ao macOS?", "Não há plano anunciado. Por agora, as apps de terceiros são a única forma de tornar o notch do Mac interativo.")],
              "body": """<p>O Dynamic Island do iPhone transforma o recorte da câmara numa interface viva para temporizadores, música, chamadas e Atividades Live. Muitos donos de Mac perguntam: o macOS faz o mesmo com o notch? Não por predefinição — mas pode adicionar.</p>
    <h2>Notch vs Dynamic Island</h2>
    <ul>
      <li><strong>Dynamic Island do iPhone</strong> — uma interface de software ativa e animada que aloja Atividades Live e se expande ao toque.</li>
      <li><strong>Notch do Mac</strong> — um recorte de hardware passivo. O macOS desenha a barra de menus à volta e mostra um ponto verde de câmara. Nenhuma interface interativa.</li>
    </ul>
    <p>Então, de origem, o notch do Mac é só um buraco para a câmara. Veja "o notch do Mac faz alguma coisa" para o detalhe completo.</p>
    <h2>Porque não adicionou a Apple um?</h2>
    <p>O modelo do cursor difere do toque, a descoberta é mais difícil sem uma indicação no ecrã, e o notch só existe no ecrã integrado. Seja qual for a razão, a Apple não entrega nenhuma interface de notch até ao macOS Tahoe.</p>
    <h2>Como ter Dynamic Island no Mac</h2>
    <p>As apps de terceiros preenchem a lacuna. O NotchNest envolve o notch num painel ativado ao passar o cursor — calendário, área de transferência com IA, notas rápidas, Pomodoro, controlos de música e arrastar para AirDrop — o mais próximo de um Dynamic Island no Mac, e muito mais. Quer experimentar primeiro? Abra o playground interativo do notch no navegador. Outras apps focam-se em animações ao estilo multimédia especificamente; veja a comparação NotchNest vs Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne o seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Gratuito na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-PT", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglês — a resposta."))},
    "es-MX": {"title": "¿Hay Dynamic Island en Mac? — NotchNest", "description": "¿El Mac tiene Dynamic Island como el iPhone? Qué hace y qué no hace macOS con el notch, y cómo obtener funciones estilo Dynamic Island en Mac.",
              "og_title": "¿Hay Dynamic Island en Mac?", "og_desc": "Notch vs Dynamic Island — y cómo obtener la experiencia de todos modos.",
              "jsonld_headline": "¿Hay Dynamic Island en Mac?", "jsonld_desc": "La diferencia entre el notch del Mac y el Dynamic Island del iPhone, y cómo traer la experiencia al Mac.",
              "kicker": KICK["explainer"]["es-MX"], "h1": "¿Hay Dynamic Island en Mac?",
              "lede": "El Mac tiene notch, pero no un Dynamic Island integrado. Aquí está la diferencia — y cómo obtener la experiencia de todos modos.",
              "readtime": READ5["es-MX"], "crumb_this": "¿Dynamic Island en Mac?",
              "faq": [("¿El Mac tiene Dynamic Island?", "No de forma integrada. El Mac tiene notch, pero macOS no coloca ninguna interfaz interactiva en él. Apps de terceros como NotchNest agregan funciones estilo Dynamic Island."),
                      ("¿El notch del Mac es lo mismo que el Dynamic Island?", "No. El Dynamic Island es una interfaz activa y animada del iPhone para Actividades en Vivo. El notch del Mac es un recorte de hardware pasivo para la cámara, sin interactividad integrada."),
                      ("¿Cómo obtengo funciones de Dynamic Island en mi MacBook?", "Instala una app de notch como NotchNest, que convierte el notch en un panel al pasar el cursor para calendario, portapapeles, notas, música, Pomodoro y AirDrop."),
                      ("¿Apple agregará Dynamic Island a macOS?", "No hay plan anunciado. Por ahora, las apps de terceros son la única forma de hacer interactivo el notch del Mac.")],
              "body": """<p>El Dynamic Island del iPhone convierte el recorte de la cámara en una interfaz viva para temporizadores, música, llamadas y Actividades en Vivo. Muchos dueños de Mac preguntan: ¿macOS hace lo mismo con su notch? No por defecto — pero puedes agregarlo.</p>
    <h2>Notch vs Dynamic Island</h2>
    <ul>
      <li><strong>Dynamic Island del iPhone</strong> — una interfaz de software activa y animada que aloja Actividades en Vivo y se expande al tocar.</li>
      <li><strong>Notch del Mac</strong> — un recorte de hardware pasivo. macOS dibuja la barra de menús alrededor y muestra un punto verde de cámara. Ninguna interfaz interactiva.</li>
    </ul>
    <p>Así que de fábrica, el notch del Mac es solo un hueco para la cámara. Mira "¿el notch del Mac hace algo?" para el desglose completo.</p>
    <h2>¿Por qué Apple no agregó uno?</h2>
    <p>El modelo del cursor difiere del toque, la descubribilidad es más difícil sin una señal en pantalla, y el notch solo existe en la pantalla integrada. Sea cual sea la razón, Apple no entrega ninguna interfaz de notch hasta macOS Tahoe.</p>
    <h2>Cómo obtener Dynamic Island en Mac</h2>
    <p>Las apps de terceros llenan el vacío. NotchNest envuelve el notch en un panel activado al pasar el cursor — calendario, portapapeles con IA, notas rápidas, Pomodoro, controles de música y arrastrar a AirDrop — lo más cercano a un Dynamic Island de Mac, y mucho más. ¿Quieres sentirlo primero? Abre el playground interactivo del notch en tu navegador. Otras apps se enfocan en animaciones estilo medios específicamente; mira nuestra comparativa NotchNest vs Boring Notch.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Haz útil tu notch</h3><p>NotchNest pone diez herramientas en el notch de tu MacBook. Gratis en el Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>""",
              "related": _related("es-MX", ("/learn/does-the-mac-notch-actually-do-anything/", "Does the Mac notch actually do anything?", "Inglés — la respuesta."))},
}


# ── drop-files-into-macbook-notch ───────────────────────────────────────────
DROP = {
    "de": {"title": "Dateien in die MacBook-Notch ziehen — NotchNest", "description": "Mach die Notch zum Drag-and-Drop-Regal — MacBook-Notch-Dateidrop für sofortiges AirDrop, ein Zwischenlager und schnelles Teilen ohne Finder-Fenster.",
           "og_title": "Dateien in die MacBook-Notch ziehen", "og_desc": "So funktioniert der Notch-Dateidrop — und warum er schneller ist als Finder.",
           "jsonld_headline": "Dateien in die MacBook-Notch ziehen", "jsonld_desc": "Wie MacBook-Notch-Dateidrop für AirDrop, Zwischenlager und schnelles Teilen funktioniert.",
           "kicker": KICK["guide"]["de"], "h1": "Dateien in die MacBook-Notch ziehen",
           "lede": "Die Notch fängt Dateien, die du auf sie ziehst — ein Tray für AirDrop und schnelles Teilen. So funktioniert der MacBook-Notch-Dateidrop und warum er schneller ist als Finder.",
           "readtime": READ5["de"], "crumb_this": "Dateidrop in die Notch",
           "faq": [("Kann man Dateien auf die MacBook-Notch ziehen?", "Ja, mit einer Notch-App wie NotchNest. Eine Datei auf die Notch zu ziehen öffnet ein Tray für AirDrop, ein Zwischenlager oder das Teilen-Menü."),
                   ("Ist Notch-Dateidrop schneller als AirDrop aus dem Finder?", "Meist. Die Notch ist ein fester Punkt oben in der Mitte jedes Bildschirms — kein Fensterwechsel, kein Rechtsklick-Menü. Rauf ziehen und loslassen."),
                   ("Behält das Notch-Tray meine Dateien?", "Das Datei-Tray hält zuletzt verwendete Dateien, damit du sie aus jeder App wieder greifst. Nichts wird hochgeladen; Dateien bleiben lokal auf deinem Mac."),
                   ("Welche Macs unterstützen Notch-Dateidrop?", "Jedes MacBook mit Notch — MacBook Pro ab 2021 und MacBook Air ab 2022 — mit macOS 14 oder neuer und installiertem NotchNest.")],
           "body": """<p>Eine Datei zum Teilen zu ziehen bedeutet meist, Finder-Fenster oder das Teilen-Menü zu jonglieren. MacBook-Notch-Dateidrop ersetzt das: Du ziehst eine Datei auf die Notch, und sie wird zum Startpunkt für AirDrop, zu einem Zwischenlager oder einer Schnellaktion.</p>
    <h2>So funktioniert der Notch-Dateidrop</h2>
    <p>Läuft NotchNest, wird die Notch zum Drop-Ziel. Nimm eine beliebige Datei — aus Finder, vom Schreibtisch oder aus einer App — zieh sie auf die Notch, und ein Tray öffnet sich:</p>
    <ul>
      <li><strong>AirDrop</strong> — auf einem nahen Gerät loslassen, um sofort zu senden.</li>
      <li><strong>Datei-Tray</strong> — Dateien dort parken und später aus jeder App wieder greifen.</li>
      <li><strong>Schnell teilen</strong> — ans Teilen-Menü übergeben, ohne es zu suchen.</li>
    </ul>
    <h2>Warum es den normalen Ablauf schlägt</h2>
    <p>Die Notch ist immer oben in der Mitte deines Bildschirms, also ein fester, vorhersehbarer Punkt, egal welche App vorne ist. Kein Fensterwechsel, keine Rechtsklick-Menüs. Rauf ziehen, ablegen, fertig. Das Zuletzt-Verwendet-Tray sorgt dafür, dass du nicht den Überblick verlierst.</p>
    <h2>Probier das Drop-Tray</h2>
    <p>Der Notch-Playground zeigt das Aufklapp-Tray, damit du die Drop-Zone vor der Installation siehst.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Mach deine Notch nützlich</h3><p>NotchNest bringt zehn Tools in die Notch deines MacBooks. Kostenlos im Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>""",
           "related": _related("de", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Übersicht 2026."))},
    "zh": {"title": "如何把文件拖进 MacBook 刘海 — NotchNest", "description": "把刘海变成拖放搁架——MacBook 刘海文件拖放，实现即时 AirDrop、暂存托盘和无需 Finder 窗口的快速分享。",
           "og_title": "如何把文件拖进 MacBook 刘海", "og_desc": "刘海文件拖放怎么用——以及为何比 Finder 更快。",
           "jsonld_headline": "如何把文件拖进 MacBook 刘海", "jsonld_desc": "MacBook 刘海文件拖放如何用于 AirDrop、暂存托盘和快速分享。",
           "kicker": KICK["guide"]["zh"], "h1": "如何把文件拖进 MacBook 刘海",
           "lede": "刘海能接住你拖上去的文件——一个用于 AirDrop 和快速分享的托盘。看看 MacBook 刘海文件拖放怎么用，以及为何比 Finder 更快。",
           "readtime": READ5["zh"], "crumb_this": "把文件拖进刘海",
           "faq": [("能把文件拖到 MacBook 刘海上吗？", "能，配合 NotchNest 这样的刘海应用。把文件拖到刘海会打开一个用于 AirDrop、暂存搁架或分享菜单的托盘。"),
                   ("刘海文件拖放比从 Finder 用 AirDrop 更快吗？", "通常是。刘海是每块屏幕顶部居中的固定目标，无需切窗、无需右键菜单——往上拖，松手即可。"),
                   ("刘海托盘会保留我的文件吗？", "文件托盘保留最近文件，你可从任意应用再取。什么都不会上传；文件留在你的 Mac 本地。"),
                   ("哪些 Mac 支持刘海文件拖放？", "任何带刘海的 MacBook——2021 年起的 MacBook Pro 与 2022 年起的 MacBook Air——运行 macOS 14 或更新并安装 NotchNest。")],
           "body": """<p>拖一个文件去分享，通常意味着在 Finder 窗口或分享菜单间来回折腾。MacBook 刘海文件拖放取而代之：你把文件拖到刘海，它便成为 AirDrop 的起点、一个暂存托盘或一个快捷操作。</p>
    <h2>刘海文件拖放怎么用</h2>
    <p>运行 NotchNest 后，刘海成为放置目标。拿起任意文件——来自 Finder、桌面或某个应用——拖到刘海，托盘随即打开：</p>
    <ul>
      <li><strong>AirDrop</strong>——松手落在附近设备上即刻发送。</li>
      <li><strong>文件托盘</strong>——把文件停在那里，稍后从任意应用再取。</li>
      <li><strong>快速分享</strong>——交给分享菜单，无需翻找。</li>
    </ul>
    <h2>它为何胜过常规流程</h2>
    <p>刘海始终在屏幕顶部居中，因此无论哪个应用在前台，它都是固定、可预期的目标。无需切换窗口，无需右键菜单。往上拖、放下、搞定。最近文件托盘让你不会弄丢刚移动的东西。</p>
    <h2>试试拖放托盘</h2>
    <p>刘海演示会展示悬停展开的托盘，让你在安装前就看到放置区。</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>让你的刘海有用</h3><p>NotchNest 把十个工具放进 MacBook 刘海。在 Mac App Store 免费。</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>""",
           "related": _related("zh", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "英文——2026 盘点。"))},
    "ar": {"title": "كيفية إفلات الملفات في نتش الماك بوك — NotchNest", "description": "حوّل النتش إلى رفّ سحب وإفلات — إفلات ملفات نتش الماك بوك لـ AirDrop فوري ودرج تخزين ومشاركة سريعة بلا نافذة Finder.",
           "og_title": "كيفية إفلات الملفات في نتش الماك بوك", "og_desc": "كيف يعمل إفلات ملفات النتش — ولماذا هو أسرع من Finder.",
           "jsonld_headline": "كيفية إفلات الملفات في نتش الماك بوك", "jsonld_desc": "كيف يعمل إفلات ملفات نتش الماك بوك لـ AirDrop ودرج التخزين والمشاركة السريعة.",
           "kicker": KICK["guide"]["ar"], "h1": "كيفية إفلات الملفات في نتش الماك بوك",
           "lede": "يلتقط النتش الملفات التي تسحبها إليه — درج لـ AirDrop والمشاركة السريعة. إليك كيف يعمل إفلات ملفات نتش الماك بوك ولماذا هو أسرع من Finder.",
           "readtime": READ5["ar"], "crumb_this": "إفلات الملفات في النتش",
           "faq": [("هل يمكن سحب الملفات إلى نتش الماك بوك؟", "نعم، بتطبيق نتش مثل NotchNest. سحب ملف إلى النتش يفتح درجًا لـ AirDrop أو رفّ تخزين أو قائمة المشاركة."),
                   ("هل إفلات ملفات النتش أسرع من AirDrop من Finder؟", "عادةً. النتش هدف ثابت أعلى منتصف كل شاشة، فلا تبديل نوافذ ولا قائمة نقر يمين — اسحب لأعلى وأفلت."),
                   ("هل يحتفظ درج النتش بملفاتي؟", "يحتفظ درج الملفات بالأخيرة لتأخذها من أي تطبيق. لا يُرفع شيء؛ تبقى الملفات محليًا على جهاز الماك."),
                   ("أي أجهزة ماك تدعم إفلات ملفات النتش؟", "أي ماك بوك بنتش — MacBook Pro من 2021 وMacBook Air من 2022 — يعمل بـ macOS 14 أو أحدث مع تثبيت NotchNest.")],
           "body": """<p>سحب ملف لمشاركته يعني عادةً التنقّل بين نوافذ Finder أو قائمة المشاركة. يحلّ إفلات ملفات نتش الماك بوك محلّ ذلك: تسحب ملفًا إلى النتش فيصبح نقطة انطلاق لـ AirDrop أو درج تخزين أو إجراء سريع.</p>
    <h2>كيف يعمل إفلات ملفات النتش</h2>
    <p>مع تشغيل NotchNest، يصبح النتش هدف إفلات. التقط أي ملف — من Finder أو سطح المكتب أو تطبيق — واسحبه إلى النتش، فيفتح درج:</p>
    <ul>
      <li><strong>AirDrop</strong> — أفلت على جهاز قريب للإرسال فورًا.</li>
      <li><strong>درج الملفات</strong> — خزّن الملفات هناك واسحبها لاحقًا من أي تطبيق.</li>
      <li><strong>مشاركة سريعة</strong> — سلّم إلى قائمة المشاركة دون البحث عنها.</li>
    </ul>
    <h2>لماذا يتفوّق على المسار العادي</h2>
    <p>النتش دائمًا أعلى منتصف شاشتك، فهو هدف ثابت ومتوقّع أيًّا كان التطبيق الأمامي. لا تبديل نوافذ ولا قوائم نقر يمين. اسحب لأعلى، أفلت، انتهى. درج الملفات الأخيرة يمنعك من فقدان ما نقلته.</p>
    <h2>جرّب درج الإفلات</h2>
    <p>يعرض عرض النتش درج التوسّع بالتمرير لترى منطقة الإفلات قبل التثبيت.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>اجعل نتشك مفيدًا</h3><p>يضع NotchNest عشر أدوات في نتش الماك بوك. مجانًا على Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>""",
           "related": _related("ar", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "إنجليزي — اختيارات 2026."))},
    "fr": {"title": "Déposer des fichiers dans l'encoche du MacBook — NotchNest", "description": "Transformez l'encoche en étagère glisser-déposer — dépôt de fichiers pour AirDrop instantané, un bac de rétention et un partage rapide sans fenêtre Finder.",
           "og_title": "Déposer des fichiers dans l'encoche du MacBook", "og_desc": "Comment fonctionne le dépôt de fichiers dans l'encoche — et pourquoi c'est plus rapide que le Finder.",
           "jsonld_headline": "Déposer des fichiers dans l'encoche du MacBook", "jsonld_desc": "Comment le dépôt de fichiers dans l'encoche du MacBook fonctionne pour AirDrop, un bac de rétention et un partage rapide.",
           "kicker": KICK["guide"]["fr"], "h1": "Déposer des fichiers dans l'encoche du MacBook",
           "lede": "L'encoche attrape les fichiers que vous y glissez — un bac pour AirDrop et le partage rapide. Voici comment fonctionne le dépôt de fichiers dans l'encoche et pourquoi c'est plus rapide que le Finder.",
           "readtime": READ5["fr"], "crumb_this": "Dépôt de fichiers dans l'encoche",
           "faq": [("Peut-on glisser des fichiers sur l'encoche du MacBook ?", "Oui, avec une app d'encoche comme NotchNest. Glisser un fichier sur l'encoche ouvre un bac pour AirDrop, une étagère de rétention ou la feuille de partage."),
                   ("Le dépôt dans l'encoche est-il plus rapide qu'AirDrop depuis le Finder ?", "En général. L'encoche est une cible fixe en haut au centre de chaque écran — pas de changement de fenêtre, pas de menu clic droit. Glissez vers le haut et relâchez."),
                   ("Le bac de l'encoche conserve-t-il mes fichiers ?", "Le bac à fichiers garde les récents pour les reprendre depuis n'importe quelle app. Rien n'est envoyé ; les fichiers restent en local sur votre Mac."),
                   ("Quels Mac prennent en charge le dépôt dans l'encoche ?", "Tout MacBook à encoche — MacBook Pro depuis 2021 et MacBook Air depuis 2022 — sous macOS 14 ou plus récent avec NotchNest installé.")],
           "body": """<p>Glisser un fichier pour le partager signifie d'habitude jongler avec des fenêtres Finder ou la feuille de partage. Le dépôt de fichiers dans l'encoche du MacBook remplace cela : vous glissez un fichier sur l'encoche et elle devient un point de départ pour AirDrop, un bac de rétention ou une action rapide.</p>
    <h2>Comment fonctionne le dépôt dans l'encoche</h2>
    <p>Avec NotchNest lancé, l'encoche devient une cible de dépôt. Prenez n'importe quel fichier — du Finder, du Bureau ou d'une app — glissez-le vers l'encoche, et un bac s'ouvre :</p>
    <ul>
      <li><strong>AirDrop</strong> — relâchez sur un appareil proche pour envoyer instantanément.</li>
      <li><strong>Bac à fichiers</strong> — garez-y des fichiers et reprenez-les plus tard depuis n'importe quelle app.</li>
      <li><strong>Partage rapide</strong> — passez à la feuille de partage sans chercher le menu.</li>
    </ul>
    <h2>Pourquoi ça bat le flux normal</h2>
    <p>L'encoche est toujours en haut au centre de votre écran, donc une cible fixe et prévisible quelle que soit l'app au premier plan. Pas de changement de fenêtre, pas de menus clic droit. Glissez vers le haut, déposez, c'est fait. Le bac des fichiers récents évite de perdre le fil de ce que vous avez déplacé.</p>
    <h2>Essayez le bac de dépôt</h2>
    <p>Le terrain de jeu de l'encoche montre le bac qui se déploie au survol, pour voir la zone de dépôt avant d'installer.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Rendez votre encoche utile</h3><p>NotchNest met dix outils dans l'encoche de votre MacBook. Gratuit sur le Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>""",
           "related": _related("fr", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Anglais — sélection 2026."))},
    "pt-BR": {"title": "Como soltar arquivos no notch do MacBook — NotchNest", "description": "Transforme o notch em uma prateleira de arrastar e soltar — soltar arquivos no notch para AirDrop instantâneo, uma bandeja e compartilhamento rápido sem janela do Finder.",
              "og_title": "Como soltar arquivos no notch do MacBook", "og_desc": "Como funciona soltar arquivos no notch — e por que é mais rápido que o Finder.",
              "jsonld_headline": "Como soltar arquivos no notch do MacBook", "jsonld_desc": "Como soltar arquivos no notch do MacBook funciona para AirDrop, bandeja e compartilhamento rápido.",
              "kicker": KICK["guide"]["pt-BR"], "h1": "Como soltar arquivos no notch do MacBook",
              "lede": "O notch pega arquivos que você arrasta até ele — uma bandeja para AirDrop e compartilhamento rápido. Veja como soltar arquivos no notch funciona e por que é mais rápido que o Finder.",
              "readtime": READ5["pt-BR"], "crumb_this": "Soltar arquivos no notch",
              "faq": [("Dá para arrastar arquivos para o notch do MacBook?", "Sim, com um app de notch como o NotchNest. Arrastar um arquivo para o notch abre uma bandeja para AirDrop, uma prateleira ou a folha de compartilhamento."),
                      ("Soltar no notch é mais rápido que AirDrop pelo Finder?", "Geralmente. O notch é um alvo fixo no topo central de toda tela — sem troca de janela, sem menu de clique direito. Arraste para cima e solte."),
                      ("A bandeja do notch guarda meus arquivos?", "A bandeja de arquivos guarda os recentes para você pegá-los de qualquer app. Nada é enviado; os arquivos ficam locais no seu Mac."),
                      ("Quais Macs suportam soltar arquivos no notch?", "Qualquer MacBook com notch — MacBook Pro 2021+ e MacBook Air 2022+ — rodando macOS 14 ou mais recente com o NotchNest instalado.")],
              "body": """<p>Arrastar um arquivo para compartilhar normalmente significa fazer malabarismo com janelas do Finder ou a folha de compartilhamento. Soltar arquivos no notch do MacBook substitui isso: você arrasta um arquivo para o notch e ele vira um ponto de partida para AirDrop, uma bandeja ou uma ação rápida.</p>
    <h2>Como soltar arquivos no notch funciona</h2>
    <p>Com o NotchNest rodando, o notch vira um alvo de soltar. Pegue qualquer arquivo — do Finder, da Mesa ou de um app — arraste-o para o notch, e uma bandeja abre:</p>
    <ul>
      <li><strong>AirDrop</strong> — solte em um dispositivo próximo para enviar na hora.</li>
      <li><strong>Bandeja de arquivos</strong> — estacione arquivos ali e pegue-os depois de qualquer app.</li>
      <li><strong>Compartilhar rápido</strong> — entregue à folha de compartilhamento sem procurar o menu.</li>
    </ul>
    <h2>Por que supera o fluxo normal</h2>
    <p>O notch está sempre no topo central da sua tela, então é um alvo fixo e previsível não importa qual app está na frente. Sem troca de janela, sem menus de clique direito. Arraste para cima, solte, pronto. A bandeja de recentes evita que você perca o rastro do que moveu.</p>
    <h2>Teste a bandeja de soltar</h2>
    <p>O playground do notch demonstra a bandeja que expande ao passar o cursor, para você ver a zona de soltar antes de instalar.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Grátis na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-BR", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "pt-PT": {"title": "Como largar ficheiros no notch do MacBook — NotchNest", "description": "Transforme o notch numa prateleira de arrastar e largar — largar ficheiros no notch para AirDrop instantâneo, um tabuleiro e partilha rápida sem janela do Finder.",
              "og_title": "Como largar ficheiros no notch do MacBook", "og_desc": "Como funciona largar ficheiros no notch — e porque é mais rápido que o Finder.",
              "jsonld_headline": "Como largar ficheiros no notch do MacBook", "jsonld_desc": "Como largar ficheiros no notch do MacBook funciona para AirDrop, tabuleiro e partilha rápida.",
              "kicker": KICK["guide"]["pt-PT"], "h1": "Como largar ficheiros no notch do MacBook",
              "lede": "O notch apanha ficheiros que arrasta até ele — um tabuleiro para AirDrop e partilha rápida. Veja como largar ficheiros no notch funciona e porque é mais rápido que o Finder.",
              "readtime": READ5["pt-PT"], "crumb_this": "Largar ficheiros no notch",
              "faq": [("Dá para arrastar ficheiros para o notch do MacBook?", "Sim, com uma app de notch como o NotchNest. Arrastar um ficheiro para o notch abre um tabuleiro para AirDrop, uma prateleira ou a folha de partilha."),
                      ("Largar no notch é mais rápido que AirDrop pelo Finder?", "Geralmente. O notch é um alvo fixo no topo central de todos os ecrãs — sem troca de janela, sem menu de clique direito. Arraste para cima e largue."),
                      ("O tabuleiro do notch guarda os meus ficheiros?", "O tabuleiro de ficheiros guarda os recentes para os apanhar de qualquer app. Nada é enviado; os ficheiros ficam locais no seu Mac."),
                      ("Que Macs suportam largar ficheiros no notch?", "Qualquer MacBook com notch — MacBook Pro 2021+ e MacBook Air 2022+ — a correr macOS 14 ou mais recente com o NotchNest instalado.")],
              "body": """<p>Arrastar um ficheiro para partilhar significa normalmente fazer malabarismo com janelas do Finder ou a folha de partilha. Largar ficheiros no notch do MacBook substitui isso: arrasta um ficheiro para o notch e ele torna-se um ponto de partida para AirDrop, um tabuleiro ou uma ação rápida.</p>
    <h2>Como largar ficheiros no notch funciona</h2>
    <p>Com o NotchNest a correr, o notch torna-se um alvo de largar. Pegue em qualquer ficheiro — do Finder, da Secretária ou de uma app — arraste-o para o notch, e um tabuleiro abre:</p>
    <ul>
      <li><strong>AirDrop</strong> — largue num dispositivo próximo para enviar de imediato.</li>
      <li><strong>Tabuleiro de ficheiros</strong> — estacione ficheiros ali e apanhe-os depois de qualquer app.</li>
      <li><strong>Partilha rápida</strong> — entregue à folha de partilha sem procurar o menu.</li>
    </ul>
    <h2>Porque supera o fluxo normal</h2>
    <p>O notch está sempre no topo central do seu ecrã, por isso é um alvo fixo e previsível seja qual for a app à frente. Sem troca de janela, sem menus de clique direito. Arraste para cima, largue, pronto. O tabuleiro de recentes evita que perca o rasto do que moveu.</p>
    <h2>Experimente o tabuleiro de largar</h2>
    <p>O playground do notch demonstra o tabuleiro que expande ao passar o cursor, para ver a zona de largar antes de instalar.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne o seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Gratuito na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-PT", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglês — seleção 2026."))},
    "es-MX": {"title": "Cómo soltar archivos en el notch del MacBook — NotchNest", "description": "Convierte el notch en un estante de arrastrar y soltar — soltar archivos en el notch para AirDrop instantáneo, una bandeja y compartir rápido sin ventana del Finder.",
              "og_title": "Cómo soltar archivos en el notch del MacBook", "og_desc": "Cómo funciona soltar archivos en el notch — y por qué es más rápido que el Finder.",
              "jsonld_headline": "Cómo soltar archivos en el notch del MacBook", "jsonld_desc": "Cómo soltar archivos en el notch del MacBook funciona para AirDrop, bandeja y compartir rápido.",
              "kicker": KICK["guide"]["es-MX"], "h1": "Cómo soltar archivos en el notch del MacBook",
              "lede": "El notch atrapa archivos que arrastras hacia él — una bandeja para AirDrop y compartir rápido. Aquí cómo funciona soltar archivos en el notch y por qué es más rápido que el Finder.",
              "readtime": READ5["es-MX"], "crumb_this": "Soltar archivos en el notch",
              "faq": [("¿Se pueden arrastrar archivos al notch del MacBook?", "Sí, con una app de notch como NotchNest. Arrastrar un archivo al notch abre una bandeja para AirDrop, un estante o la hoja de compartir."),
                      ("¿Soltar en el notch es más rápido que AirDrop desde el Finder?", "Normalmente. El notch es un objetivo fijo en la parte superior central de cada pantalla — sin cambiar de ventana, sin menú de clic derecho. Arrastra hacia arriba y suelta."),
                      ("¿La bandeja del notch conserva mis archivos?", "La bandeja de archivos guarda los recientes para tomarlos desde cualquier app. Nada se sube; los archivos se quedan locales en tu Mac."),
                      ("¿Qué Macs admiten soltar archivos en el notch?", "Cualquier MacBook con notch — MacBook Pro 2021+ y MacBook Air 2022+ — con macOS 14 o posterior y NotchNest instalado.")],
              "body": """<p>Arrastrar un archivo para compartir suele significar hacer malabares con ventanas del Finder o la hoja de compartir. Soltar archivos en el notch del MacBook lo reemplaza: arrastras un archivo al notch y se convierte en un punto de partida para AirDrop, una bandeja o una acción rápida.</p>
    <h2>Cómo funciona soltar archivos en el notch</h2>
    <p>Con NotchNest en marcha, el notch se vuelve un objetivo para soltar. Toma cualquier archivo — del Finder, del Escritorio o de una app — arrástralo al notch, y se abre una bandeja:</p>
    <ul>
      <li><strong>AirDrop</strong> — suelta en un dispositivo cercano para enviar al instante.</li>
      <li><strong>Bandeja de archivos</strong> — estaciona archivos ahí y tómalos después desde cualquier app.</li>
      <li><strong>Compartir rápido</strong> — entrégalo a la hoja de compartir sin buscar el menú.</li>
    </ul>
    <h2>Por qué supera el flujo normal</h2>
    <p>El notch siempre está en la parte superior central de tu pantalla, así que es un objetivo fijo y predecible sin importar qué app esté al frente. Sin cambiar de ventana, sin menús de clic derecho. Arrastra hacia arriba, suelta, listo. La bandeja de recientes evita que pierdas el rastro de lo que moviste.</p>
    <h2>Prueba la bandeja de soltar</h2>
    <p>El playground del notch muestra la bandeja que se expande al pasar el cursor, para que veas la zona de soltar antes de instalar.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Haz útil tu notch</h3><p>NotchNest pone diez herramientas en el notch de tu MacBook. Gratis en el Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>""",
              "related": _related("es-MX", ("/learn/best-macos-notch-apps/", "Best macOS notch apps", "Inglés — selección 2026."))},
}


# ── notch-camera-on-mac ─────────────────────────────────────────────────────
CAMERA = {
    "de": {"title": "Die Notch-Kamera auf dem Mac — NotchNest", "description": "Alles über die Notch-Kamera auf dem Mac — die 1080p-Webcam in der Notch, wie du sie vorschaust und ein Notch-Kamera-Spiegel für schnelle Checks.",
           "og_title": "Die Notch-Kamera auf dem Mac", "og_desc": "Was die Notch-Kamera kann und wie du sie in der Notch spiegelst.",
           "jsonld_headline": "Die Notch-Kamera auf dem Mac", "jsonld_desc": "Die 1080p-Kamera in der Mac-Notch, wie man sie vorschaut und in der Notch spiegelt.",
           "kicker": KICK["explainer"]["de"], "h1": "Die Notch-Kamera auf dem Mac",
           "lede": "Die Notch existiert, um die Kamera deines MacBooks zu beherbergen. Hier, was diese Kamera kann, wie du sie vor einem Call prüfst und in der Notch selbst spiegelst.",
           "readtime": READ5["de"], "crumb_this": "Notch-Kamera",
           "faq": [("Welche Kamera steckt in der Mac-Notch?", "Eine 1080p-FaceTime-HD-Kamera plus der Umgebungslichtsensor. Center Stage wird auf neueren Modellen unterstützt."),
                   ("Wie sehe ich die Notch-Kamera vor einem Call?", "Öffne Photo Booth oder QuickTimes ‚Neue Videoaufnahme' für ein Live-Bild — oder nutze einen Notch-Kamera-Spiegel wie NotchNest, um sie per Hover vorzuschauen."),
                   ("Kann man die Mac-Kamera in der Notch spiegeln?", "Ja. NotchNests Kamera-Spiegel zeigt ein Live-Webcam-Bild in der Notch selbst, sodass du das Bild ohne separate App prüfst."),
                   ("Nimmt der Kamera-Spiegel etwas auf?", "Nein. Ein Spiegel zeigt dein eigenes Live-Bild lokal. Die grüne Datenschutz-LED leuchtet weiterhin per Hardware, sobald die Kamera an ist.")],
           "body": """<p>Der ganze Grund für die Notch ist die Kamera. Apple verkleinerte den Rand und schob die FaceTime-HD-Webcam in eine kleine Aussparung oben am Bildschirm. Das ist die Notch-Kamera auf dem Mac — und sie kann mehr als Videocalls.</p>
    <h2>Was die Notch-Kamera ist</h2>
    <p>Auf MacBook Pro (ab 2021) und MacBook Air (ab 2022) hält die Notch eine 1080p-FaceTime-HD-Kamera plus den Umgebungslichtsensor. Sie unterstützt Center Stage auf unterstützten Modellen und speist jede App, die deine Webcam nutzt.</p>
    <h2>So schaust du die Notch-Kamera schnell vor</h2>
    <p>Normalerweise siehst du dich erst, wenn du schon im Call bist. Um Bildausschnitt und Licht vorher zu prüfen, öffne Photo Booth oder QuickTime → Neue Videoaufnahme. Beide zeigen ein Live-Bild der Notch-Kamera.</p>
    <h2>Ein Notch-Kamera-Spiegel — check dich per Hover</h2>
    <p>Eine ganze App nur zum Sehen deines Gesichts zu öffnen ist umständlich. NotchNest hat einen Kamera-Spiegel in der Notch: Hover und ein Live-Webcam-Bild erscheint genau dort, wo die Kamera physisch sitzt. Richte deine Haare, prüf den Hintergrund, dann schließ es — kein Photo Booth, kein Extra-Fenster. Sieh es im Notch-Playground.</p>
    <h2>Privatsphäre</h2>
    <p>Die grüne LED neben der Notch-Kamera leuchtet, sobald die Kamera aktiv ist — sie ist fest verdrahtet und kann per Software nicht umgangen werden. Ein Notch-Spiegel zeigt nur dein eigenes Bild lokal; nichts wird aufgezeichnet oder gesendet.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Mach deine Notch nützlich</h3><p>NotchNest bringt zehn Tools in die Notch deines MacBooks. Kostenlos im Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Im Mac App Store laden" /></a>
    </div>""",
           "related": _related("de", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Englisch — Grundlagen."))},
    "zh": {"title": "Mac 上的刘海摄像头 — NotchNest", "description": "关于 Mac 刘海摄像头的一切——刘海里的 1080p 摄像头、如何预览，以及用于快速自查的刘海摄像头镜像。",
           "og_title": "Mac 上的刘海摄像头", "og_desc": "刘海摄像头能做什么，以及如何在刘海里镜像它。",
           "jsonld_headline": "Mac 上的刘海摄像头", "jsonld_desc": "Mac 刘海里的 1080p 摄像头、如何预览，以及如何在刘海里镜像。",
           "kicker": KICK["explainer"]["zh"], "h1": "Mac 上的刘海摄像头",
           "lede": "刘海存在就是为了容纳 MacBook 的摄像头。这里讲清这颗摄像头能做什么、通话前怎么检查，以及如何在刘海里镜像它。",
           "readtime": READ5["zh"], "crumb_this": "刘海摄像头",
           "faq": [("Mac 刘海里是什么摄像头？", "一颗 1080p FaceTime 高清摄像头，外加环境光传感器。较新机型支持“居中对焦”。"),
                   ("通话前如何查看刘海摄像头？", "打开 Photo Booth 或 QuickTime 的“新建影片录制”查看实时画面——或用 NotchNest 这样的刘海摄像头镜像，悬停即可预览。"),
                   ("有办法在刘海里镜像 Mac 摄像头吗？", "有。NotchNest 的摄像头镜像在刘海本身显示实时预览，无需另开应用即可检查取景。"),
                   ("摄像头镜像会录制什么吗？", "不会。镜像仅在本地显示你自己的实时画面。只要摄像头开启，绿色隐私指示灯就会由硬件点亮。")],
           "body": """<p>刘海存在的全部理由就是摄像头。Apple 缩小边框，把 FaceTime 高清摄像头塞进屏幕顶部的小缺口。这就是 Mac 上的刘海摄像头——而且它不止能用于视频通话。</p>
    <h2>刘海摄像头是什么</h2>
    <p>在 MacBook Pro（2021 年起）和 MacBook Air（2022 年起）上，刘海容纳一颗 1080p FaceTime 高清摄像头以及环境光传感器。在支持的机型上支持“居中对焦”，并为每个使用你摄像头的应用供画。</p>
    <h2>如何快速预览刘海摄像头</h2>
    <p>通常你要进了通话才看得到自己。想提前检查取景与光线，打开 Photo Booth 或 QuickTime →“新建影片录制”。两者都显示刘海摄像头的实时画面。</p>
    <h2>刘海摄像头镜像——一次悬停自查</h2>
    <p>只为看一眼自己的脸就开一整个应用很笨拙。NotchNest 内置了嵌在刘海里的摄像头镜像：悬停，实时预览就出现在摄像头实际所在之处。整理头发、检查背景，然后关掉——无需 Photo Booth，无需额外窗口。在刘海演示里看看。</p>
    <h2>隐私</h2>
    <p>只要摄像头启用，刘海摄像头旁的绿色 LED 就会亮起——它是硬连线的，软件无法绕过。刘海镜像只在本地显示你自己的画面；不录制，也不发往任何地方。</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>让你的刘海有用</h3><p>NotchNest 把十个工具放进 MacBook 刘海。在 Mac App Store 免费。</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="在 Mac App Store 下载" /></a>
    </div>""",
           "related": _related("zh", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "英文——基础。"))},
    "ar": {"title": "كاميرا النتش على الماك — NotchNest", "description": "كل شيء عن كاميرا النتش على الماك — كاميرا 1080p داخل النتش، وكيفية معاينتها، ومرآة كاميرا النتش للفحص السريع.",
           "og_title": "كاميرا النتش على الماك", "og_desc": "ماذا تفعل كاميرا النتش وكيف تعكسها في النتش.",
           "jsonld_headline": "كاميرا النتش على الماك", "jsonld_desc": "كاميرا 1080p داخل نتش الماك، وكيفية معاينتها وعكسها في النتش.",
           "kicker": KICK["explainer"]["ar"], "h1": "كاميرا النتش على الماك",
           "lede": "يوجد النتش ليحتضن كاميرا الماك بوك. إليك ماذا تفعل هذه الكاميرا، وكيف تفحصها قبل مكالمة، وكيف تعكسها في النتش نفسه.",
           "readtime": READ5["ar"], "crumb_this": "كاميرا النتش",
           "faq": [("ما الكاميرا الموجودة في نتش الماك؟", "كاميرا FaceTime HD بدقة 1080p، إضافةً إلى مستشعر الضوء المحيط. Center Stage مدعوم في الطُرز الأحدث."),
                   ("كيف أرى كاميرا النتش قبل مكالمة؟", "افتح Photo Booth أو «تسجيل فيلم جديد» في QuickTime لرؤية بث مباشر — أو استخدم مرآة كاميرا نتش مثل NotchNest لمعاينتها بتمريرة واحدة."),
                   ("هل توجد طريقة لعكس كاميرا الماك في النتش؟", "نعم. تعرض مرآة كاميرا NotchNest معاينة مباشرة في النتش نفسه لتفحص التأطير دون فتح تطبيق منفصل."),
                   ("هل تسجّل مرآة الكاميرا شيئًا؟", "لا. تعرض المرآة بثّك المباشر محليًا. ويظل مؤشر الخصوصية الأخضر يُضيء عبر العتاد كلما كانت الكاميرا قيد التشغيل.")],
           "body": """<p>سبب وجود النتش كله هو الكاميرا. صغّرت Apple الإطار ودفعت كاميرا FaceTime HD إلى فتحة صغيرة أعلى الشاشة. هذه هي كاميرا النتش على الماك — وفيها أكثر من مكالمات الفيديو.</p>
    <h2>ما هي كاميرا النتش</h2>
    <p>على MacBook Pro (من 2021) وMacBook Air (من 2022) يحتضن النتش كاميرا FaceTime HD بدقة 1080p إضافةً إلى مستشعر الضوء المحيط. تدعم Center Stage في الطُرز المدعومة وتغذّي كل تطبيق يستخدم كاميرتك.</p>
    <h2>كيف تعاين كاميرا النتش بسرعة</h2>
    <p>عادةً لا ترى نفسك إلا بعد أن تكون في المكالمة. لفحص التأطير والإضاءة مسبقًا، افتح Photo Booth أو QuickTime ← تسجيل فيلم جديد. كلاهما يعرض بثًا مباشرًا من كاميرا النتش.</p>
    <h2>مرآة كاميرا نتش — افحص نفسك بتمريرة</h2>
    <p>فتح تطبيق كامل لمجرد رؤية وجهك أمر أخرق. يتضمّن NotchNest مرآة كاميرا مدمجة في النتش: مرّر فتظهر معاينة مباشرة للكاميرا حيث تقع الكاميرا فعليًا. رتّب شعرك، وافحص خلفيتك، ثم أغلقها — بلا Photo Booth وبلا نافذة إضافية. شاهدها في عرض النتش.</p>
    <h2>الخصوصية</h2>
    <p>يُضيء مؤشر LED الأخضر بجانب كاميرا النتش كلما كانت الكاميرا نشطة — وهو موصول بالعتاد ولا يمكن للبرمجيات تجاوزه. تعرض مرآة النتش بثّك أنت فقط محليًا؛ لا يُسجَّل شيء ولا يُرسَل إلى أي مكان.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>اجعل نتشك مفيدًا</h3><p>يضع NotchNest عشر أدوات في نتش الماك بوك. مجانًا على Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>""",
           "related": _related("ar", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "إنجليزي — الأساسيات."))},
    "fr": {"title": "La caméra de l'encoche sur Mac — NotchNest", "description": "Tout sur la caméra de l'encoche sur Mac — la webcam 1080p dans l'encoche, comment la prévisualiser, et un miroir caméra dans l'encoche pour des vérifs rapides.",
           "og_title": "La caméra de l'encoche sur Mac", "og_desc": "Ce que fait la caméra de l'encoche et comment la mettre en miroir dans l'encoche.",
           "jsonld_headline": "La caméra de l'encoche sur Mac", "jsonld_desc": "La caméra 1080p dans l'encoche du Mac, comment la prévisualiser et la mettre en miroir dans l'encoche.",
           "kicker": KICK["explainer"]["fr"], "h1": "La caméra de l'encoche sur Mac",
           "lede": "L'encoche existe pour loger la caméra de votre MacBook. Voici ce que fait cette caméra, comment la vérifier avant un appel, et comment la mettre en miroir dans l'encoche même.",
           "readtime": READ5["fr"], "crumb_this": "Caméra de l'encoche",
           "faq": [("Quelle caméra se trouve dans l'encoche du Mac ?", "Une caméra FaceTime HD 1080p, plus le capteur de luminosité. Cadre centré est pris en charge sur les modèles récents."),
                   ("Comment voir la caméra de l'encoche avant un appel ?", "Ouvrez Photo Booth ou « Nouvel enregistrement vidéo » de QuickTime pour un aperçu en direct — ou utilisez un miroir caméra comme NotchNest pour la prévisualiser au survol."),
                   ("Peut-on mettre la caméra du Mac en miroir dans l'encoche ?", "Oui. Le miroir caméra de NotchNest affiche un aperçu webcam en direct dans l'encoche même, pour vérifier le cadrage sans lancer une app séparée."),
                   ("Le miroir caméra enregistre-t-il quoi que ce soit ?", "Non. Un miroir affiche votre propre flux en local. Le voyant vert de confidentialité s'allume quand même par matériel dès que la caméra est active.")],
           "body": """<p>La raison d'être de l'encoche, c'est la caméra. Apple a réduit la bordure et poussé la webcam FaceTime HD dans une petite découpe en haut de l'écran. C'est la caméra de l'encoche sur Mac — et elle sert à plus que les appels vidéo.</p>
    <h2>Ce qu'est la caméra de l'encoche</h2>
    <p>Sur MacBook Pro (depuis 2021) et MacBook Air (depuis 2022), l'encoche loge une caméra FaceTime HD 1080p plus le capteur de luminosité. Elle prend en charge Cadre centré sur les modèles compatibles et alimente chaque app qui utilise votre webcam.</p>
    <h2>Comment prévisualiser vite la caméra de l'encoche</h2>
    <p>Normalement, vous ne vous voyez qu'une fois déjà en appel. Pour vérifier cadrage et lumière avant, ouvrez Photo Booth ou QuickTime → Nouvel enregistrement vidéo. Les deux montrent un flux en direct de la caméra de l'encoche.</p>
    <h2>Un miroir caméra dans l'encoche — vérifiez-vous en un survol</h2>
    <p>Ouvrir une app entière juste pour voir votre visage est maladroit. NotchNest inclut un miroir caméra intégré à l'encoche : survolez et un aperçu webcam en direct apparaît là où la caméra se trouve physiquement. Recoiffez-vous, vérifiez l'arrière-plan, puis fermez — pas de Photo Booth, pas de fenêtre en plus. Voyez-le dans le terrain de jeu de l'encoche.</p>
    <h2>Confidentialité</h2>
    <p>Le voyant vert à côté de la caméra de l'encoche s'allume dès que la caméra est active — il est câblé en dur et ne peut être contourné par logiciel. Un miroir d'encoche ne montre que votre propre flux en local ; rien n'est enregistré ni envoyé.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Rendez votre encoche utile</h3><p>NotchNest met dix outils dans l'encoche de votre MacBook. Gratuit sur le Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>""",
           "related": _related("fr", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Anglais — les bases."))},
    "pt-BR": {"title": "A câmera do notch no Mac — NotchNest", "description": "Tudo sobre a câmera do notch no Mac — a webcam de 1080p dentro do notch, como visualizá-la e um espelho da câmera no notch para conferências rápidas.",
              "og_title": "A câmera do notch no Mac", "og_desc": "O que a câmera do notch faz e como espelhá-la no notch.",
              "jsonld_headline": "A câmera do notch no Mac", "jsonld_desc": "A câmera de 1080p dentro do notch do Mac, como visualizá-la e espelhá-la no notch.",
              "kicker": KICK["explainer"]["pt-BR"], "h1": "A câmera do notch no Mac",
              "lede": "O notch existe para abrigar a câmera do seu MacBook. Veja o que essa câmera faz, como conferi-la antes de uma call e como espelhá-la no próprio notch.",
              "readtime": READ5["pt-BR"], "crumb_this": "Câmera do notch",
              "faq": [("Que câmera há no notch do Mac?", "Uma câmera FaceTime HD de 1080p, mais o sensor de luz ambiente. Palco Central é suportado nos modelos mais novos."),
                      ("Como vejo a câmera do notch antes de uma call?", "Abra o Photo Booth ou a Nova Gravação de Filme do QuickTime para um feed ao vivo — ou use um espelho da câmera como o NotchNest para visualizá-la ao passar o cursor."),
                      ("Dá para espelhar a câmera do Mac no notch?", "Sim. O espelho da câmera do NotchNest mostra uma prévia ao vivo no próprio notch, para você conferir o enquadramento sem abrir um app separado."),
                      ("O espelho da câmera grava algo?", "Não. Um espelho mostra o seu próprio feed localmente. O LED verde de privacidade ainda acende por hardware sempre que a câmera está ligada.")],
              "body": """<p>A razão de o notch existir é a câmera. A Apple encolheu a borda e empurrou a webcam FaceTime HD para um pequeno recorte no topo da tela. Essa é a câmera do notch no Mac — e ela serve para mais do que chamadas de vídeo.</p>
    <h2>O que é a câmera do notch</h2>
    <p>No MacBook Pro (2021+) e MacBook Air (2022+), o notch abriga uma câmera FaceTime HD de 1080p mais o sensor de luz ambiente. Suporta Palco Central nos modelos compatíveis e alimenta todo app que usa a sua webcam.</p>
    <h2>Como visualizar a câmera do notch rapidamente</h2>
    <p>Normalmente você só se vê depois de já estar na call. Para conferir enquadramento e luz antes, abra o Photo Booth ou o QuickTime → Nova Gravação de Filme. Ambos mostram um feed ao vivo da câmera do notch.</p>
    <h2>Um espelho da câmera no notch — confira-se em um hover</h2>
    <p>Abrir um app inteiro só para ver o seu rosto é desajeitado. O NotchNest inclui um espelho da câmera embutido no notch: passe o cursor e uma prévia ao vivo aparece exatamente onde a câmera fica fisicamente. Ajeite o cabelo, confira o fundo, e feche — sem Photo Booth, sem janela extra. Veja no playground do notch.</p>
    <h2>Privacidade</h2>
    <p>O LED verde ao lado da câmera do notch acende sempre que a câmera está ativa — é ligado por hardware e não pode ser burlado por software. Um espelho do notch só mostra o seu próprio feed localmente; nada é gravado ou enviado a lugar nenhum.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Grátis na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-BR", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglês — o básico."))},
    "pt-PT": {"title": "A câmara do notch no Mac — NotchNest", "description": "Tudo sobre a câmara do notch no Mac — a webcam de 1080p dentro do notch, como pré-visualizá-la e um espelho da câmara no notch para verificações rápidas.",
              "og_title": "A câmara do notch no Mac", "og_desc": "O que a câmara do notch faz e como espelhá-la no notch.",
              "jsonld_headline": "A câmara do notch no Mac", "jsonld_desc": "A câmara de 1080p dentro do notch do Mac, como pré-visualizá-la e espelhá-la no notch.",
              "kicker": KICK["explainer"]["pt-PT"], "h1": "A câmara do notch no Mac",
              "lede": "O notch existe para alojar a câmara do seu MacBook. Veja o que essa câmara faz, como verificá-la antes de uma chamada e como espelhá-la no próprio notch.",
              "readtime": READ5["pt-PT"], "crumb_this": "Câmara do notch",
              "faq": [("Que câmara há no notch do Mac?", "Uma câmara FaceTime HD de 1080p, mais o sensor de luz ambiente. O Palco Central é suportado nos modelos mais recentes."),
                      ("Como vejo a câmara do notch antes de uma chamada?", "Abra o Photo Booth ou a Nova Gravação de Filme do QuickTime para um feed em direto — ou use um espelho da câmara como o NotchNest para a pré-visualizar ao passar o cursor."),
                      ("Dá para espelhar a câmara do Mac no notch?", "Sim. O espelho da câmara do NotchNest mostra uma pré-visualização em direto no próprio notch, para verificar o enquadramento sem abrir uma app separada."),
                      ("O espelho da câmara grava algo?", "Não. Um espelho mostra o seu próprio feed localmente. O LED verde de privacidade acende à mesma por hardware sempre que a câmara está ligada.")],
              "body": """<p>A razão de o notch existir é a câmara. A Apple encolheu a moldura e empurrou a webcam FaceTime HD para um pequeno recorte no topo do ecrã. Essa é a câmara do notch no Mac — e serve para mais do que chamadas de vídeo.</p>
    <h2>O que é a câmara do notch</h2>
    <p>No MacBook Pro (2021+) e MacBook Air (2022+), o notch aloja uma câmara FaceTime HD de 1080p mais o sensor de luz ambiente. Suporta o Palco Central nos modelos compatíveis e alimenta todas as apps que usam a sua webcam.</p>
    <h2>Como pré-visualizar a câmara do notch rapidamente</h2>
    <p>Normalmente só se vê depois de já estar na chamada. Para verificar enquadramento e luz antes, abra o Photo Booth ou o QuickTime → Nova Gravação de Filme. Ambos mostram um feed em direto da câmara do notch.</p>
    <h2>Um espelho da câmara no notch — verifique-se num hover</h2>
    <p>Abrir uma app inteira só para ver o seu rosto é desajeitado. O NotchNest inclui um espelho da câmara integrado no notch: passe o cursor e uma pré-visualização em direto aparece exatamente onde a câmara está fisicamente. Ajeite o cabelo, verifique o fundo, e feche — sem Photo Booth, sem janela extra. Veja no playground do notch.</p>
    <h2>Privacidade</h2>
    <p>O LED verde ao lado da câmara do notch acende sempre que a câmara está ativa — é ligado por hardware e não pode ser contornado por software. Um espelho do notch só mostra o seu próprio feed localmente; nada é gravado ou enviado para lado nenhum.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Torne o seu notch útil</h3><p>O NotchNest coloca dez ferramentas no notch do seu MacBook. Gratuito na Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>""",
              "related": _related("pt-PT", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglês — o básico."))},
    "es-MX": {"title": "La cámara del notch en Mac — NotchNest", "description": "Todo sobre la cámara del notch en Mac — la webcam de 1080p dentro del notch, cómo previsualizarla y un espejo de cámara en el notch para revisiones rápidas.",
              "og_title": "La cámara del notch en Mac", "og_desc": "Qué hace la cámara del notch y cómo reflejarla en el notch.",
              "jsonld_headline": "La cámara del notch en Mac", "jsonld_desc": "La cámara de 1080p dentro del notch del Mac, cómo previsualizarla y reflejarla en el notch.",
              "kicker": KICK["explainer"]["es-MX"], "h1": "La cámara del notch en Mac",
              "lede": "El notch existe para alojar la cámara de tu MacBook. Aquí qué hace esa cámara, cómo revisarla antes de una llamada y cómo reflejarla en el propio notch.",
              "readtime": READ5["es-MX"], "crumb_this": "Cámara del notch",
              "faq": [("¿Qué cámara hay en el notch del Mac?", "Una cámara FaceTime HD de 1080p, más el sensor de luz ambiental. Encuadre Centrado es compatible en los modelos más nuevos."),
                      ("¿Cómo veo la cámara del notch antes de una llamada?", "Abre Photo Booth o la Nueva grabación de película de QuickTime para un feed en vivo — o usa un espejo de cámara como NotchNest para previsualizarla al pasar el cursor."),
                      ("¿Hay forma de reflejar la cámara del Mac en el notch?", "Sí. El espejo de cámara de NotchNest muestra una vista previa en vivo en el propio notch, para revisar el encuadre sin abrir una app aparte."),
                      ("¿El espejo de cámara graba algo?", "No. Un espejo muestra tu propio feed localmente. El LED verde de privacidad se enciende igual por hardware siempre que la cámara está encendida.")],
              "body": """<p>La razón entera de que exista el notch es la cámara. Apple encogió el marco y metió la webcam FaceTime HD en un pequeño recorte en la parte superior de la pantalla. Esa es la cámara del notch en Mac — y sirve para más que videollamadas.</p>
    <h2>Qué es la cámara del notch</h2>
    <p>En MacBook Pro (2021+) y MacBook Air (2022+), el notch aloja una cámara FaceTime HD de 1080p más el sensor de luz ambiental. Admite Encuadre Centrado en los modelos compatibles y alimenta a cada app que usa tu webcam.</p>
    <h2>Cómo previsualizar la cámara del notch rápido</h2>
    <p>Normalmente solo te ves una vez que ya estás en la llamada. Para revisar encuadre e iluminación antes, abre Photo Booth o QuickTime → Nueva grabación de película. Ambos muestran un feed en vivo de la cámara del notch.</p>
    <h2>Un espejo de cámara en el notch — revísate en un hover</h2>
    <p>Abrir una app entera solo para ver tu cara es torpe. NotchNest incluye un espejo de cámara integrado en el notch: pasa el cursor y una vista previa en vivo aparece justo donde está físicamente la cámara. Acomódate el cabello, revisa el fondo, y ciérralo — sin Photo Booth, sin ventana extra. Míralo en el playground del notch.</p>
    <h2>Privacidad</h2>
    <p>El LED verde junto a la cámara del notch se enciende siempre que la cámara está activa — está cableado por hardware y el software no puede eludirlo. Un espejo del notch solo muestra tu propio feed localmente; nada se graba ni se envía a ningún lado.</p>
    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body"><h3>Haz útil tu notch</h3><p>NotchNest pone diez herramientas en el notch de tu MacBook. Gratis en el Mac App Store.</p></div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>""",
              "related": _related("es-MX", ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglés — lo básico."))},
}


LEARN_ARTICLES = {
    "what-is-the-macos-notch": _assemble(WHATIS),
    "does-the-mac-notch-actually-do-anything": _assemble(DOES),
    "notch-nest-vs-boring-notch-vs-notchdrop": _assemble(BVBVD),
    "how-to-hide-the-notch-on-mac": _assemble(HIDE),
    "what-is-dynamic-island-on-mac": _assemble(DYN),
    "drop-files-into-macbook-notch": _assemble(DROP),
    "notch-camera-on-mac": _assemble(CAMERA),
}
