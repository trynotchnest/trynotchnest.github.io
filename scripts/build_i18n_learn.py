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
}
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


LEARN_ARTICLES = {
    "what-is-the-macos-notch": _assemble(WHATIS),
}
