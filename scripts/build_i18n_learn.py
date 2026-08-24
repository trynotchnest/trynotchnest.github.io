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


LEARN_ARTICLES = {
    "what-is-the-macos-notch": _assemble(WHATIS),
    "does-the-mac-notch-actually-do-anything": _assemble(DOES),
    "notch-nest-vs-boring-notch-vs-notchdrop": _assemble(BVBVD),
}
