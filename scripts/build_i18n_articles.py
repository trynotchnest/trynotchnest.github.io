# -*- coding: utf-8 -*-
"""Article translations for build_i18n.py (how-to-use-the-macbook-notch,
best-macos-notch-apps) across fr, es-MX, pt-BR, pt-PT, ar. %STORE% is replaced
with the locale App Store URL at build time."""

# per-locale reusable bits
C = {
    "de": {"crumb_home": "Start", "crumb_learn": "Lernen", "nav_learn": "Lernen",
           "byline": "Von Satnam Singh", "author_h3": "Über den Autor", "related_h2": "Weiterlesen",
           "updated": "Aktualisiert 13. Juni 2026"},
    "zh": {"crumb_home": "首页", "crumb_learn": "学习", "nav_learn": "学习",
           "byline": "作者 Satnam Singh", "author_h3": "关于作者", "related_h2": "继续阅读",
           "updated": "更新于 2026 年 6 月 13 日"},
    "fr": {"crumb_home": "Accueil", "crumb_learn": "Guides", "nav_learn": "Guides",
           "byline": "Par Satnam Singh", "author_h3": "À propos de l'auteur", "related_h2": "À lire aussi",
           "updated": "Mis à jour le 13 juin 2026"},
    "es-MX": {"crumb_home": "Inicio", "crumb_learn": "Guías", "nav_learn": "Guías",
              "byline": "Por Satnam Singh", "author_h3": "Sobre el autor", "related_h2": "Sigue leyendo",
              "updated": "Actualizado el 13 de junio de 2026"},
    "pt-BR": {"crumb_home": "Início", "crumb_learn": "Guias", "nav_learn": "Guias",
              "byline": "Por Satnam Singh", "author_h3": "Sobre o autor", "related_h2": "Continue lendo",
              "updated": "Atualizado em 13 de junho de 2026"},
    "pt-PT": {"crumb_home": "Início", "crumb_learn": "Guias", "nav_learn": "Guias",
              "byline": "Por Satnam Singh", "author_h3": "Sobre o autor", "related_h2": "Continue a ler",
              "updated": "Atualizado a 13 de junho de 2026"},
    "ar": {"crumb_home": "الرئيسية", "crumb_learn": "الأدلة", "nav_learn": "الأدلة",
           "byline": "بقلم Satnam Singh", "author_h3": "عن المؤلف", "related_h2": "اقرأ أيضًا",
           "updated": "تحديث 13 يونيو 2026"},
}

AUTHOR_LONG = {
    "de": '<strong>Satnam Singh</strong> ist der Swift-Entwickler hinter NotchNest. Er schreibt über macOS-Produktivität, KI auf Apple Silicon und Indie-App-Handwerk. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "zh": '<strong>Satnam Singh</strong> 是 NotchNest 背后的 Swift 开发者。他撰写关于 macOS 生产力、Apple 芯片上的 AI 以及独立应用工艺的文章。<a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "fr": '<strong>Satnam Singh</strong> est le développeur Swift derrière NotchNest. Il écrit sur la productivité macOS, l\'IA sur Apple Silicon et l\'artisanat des apps indépendantes. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "es-MX": '<strong>Satnam Singh</strong> es el desarrollador Swift detrás de NotchNest. Escribe sobre productividad en macOS, IA en Apple Silicon y el oficio de las apps indie. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "pt-BR": '<strong>Satnam Singh</strong> é o desenvolvedor Swift por trás do NotchNest. Ele escreve sobre produtividade no macOS, IA no Apple Silicon e o ofício de apps indie. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "pt-PT": '<strong>Satnam Singh</strong> é o programador Swift por trás do NotchNest. Escreve sobre produtividade no macOS, IA no Apple Silicon e o ofício das apps independentes. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "ar": '<strong>Satnam Singh</strong> هو مطوّر Swift وراء NotchNest. يكتب عن إنتاجية macOS والذكاء الاصطناعي على Apple Silicon وحِرفة التطبيقات المستقلة. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
}
AUTHOR_SHORT = {
    "fr": '<strong>Satnam Singh</strong> développe NotchNest. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "es-MX": '<strong>Satnam Singh</strong> desarrolla NotchNest. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "pt-BR": '<strong>Satnam Singh</strong> desenvolve o NotchNest. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "pt-PT": '<strong>Satnam Singh</strong> desenvolve o NotchNest. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
    "ar": '<strong>Satnam Singh</strong> يطوّر NotchNest. <a href="https://silverseahog.com/" target="_blank" rel="noopener">silverseahog.com</a> · <a href="https://twitter.com/codetard" target="_blank" rel="noopener nofollow">@codetard</a>',
}

# ── how-to-use-the-macbook-notch ────────────────────────────────────────────
HOWTO = {
    "fr": {
        "title": "Comment utiliser l'encoche du MacBook — NotchNest",
        "description": "Transformez l'encoche vide du MacBook en centre de productivité en trois étapes. Calendrier, presse-papiers, notes, Pomodoro, musique et AirDrop — à un survol près.",
        "og_title": "Comment utiliser l'encoche du MacBook", "og_desc": "Trois étapes vers une encoche utile.",
        "jsonld_headline": "Comment utiliser l'encoche du MacBook",
        "jsonld_desc": "Transformez l'encoche vide du MacBook en centre de productivité avec calendrier, presse-papiers, notes, Pomodoro, musique et AirDrop.",
        "kicker": "Guide", "h1": "Comment utiliser l'encoche du MacBook",
        "lede": "Trois étapes, quatre-vingt-dix secondes. Transformez l'encoche vide de votre MacBook Pro ou MacBook Air en centre de productivité pour calendrier, presse-papiers, notes, Pomodoro, musique et AirDrop.",
        "readtime": "5 min de lecture", "crumb_this": "Utiliser l'encoche",
        "howto_name": "Comment utiliser l'encoche du MacBook",
        "howto_steps": [
            ("Installer NotchNest", "Téléchargez NotchNest gratuitement sur le Mac App Store. Ouvrez l'app une fois."),
            ("Accorder les autorisations", "Confirmez l'accès au calendrier, aux notes et à la musique. Toutes les autorisations sont facultatives."),
            ("Survoler l'encoche", "Amenez le pointeur sur l'encoche. Le panneau en verre s'ouvre. Choisissez les widgets dans les réglages."),
        ],
        "faq": [
            ("Dois-je d'abord activer l'encoche ?", "Non. L'encoche est du matériel. macOS la traite comme une partie de la barre des menus. Installez une app d'encoche comme NotchNest pour la rendre interactive."),
            ("Pourquoi rien ne se passe au survol ?", "Sans app d'encoche, le survol ne fait rien — macOS lui-même n'a pas d'interface d'encoche. Installez NotchNest, Boring Notch ou NotchDrop pour un comportement au survol."),
            ("L'utilisation de l'encoche consomme-t-elle de la batterie ?", "Les apps d'encoche SwiftUI natives se mettent en veille quand le panneau est fermé et utilisent quelques Mo de RAM. Aucun impact mesurable sur la batterie en usage normal."),
            ("Puis-je déclencher le panneau sans souris ?", "Oui — NotchNest prend en charge un raccourci global. Réglez-le dans Réglages → Déclencheurs."),
        ],
        "body": """<p>Par défaut, l'encoche du MacBook ne fait <strong>rien</strong> — c'est un espace pour la caméra. Apple ne fournit aucune interface d'encoche. Les apps tierces comblent le vide. Le chemin le plus rapide de « creux ignoré » à « vraiment utile », c'est NotchNest, gratuit sur le Mac App Store.</p>

    <h2>Étape 1 — Installer NotchNest</h2>
    <p>Ouvrez le Mac App Store, cherchez « NotchNest », installez. Gratuit. Signé et notarisé par Apple, en bac à sable automatiquement. Nécessite macOS 14 (Sonoma) ou plus récent ; Apple Silicon recommandé pour les fonctions IA.</p>
    <p>Après l'installation, ouvrez-la une fois. macOS l'enregistre dans les objets d'ouverture de session pour qu'elle démarre automatiquement.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Installer NotchNest</h3>
        <p>Gratuit sur le Mac App Store. macOS 14+. Sans compte, sans abonnement.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>

    <h2>Étape 2 — Accorder les autorisations</h2>
    <p>NotchNest demande les autorisations au fur et à mesure — jamais toutes d'un coup. Chacune peut être ignorée :</p>
    <ul>
      <li><strong>Calendrier</strong> — pour le widget agenda du jour et les briefings IA.</li>
      <li><strong>Notes</strong> — pour les notes rapides synchronisées avec Apple Notes.</li>
      <li><strong>Musique / Spotify</strong> — pour le contrôle de la lecture.</li>
      <li><strong>Apple Intelligence</strong> — pour reformuler le presse-papiers, les briefings de calendrier, l'affinage des notes. Tout sur l'appareil.</li>
      <li><strong>Photos / Caméra</strong> — pour le widget miroir caméra.</li>
    </ul>
    <p>Rien n'est envoyé en ligne. NotchNest est une app du Mac App Store — elle ne peut pas faire de requêtes réseau hors de celles attendues.</p>

    <h2>Étape 3 — Survoler l'encoche</h2>
    <p>Amenez le pointeur directement sur l'encoche. Le panneau se déploie — une surface en verre qui encadre l'encoche avec des widgets de part et d'autre. Cliquez un widget pour l'utiliser ; cliquez ailleurs pour fermer.</p>
    <p>Pas de déclenchement au survol ? <strong>NotchNest → Réglages → Déclencheurs</strong> permet le clic seul ou un raccourci global (par défaut : F1). Vous pouvez aussi garder le panneau ouvert en permanence.</p>

    <h2>Choisir les widgets</h2>
    <p>Réglages → Widgets. Chaque widget est indépendant. N'activez que ce dont vous avez besoin :</p>
    <ul>
      <li><strong>Presse-papiers IA</strong> — historique cherchable, épingles, reformulation IA.</li>
      <li><strong>AirDrop / Bac à fichiers</strong> — déposez un fichier sur l'encoche, transférez.</li>
      <li><strong>Favoris</strong> — URLs et apps en lancement d'un clic.</li>
      <li><strong>Calendrier</strong> — agenda du jour avec briefings IA.</li>
      <li><strong>Miroir caméra</strong> — aperçu webcam en un tap.</li>
      <li><strong>Musique</strong> — Spotify et Apple Music avec pochette.</li>
      <li><strong>Pomodoro</strong> — minuteur de focus avec pauses et série.</li>
      <li><strong>Notes rapides</strong> — capture, affinage IA, sync Apple Notes.</li>
    </ul>

    <h2>Si votre Mac n'a pas d'encoche</h2>
    <p>NotchNest fonctionne quand même. Sur MacBook Air M1, anciens MacBook Pro, Mac mini, iMac et Mac Studio, il apparaît comme un panneau fin en haut au centre de l'écran. Mêmes widgets, mêmes raccourcis.</p>

    <h2>Problèmes courants</h2>
    <h3>Le panneau ne s'ouvre pas au survol.</h3>
    <p><strong>Réglages Système → Confidentialité et sécurité → Accessibilité</strong> — activez NotchNest. macOS l'exige pour les déclencheurs au survol inter-fenêtres.</p>
    <h3>L'encoche masque des icônes de la barre des menus.</h3>
    <p>Avec beaucoup d'icônes, l'encoche peut en cacher. Utilisez un gestionnaire de barre des menus comme Ice ou Bartender.</p>
    <h3>Les fonctions IA n'apparaissent pas.</h3>
    <p>Apple Intelligence nécessite macOS 15 (Sequoia) ou plus récent sur Apple Silicon. Les autres widgets continuent de fonctionner.</p>""",
        "related": [
            ("/fr/learn/best-macos-notch-apps/", "Les meilleures apps d'encoche macOS", "Sélection 2026."),
            ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Anglais — les bases."),
            ("/fr/", "Accueil NotchNest", "Vers la page d'accueil française."),
        ],
    },
    "es-MX": {
        "title": "Cómo usar el notch del MacBook — NotchNest",
        "description": "Convierte el notch vacío del MacBook en un centro de productividad en tres pasos. Calendario, portapapeles, notas, Pomodoro, música y AirDrop, a un cursor de distancia.",
        "og_title": "Cómo usar el notch del MacBook", "og_desc": "Tres pasos hacia un notch útil.",
        "jsonld_headline": "Cómo usar el notch del MacBook",
        "jsonld_desc": "Convierte el notch vacío del MacBook en un centro de productividad con calendario, portapapeles, notas, Pomodoro, música y AirDrop.",
        "kicker": "Guía", "h1": "Cómo usar el notch del MacBook",
        "lede": "Tres pasos, noventa segundos. Convierte el notch vacío de tu MacBook Pro o MacBook Air en un centro de productividad para calendario, portapapeles, notas, Pomodoro, música y AirDrop.",
        "readtime": "5 min de lectura", "crumb_this": "Usar el notch",
        "howto_name": "Cómo usar el notch del MacBook",
        "howto_steps": [
            ("Instalar NotchNest", "Descarga NotchNest gratis en el Mac App Store. Abre la app una vez."),
            ("Conceder permisos", "Confirma el acceso a calendario, notas y música. Todos los permisos son opcionales."),
            ("Pasar el cursor sobre el notch", "Lleva el cursor al notch. El panel de vidrio se abre. Elige los widgets en los ajustes."),
        ],
        "faq": [
            ("¿Tengo que activar el notch primero?", "No. El notch es hardware. macOS lo trata como parte de la barra de menús. Instala una app de notch como NotchNest para hacerlo interactivo."),
            ("¿Por qué no pasa nada al pasar el cursor?", "Sin una app de notch, pasar el cursor no hace nada: macOS no tiene interfaz de notch. Instala NotchNest, Boring Notch o NotchDrop para el comportamiento al pasar el cursor."),
            ("¿Usar el notch consume batería?", "Las apps de notch nativas en SwiftUI se duermen cuando el panel está cerrado y usan unos pocos MB de RAM. Sin impacto medible en la batería en uso normal."),
            ("¿Puedo abrir el panel sin ratón?", "Sí: NotchNest admite un atajo global. Configúralo en Ajustes → Disparadores."),
        ],
        "body": """<p>Por defecto, el notch del MacBook no hace <strong>nada</strong>: es un espacio para la cámara. Apple no incluye ninguna interfaz de notch. Las apps de terceros llenan el vacío. El camino más rápido de «hueco ignorado» a «realmente útil» es NotchNest, gratis en el Mac App Store.</p>

    <h2>Paso 1 — Instalar NotchNest</h2>
    <p>Abre el Mac App Store, busca «NotchNest», instala. Gratis. Firmado y notarizado por Apple, en entorno aislado automáticamente. Requiere macOS 14 (Sonoma) o posterior; Apple Silicon recomendado para las funciones de IA.</p>
    <p>Tras instalar, ábrelo una vez. macOS lo registra en los ítems de inicio de sesión para que arranque automáticamente.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Instalar NotchNest</h3>
        <p>Gratis en el Mac App Store. macOS 14+. Sin cuenta, sin suscripción.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>

    <h2>Paso 2 — Conceder permisos</h2>
    <p>NotchNest pide permisos según los necesita, nunca todos de golpe. Cada uno se puede omitir:</p>
    <ul>
      <li><strong>Calendario</strong> — para el widget de agenda del día y los briefings de IA.</li>
      <li><strong>Notas</strong> — para las notas rápidas que se sincronizan con Apple Notes.</li>
      <li><strong>Música / Spotify</strong> — para el control de reproducción.</li>
      <li><strong>Apple Intelligence</strong> — para reformular el portapapeles, los briefings de calendario y el refinado de notas. Todo en el dispositivo.</li>
      <li><strong>Fotos / Cámara</strong> — para el widget de espejo de cámara.</li>
    </ul>
    <p>No se sube nada. NotchNest es una app del Mac App Store: no puede hacer solicitudes de red fuera de las esperadas.</p>

    <h2>Paso 3 — Pasar el cursor sobre el notch</h2>
    <p>Lleva el cursor directamente al notch. El panel se despliega: una superficie de vidrio que enmarca el notch con widgets a ambos lados. Haz clic en un widget para usarlo; haz clic fuera para cerrar.</p>
    <p>¿No quieres disparo al pasar el cursor? <strong>NotchNest → Ajustes → Disparadores</strong> permite solo clic o un atajo global (por defecto: F1). También puedes mantener el panel siempre abierto.</p>

    <h2>Elegir los widgets</h2>
    <p>Ajustes → Widgets. Cada widget es independiente. Activa solo lo que necesites:</p>
    <ul>
      <li><strong>Portapapeles con IA</strong> — historial con búsqueda, fijados, reformulación con IA.</li>
      <li><strong>AirDrop / Bandeja de archivos</strong> — arrastra un archivo al notch y reenvíalo.</li>
      <li><strong>Favoritos</strong> — URLs y apps para abrir con un clic.</li>
      <li><strong>Calendario</strong> — agenda del día con briefings de IA.</li>
      <li><strong>Espejo de cámara</strong> — vista previa de la webcam con un toque.</li>
      <li><strong>Música</strong> — Spotify y Apple Music con carátula.</li>
      <li><strong>Pomodoro</strong> — temporizador de enfoque con descansos y racha.</li>
      <li><strong>Notas rápidas</strong> — captura, refinado con IA, sincronización con Apple Notes.</li>
    </ul>

    <h2>Si tu Mac no tiene notch</h2>
    <p>NotchNest funciona igual. En MacBook Air M1, MacBook Pro antiguos, Mac mini, iMac y Mac Studio aparece como un panel delgado en la parte superior central de la pantalla. Mismos widgets, mismos atajos.</p>

    <h2>Problemas comunes</h2>
    <h3>El panel no se abre al pasar el cursor.</h3>
    <p><strong>Ajustes del Sistema → Privacidad y seguridad → Accesibilidad</strong> — activa NotchNest. macOS lo exige para los disparadores al pasar el cursor entre ventanas.</p>
    <h3>El notch tapa iconos de la barra de menús.</h3>
    <p>Con muchos iconos, el notch puede ocultar algunos. Usa un gestor de barra de menús como Ice o Bartender.</p>
    <h3>Las funciones de IA no aparecen.</h3>
    <p>Apple Intelligence requiere macOS 15 (Sequoia) o posterior en Apple Silicon. Los demás widgets siguen funcionando.</p>""",
        "related": [
            ("/es-mx/learn/best-macos-notch-apps/", "Las mejores apps de notch para macOS", "Selección 2026."),
            ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglés — lo básico."),
            ("/es-mx/", "Inicio de NotchNest", "A la página de inicio en español."),
        ],
    },
    "pt-BR": {
        "title": "Como usar o notch do MacBook — NotchNest",
        "description": "Transforme o notch vazio do MacBook em uma central de produtividade em três passos. Calendário, área de transferência, notas, Pomodoro, música e AirDrop, a um cursor de distância.",
        "og_title": "Como usar o notch do MacBook", "og_desc": "Três passos para um notch útil.",
        "jsonld_headline": "Como usar o notch do MacBook",
        "jsonld_desc": "Transforme o notch vazio do MacBook em uma central de produtividade com calendário, área de transferência, notas, Pomodoro, música e AirDrop.",
        "kicker": "Guia", "h1": "Como usar o notch do MacBook",
        "lede": "Três passos, noventa segundos. Transforme o notch vazio do seu MacBook Pro ou MacBook Air em uma central de produtividade para calendário, área de transferência, notas, Pomodoro, música e AirDrop.",
        "readtime": "5 min de leitura", "crumb_this": "Usar o notch",
        "howto_name": "Como usar o notch do MacBook",
        "howto_steps": [
            ("Instalar o NotchNest", "Baixe o NotchNest grátis na Mac App Store. Abra o app uma vez."),
            ("Conceder permissões", "Confirme o acesso a calendário, notas e música. Todas as permissões são opcionais."),
            ("Passar o cursor sobre o notch", "Leve o cursor até o notch. O painel de vidro se abre. Escolha os widgets nos ajustes."),
        ],
        "faq": [
            ("Preciso ativar o notch primeiro?", "Não. O notch é hardware. O macOS o trata como parte da barra de menus. Instale um app de notch como o NotchNest para torná-lo interativo."),
            ("Por que nada acontece ao passar o cursor?", "Sem um app de notch, passar o cursor não faz nada — o macOS não tem interface de notch. Instale NotchNest, Boring Notch ou NotchDrop para o comportamento ao passar o cursor."),
            ("Usar o notch consome bateria?", "Apps de notch nativos em SwiftUI dormem quando o painel está fechado e usam poucos MB de RAM. Nenhum impacto perceptível na bateria em uso normal."),
            ("Posso abrir o painel sem mouse?", "Sim — o NotchNest suporta um atalho global. Configure em Ajustes → Gatilhos."),
        ],
        "body": """<p>Por padrão, o notch do MacBook não faz <strong>nada</strong> — é um espaço para a câmera. A Apple não inclui nenhuma interface de notch. Apps de terceiros preenchem a lacuna. O caminho mais rápido de «recorte ignorado» a «realmente útil» é o NotchNest, grátis na Mac App Store.</p>

    <h2>Passo 1 — Instalar o NotchNest</h2>
    <p>Abra a Mac App Store, busque «NotchNest», instale. Grátis. Assinado e notarizado pela Apple, em sandbox automaticamente. Requer macOS 14 (Sonoma) ou mais recente; Apple Silicon recomendado para os recursos de IA.</p>
    <p>Depois de instalar, abra uma vez. O macOS o registra nos itens de início de sessão para que abra automaticamente.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Instalar o NotchNest</h3>
        <p>Grátis na Mac App Store. macOS 14+. Sem conta, sem assinatura.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>

    <h2>Passo 2 — Conceder permissões</h2>
    <p>O NotchNest pede permissões conforme necessário — nunca todas de uma vez. Cada uma pode ser ignorada:</p>
    <ul>
      <li><strong>Calendário</strong> — para o widget de agenda do dia e os briefings de IA.</li>
      <li><strong>Notas</strong> — para as notas rápidas que sincronizam com o Apple Notes.</li>
      <li><strong>Música / Spotify</strong> — para o controle de reprodução.</li>
      <li><strong>Apple Intelligence</strong> — para reformular a área de transferência, os briefings de calendário e o refinamento de notas. Tudo no dispositivo.</li>
      <li><strong>Fotos / Câmera</strong> — para o widget de espelho da câmera.</li>
    </ul>
    <p>Nada é enviado. O NotchNest é um app da Mac App Store — não pode fazer requisições de rede além das esperadas.</p>

    <h2>Passo 3 — Passar o cursor sobre o notch</h2>
    <p>Leve o cursor diretamente ao notch. O painel se abre — uma superfície de vidro que emoldura o notch com widgets dos dois lados. Clique num widget para usar; clique fora para fechar.</p>
    <p>Não quer o disparo ao passar o cursor? <strong>NotchNest → Ajustes → Gatilhos</strong> permite só clique ou um atalho global (padrão: F1). Você também pode manter o painel sempre aberto.</p>

    <h2>Escolher os widgets</h2>
    <p>Ajustes → Widgets. Cada widget é independente. Ative só o que precisar:</p>
    <ul>
      <li><strong>Área de transferência com IA</strong> — histórico pesquisável, fixados, reformulação por IA.</li>
      <li><strong>AirDrop / Bandeja de arquivos</strong> — arraste um arquivo ao notch e encaminhe.</li>
      <li><strong>Favoritos</strong> — URLs e apps para abrir com um clique.</li>
      <li><strong>Calendário</strong> — agenda do dia com briefings de IA.</li>
      <li><strong>Espelho da câmera</strong> — prévia da webcam com um toque.</li>
      <li><strong>Música</strong> — Spotify e Apple Music com capa.</li>
      <li><strong>Pomodoro</strong> — timer de foco com pausas e sequência.</li>
      <li><strong>Notas rápidas</strong> — captura, refinamento por IA, sincronização com Apple Notes.</li>
    </ul>

    <h2>Se o seu Mac não tem notch</h2>
    <p>O NotchNest funciona mesmo assim. Em MacBook Air M1, MacBook Pro antigos, Mac mini, iMac e Mac Studio ele aparece como um painel fino no topo central da tela. Mesmos widgets, mesmos atalhos.</p>

    <h2>Problemas comuns</h2>
    <h3>O painel não abre ao passar o cursor.</h3>
    <p><strong>Ajustes do Sistema → Privacidade e Segurança → Acessibilidade</strong> — ative o NotchNest. O macOS exige isso para os gatilhos ao passar o cursor entre janelas.</p>
    <h3>O notch encobre ícones da barra de menus.</h3>
    <p>Com muitos ícones, o notch pode esconder alguns. Use um gerenciador de barra de menus como Ice ou Bartender.</p>
    <h3>Os recursos de IA não aparecem.</h3>
    <p>O Apple Intelligence requer macOS 15 (Sequoia) ou mais recente em Apple Silicon. Os demais widgets continuam funcionando.</p>""",
        "related": [
            ("/pt-br/learn/best-macos-notch-apps/", "Os melhores apps de notch para macOS", "Seleção 2026."),
            ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglês — o básico."),
            ("/pt-br/", "Início do NotchNest", "Para a página inicial em português."),
        ],
    },
    "pt-PT": {
        "title": "Como usar o notch do MacBook — NotchNest",
        "description": "Transforme o notch vazio do MacBook numa central de produtividade em três passos. Calendário, área de transferência, notas, Pomodoro, música e AirDrop, a um cursor de distância.",
        "og_title": "Como usar o notch do MacBook", "og_desc": "Três passos para um notch útil.",
        "jsonld_headline": "Como usar o notch do MacBook",
        "jsonld_desc": "Transforme o notch vazio do MacBook numa central de produtividade com calendário, área de transferência, notas, Pomodoro, música e AirDrop.",
        "kicker": "Guia", "h1": "Como usar o notch do MacBook",
        "lede": "Três passos, noventa segundos. Transforme o notch vazio do seu MacBook Pro ou MacBook Air numa central de produtividade para calendário, área de transferência, notas, Pomodoro, música e AirDrop.",
        "readtime": "5 min de leitura", "crumb_this": "Usar o notch",
        "howto_name": "Como usar o notch do MacBook",
        "howto_steps": [
            ("Instalar o NotchNest", "Descarregue o NotchNest gratuitamente na Mac App Store. Abra a app uma vez."),
            ("Conceder permissões", "Confirme o acesso a calendário, notas e música. Todas as permissões são opcionais."),
            ("Passar o cursor sobre o notch", "Leve o cursor até ao notch. O painel de vidro abre. Escolha os widgets nas definições."),
        ],
        "faq": [
            ("Preciso de ativar o notch primeiro?", "Não. O notch é hardware. O macOS trata-o como parte da barra de menus. Instale uma app de notch como o NotchNest para o tornar interativo."),
            ("Porque não acontece nada ao passar o cursor?", "Sem uma app de notch, passar o cursor não faz nada — o macOS não tem interface de notch. Instale NotchNest, Boring Notch ou NotchDrop para o comportamento ao passar o cursor."),
            ("Usar o notch consome bateria?", "As apps de notch nativas em SwiftUI adormecem quando o painel está fechado e usam poucos MB de RAM. Sem impacto percetível na bateria em uso normal."),
            ("Posso abrir o painel sem rato?", "Sim — o NotchNest suporta um atalho global. Configure em Definições → Acionadores."),
        ],
        "body": """<p>Por predefinição, o notch do MacBook não faz <strong>nada</strong> — é um espaço para a câmara. A Apple não inclui qualquer interface de notch. As apps de terceiros preenchem a lacuna. O caminho mais rápido de «recorte ignorado» a «realmente útil» é o NotchNest, gratuito na Mac App Store.</p>

    <h2>Passo 1 — Instalar o NotchNest</h2>
    <p>Abra a Mac App Store, procure «NotchNest», instale. Gratuito. Assinado e notarizado pela Apple, em sandbox automaticamente. Requer macOS 14 (Sonoma) ou mais recente; Apple Silicon recomendado para as funcionalidades de IA.</p>
    <p>Depois de instalar, abra uma vez. O macOS regista-o nos itens de início de sessão para que abra automaticamente.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>Instalar o NotchNest</h3>
        <p>Gratuito na Mac App Store. macOS 14+. Sem conta, sem subscrição.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>

    <h2>Passo 2 — Conceder permissões</h2>
    <p>O NotchNest pede permissões conforme necessário — nunca todas de uma vez. Cada uma pode ser ignorada:</p>
    <ul>
      <li><strong>Calendário</strong> — para o widget de agenda do dia e os briefings de IA.</li>
      <li><strong>Notas</strong> — para as notas rápidas que sincronizam com o Apple Notes.</li>
      <li><strong>Música / Spotify</strong> — para o controlo de reprodução.</li>
      <li><strong>Apple Intelligence</strong> — para reformular a área de transferência, os briefings de calendário e o aperfeiçoamento de notas. Tudo no dispositivo.</li>
      <li><strong>Fotografias / Câmara</strong> — para o widget de espelho da câmara.</li>
    </ul>
    <p>Nada é enviado. O NotchNest é uma app da Mac App Store — não pode fazer pedidos de rede além dos esperados.</p>

    <h2>Passo 3 — Passar o cursor sobre o notch</h2>
    <p>Leve o cursor diretamente ao notch. O painel abre — uma superfície de vidro que emoldura o notch com widgets de ambos os lados. Clique num widget para usar; clique fora para fechar.</p>
    <p>Não quer o acionamento ao passar o cursor? <strong>NotchNest → Definições → Acionadores</strong> permite só clique ou um atalho global (predefinição: F1). Também pode manter o painel sempre aberto.</p>

    <h2>Escolher os widgets</h2>
    <p>Definições → Widgets. Cada widget é independente. Ative apenas o que precisar:</p>
    <ul>
      <li><strong>Área de transferência com IA</strong> — histórico pesquisável, fixados, reformulação por IA.</li>
      <li><strong>AirDrop / Tabuleiro de ficheiros</strong> — arraste um ficheiro para o notch e encaminhe.</li>
      <li><strong>Favoritos</strong> — URLs e apps para abrir com um clique.</li>
      <li><strong>Calendário</strong> — agenda do dia com briefings de IA.</li>
      <li><strong>Espelho da câmara</strong> — pré-visualização da webcam com um toque.</li>
      <li><strong>Música</strong> — Spotify e Apple Music com capa.</li>
      <li><strong>Pomodoro</strong> — temporizador de foco com pausas e sequência.</li>
      <li><strong>Notas rápidas</strong> — captura, aperfeiçoamento por IA, sincronização com Apple Notes.</li>
    </ul>

    <h2>Se o seu Mac não tem notch</h2>
    <p>O NotchNest funciona à mesma. Em MacBook Air M1, MacBook Pro antigos, Mac mini, iMac e Mac Studio aparece como um painel fino no topo central do ecrã. Os mesmos widgets, os mesmos atalhos.</p>

    <h2>Problemas comuns</h2>
    <h3>O painel não abre ao passar o cursor.</h3>
    <p><strong>Definições do Sistema → Privacidade e Segurança → Acessibilidade</strong> — ative o NotchNest. O macOS exige isto para os acionadores ao passar o cursor entre janelas.</p>
    <h3>O notch tapa ícones da barra de menus.</h3>
    <p>Com muitos ícones, o notch pode esconder alguns. Use um gestor de barra de menus como o Ice ou o Bartender.</p>
    <h3>As funcionalidades de IA não aparecem.</h3>
    <p>O Apple Intelligence requer macOS 15 (Sequoia) ou mais recente em Apple Silicon. Os restantes widgets continuam a funcionar.</p>""",
        "related": [
            ("/pt-pt/learn/best-macos-notch-apps/", "As melhores aplicações de notch para macOS", "Seleção 2026."),
            ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "Inglês — o básico."),
            ("/pt-pt/", "Início do NotchNest", "Para a página inicial em português."),
        ],
    },
    "ar": {
        "title": "كيفية استخدام نتش الماك بوك — NotchNest",
        "description": "حوّل نتش الماك بوك الفارغ إلى مركز إنتاجية في ثلاث خطوات. تقويم وحافظة وملاحظات وبومودورو وموسيقى وAirDrop، على بُعد تمريرة واحدة.",
        "og_title": "كيفية استخدام نتش الماك بوك", "og_desc": "ثلاث خطوات نحو نتش مفيد.",
        "jsonld_headline": "كيفية استخدام نتش الماك بوك",
        "jsonld_desc": "حوّل نتش الماك بوك الفارغ إلى مركز إنتاجية مع تقويم وحافظة وملاحظات وبومودورو وموسيقى وAirDrop.",
        "kicker": "دليل", "h1": "كيفية استخدام نتش الماك بوك",
        "lede": "ثلاث خطوات، تسعون ثانية. حوّل نتش الماك بوك برو أو الماك بوك إير الفارغ إلى مركز إنتاجية للتقويم والحافظة والملاحظات وبومودورو والموسيقى وAirDrop.",
        "readtime": "قراءة 5 دقائق", "crumb_this": "استخدام النتش",
        "howto_name": "كيفية استخدام نتش الماك بوك",
        "howto_steps": [
            ("تثبيت NotchNest", "نزّل NotchNest مجانًا من Mac App Store. افتح التطبيق مرة واحدة."),
            ("منح الأذونات", "أكّد الوصول إلى التقويم والملاحظات والموسيقى. جميع الأذونات اختيارية."),
            ("مرّر المؤشر فوق النتش", "حرّك المؤشر إلى النتش. تفتح اللوحة الزجاجية. اختر الأدوات من الإعدادات."),
        ],
        "faq": [
            ("هل يجب تفعيل النتش أولًا؟", "لا. النتش جزء من العتاد. يتعامل معه macOS كجزء من شريط القوائم. ثبّت تطبيق نتش مثل NotchNest لجعله تفاعليًا."),
            ("لماذا لا يحدث شيء عند التمرير؟", "بدون تطبيق نتش، لا يفعل التمرير شيئًا — لا يملك macOS نفسه واجهة نتش. ثبّت NotchNest أو Boring Notch أو NotchDrop للحصول على سلوك التمرير."),
            ("هل يستهلك استخدام النتش البطارية؟", "تطبيقات النتش الأصلية بـ SwiftUI تنام عند إغلاق اللوحة وتستخدم بضعة ميغابايت من الذاكرة. لا تأثير ملموس على البطارية في الاستخدام العادي."),
            ("هل يمكنني فتح اللوحة بدون فأرة؟", "نعم — يدعم NotchNest اختصارًا عامًا. اضبطه من الإعدادات ← المُشغّلات."),
        ],
        "body": """<p>افتراضيًا، لا يفعل نتش الماك بوك <strong>شيئًا</strong> — إنه مساحة للكاميرا. لا توفّر Apple أي واجهة للنتش. تسدّ تطبيقات الطرف الثالث الفراغ. وأسرع طريق من «فجوة مُتجاهَلة» إلى «مفيد فعلًا» هو NotchNest، مجانًا على Mac App Store.</p>

    <h2>الخطوة 1 — تثبيت NotchNest</h2>
    <p>افتح Mac App Store، وابحث عن «NotchNest»، وثبّت. مجاني. موقّع وموثّق من Apple، ومعزول تلقائيًا. يتطلب macOS 14 (Sonoma) أو أحدث؛ يُنصح بـ Apple Silicon لميزات الذكاء الاصطناعي.</p>
    <p>بعد التثبيت، افتحه مرة واحدة. يسجّله macOS في عناصر تسجيل الدخول ليعمل تلقائيًا عند البدء.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>تثبيت NotchNest</h3>
        <p>مجانًا على Mac App Store. macOS 14+. بلا حساب، بلا اشتراك.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>

    <h2>الخطوة 2 — منح الأذونات</h2>
    <p>يطلب NotchNest الأذونات عند الحاجة — لا جميعها دفعة واحدة. يمكن تخطّي كل منها:</p>
    <ul>
      <li><strong>التقويم</strong> — لأداة جدول اليوم وملخصات الذكاء الاصطناعي.</li>
      <li><strong>الملاحظات</strong> — للملاحظات السريعة التي تتزامن مع Apple Notes.</li>
      <li><strong>الموسيقى / Spotify</strong> — للتحكم في التشغيل.</li>
      <li><strong>Apple Intelligence</strong> — لإعادة صياغة الحافظة وملخصات التقويم وتحسين الملاحظات. كل ذلك على الجهاز.</li>
      <li><strong>الصور / الكاميرا</strong> — لأداة مرآة الكاميرا.</li>
    </ul>
    <p>لا يُرفع أي شيء. NotchNest تطبيق من Mac App Store — لا يمكنه إجراء طلبات شبكة خارج المتوقع.</p>

    <h2>الخطوة 3 — تمرير المؤشر فوق النتش</h2>
    <p>حرّك المؤشر مباشرة إلى النتش. تنفتح اللوحة — سطح زجاجي يؤطّر النتش بأدوات على الجانبين. انقر أداة لاستخدامها؛ انقر خارجها للإغلاق.</p>
    <p>لا تريد التشغيل بالتمرير؟ <strong>NotchNest ← الإعدادات ← المُشغّلات</strong> يتيح النقر فقط أو اختصارًا عامًا (الافتراضي: F1). يمكنك أيضًا إبقاء اللوحة مفتوحة دائمًا.</p>

    <h2>اختيار الأدوات</h2>
    <p>الإعدادات ← الأدوات. كل أداة مستقلة. فعّل ما تحتاجه فقط:</p>
    <ul>
      <li><strong>حافظة بالذكاء الاصطناعي</strong> — سجل قابل للبحث وتثبيت وإعادة صياغة بالذكاء الاصطناعي.</li>
      <li><strong>AirDrop / درج الملفات</strong> — اسحب ملفًا إلى النتش ثم أرسله.</li>
      <li><strong>الإشارات المرجعية</strong> — روابط وتطبيقات للفتح بنقرة واحدة.</li>
      <li><strong>التقويم</strong> — جدول اليوم مع ملخصات الذكاء الاصطناعي.</li>
      <li><strong>مرآة الكاميرا</strong> — معاينة الكاميرا بلمسة واحدة.</li>
      <li><strong>الموسيقى</strong> — Spotify وApple Music مع صورة الألبوم.</li>
      <li><strong>بومودورو</strong> — مؤقت تركيز مع استراحات وسلسلة.</li>
      <li><strong>الملاحظات السريعة</strong> — التقاط وتحسين بالذكاء الاصطناعي ومزامنة مع Apple Notes.</li>
    </ul>

    <h2>إذا كان الماك لديك بلا نتش</h2>
    <p>يعمل NotchNest رغم ذلك. على الماك بوك إير M1 وأجهزة الماك بوك برو الأقدم وMac mini وiMac وMac Studio يظهر كلوحة رفيعة أعلى منتصف الشاشة. الأدوات نفسها والاختصارات نفسها.</p>

    <h2>مشكلات شائعة</h2>
    <h3>اللوحة لا تفتح عند التمرير.</h3>
    <p><strong>إعدادات النظام ← الخصوصية والأمان ← تسهيلات الاستخدام</strong> — فعّل NotchNest. يشترط macOS ذلك لمُشغّلات التمرير عبر النوافذ.</p>
    <h3>النتش يحجب أيقونات شريط القوائم.</h3>
    <p>مع كثرة الأيقونات قد يخفي النتش بعضها. استخدم مدير شريط قوائم مثل Ice أو Bartender.</p>
    <h3>ميزات الذكاء الاصطناعي لا تظهر.</h3>
    <p>يتطلب Apple Intelligence نظام macOS 15 (Sequoia) أو أحدث على Apple Silicon. تظل بقية الأدوات تعمل.</p>""",
        "related": [
            ("/ar/learn/best-macos-notch-apps/", "أفضل تطبيقات النتش لنظام macOS", "اختيارات 2026."),
            ("/learn/what-is-the-macos-notch/", "What is the macOS notch?", "إنجليزي — الأساسيات."),
            ("/ar/", "الصفحة الرئيسية لـ NotchNest", "إلى الصفحة الرئيسية العربية."),
        ],
    },
}

# ── best-macos-notch-apps ───────────────────────────────────────────────────
BEST = {
    "fr": {
        "title": "Les meilleures apps d'encoche macOS (2026) — NotchNest",
        "description": "Les meilleures apps d'encoche macOS en 2026 — hubs de productivité, contrôleurs multimédia, dépôts de fichiers pour MacBook Pro et Air.",
        "og_title": "Les meilleures apps d'encoche macOS (2026)", "og_desc": "Sélection des meilleurs outils d'encoche pour MacBook en 2026.",
        "jsonld_headline": "Les meilleures apps d'encoche macOS (2026)",
        "jsonld_desc": "Sélection éditoriale des meilleures apps d'encoche pour MacBook Pro et Air en 2026.",
        "kicker": "Sélection", "h1": "Les meilleures apps d'encoche macOS (2026)",
        "lede": "La catégorie des utilitaires d'encoche a mûri. Voici les apps qui valent vraiment le coup en 2026 — hubs de productivité polyvalents, contrôleurs multimédia ciblés, quelques spécialistes.",
        "readtime": "6 min de lecture", "crumb_this": "Meilleures apps d'encoche",
        "faq": [
            ("Quelle est la meilleure app d'encoche gratuite pour Mac ?", "NotchNest est l'app gratuite la plus polyvalente — dix widgets dont calendrier, presse-papiers IA, notes, Pomodoro, musique et AirDrop. Boring Notch est un excellent choix gratuit mono-usage pour le contrôle multimédia."),
            ("Les apps d'encoche sont-elles sûres ?", "Les apps d'encoche du Mac App Store comme NotchNest sont notarisées, signées et en bac à sable — l'option la plus sûre. Les téléchargements directs depuis GitHub (Boring Notch, NotchNook) sont fiables mais pas en bac à sable."),
            ("Les apps d'encoche fonctionnent-elles sans encoche ?", "Certaines. NotchNest s'affiche sur les MacBook sans encoche comme un panneau fin en haut. Boring Notch est spécifique à l'encoche. NotchDrop fonctionne des deux côtés."),
            ("Les apps d'encoche ralentissent-elles le Mac ?", "Les apps d'encoche SwiftUI natives utilisent quelques Mo de RAM et restent à zéro CPU quand le panneau est fermé. Aucun impact mesurable sur la batterie ou les performances."),
        ],
        "body": """<p>Si vous avez un MacBook à encoche et n'avez jamais installé d'app d'encoche, vous n'exploitez peut-être que 20 % de ce que le matériel permet. Apple livre l'encoche comme un espace décoratif ; les apps tierces la rendent utile. Voici les meilleurs choix en trois catégories.</p>

    <h2>Meilleure tout-en-un : NotchNest</h2>
    <p><strong>Ce qu'elle fait :</strong> réunit dix outils dans l'encoche — presse-papiers IA, calendrier avec briefings IA, notes rapides avec affinage IA, minuteur Pomodoro, contrôle Spotify/Apple Music, glisser-vers-AirDrop, bac à fichiers, miroir caméra, favoris, un mini-jeu Infinity Run.</p>
    <p><strong>Pourquoi ici :</strong> la seule app du Mac App Store en bac à sable qui réunit widgets de productivité, contrôle multimédia et AirDrop dans un panneau au survol. Les fonctions IA tournent entièrement sur l'appareil via Apple Intelligence.</p>
    <p><strong>Prix :</strong> gratuit. <strong>Installation :</strong> <a href="%STORE%" target="_blank" rel="noopener">Mac App Store</a>.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>NotchNest — gratuit sur le Mac App Store</h3>
        <p>Dix outils. Une encoche. macOS 14+.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Télécharger sur le Mac App Store" /></a>
    </div>

    <h2>Meilleure pour le multimédia : Boring Notch</h2>
    <p><strong>Ce qu'elle fait :</strong> contrôle multimédia façon Dynamic Island autour de l'encoche, avec batterie des AirPods, pochette en lecture et animations soignées.</p>
    <p><strong>Pourquoi ici :</strong> pour qui vit dans la musique et la vidéo sans avoir besoin de widgets de productivité — l'interface multimédia de Boring Notch est la meilleure de sa catégorie. Open source. Gratuit.</p>
    <p><strong>Inconvénient :</strong> téléchargement direct depuis GitHub, pas en bac à sable. Pas de calendrier, pas de notes, pas d'AirDrop.</p>

    <h2>Meilleure pour les fichiers : NotchDrop</h2>
    <p><strong>Ce qu'elle fait :</strong> transforme l'encoche en bac de glisser-déposer. Déposez un fichier sur l'encoche, puis transférez-le vers des apps, AirDrop ou des services d'upload.</p>
    <p><strong>Pourquoi ici :</strong> pour qui déplace des fichiers toute la journée — designers, monteurs, quiconque utilise AirDrop dix fois par jour — le modèle de bac de NotchDrop est le plus propre.</p>
    <p><strong>Prix :</strong> gratuit avec un palier Pro.</p>

    <h2>À signaler aussi</h2>
    <h3>NotchNook</h3>
    <p>Pionnier de la catégorie. Payant, belle interface, avec bac à fichiers et musique. Mi-2026, pas de grosse mise à jour depuis des mois.</p>
    <h3>Alcove</h3>
    <p>Léger et minimal. Axé musique avec des animations élégantes. Ensemble de widgets plus réduit que NotchNest.</p>
    <h3>TopNotch</h3>
    <p>Autre catégorie : cache l'encoche derrière une barre noire. Gratuit. Si vous voulez faire disparaître l'encoche — nous soutenons plutôt qu'il vaut mieux la rendre utile.</p>

    <h2>Comment nous avons choisi</h2>
    <ol>
      <li><strong>Mérite-t-elle l'encoche ?</strong> L'app ajoute-t-elle vraiment de la fonction, pas juste de la déco ?</li>
      <li><strong>Digne de confiance ?</strong> App de l'App Store en bac à sable ou projet GitHub open source connu.</li>
      <li><strong>Sait-elle se faire discrète ?</strong> Les panneaux d'encoche doivent apparaître quand on les veut et disparaître sinon.</li>
    </ol>

    <h2>Le verdict honnête</h2>
    <p>Pour la plupart des gens, <a href="/fr/">NotchNest</a> suffit — il couvre le terrain des autres apps et ajoute des outils de productivité qu'aucune autre n'a. Pour qui veut uniquement la musique ou le bac à fichiers, Boring Notch et NotchDrop sont d'excellents spécialistes.</p>""",
        "related": [
            ("/fr/learn/how-to-use-the-macbook-notch/", "Utiliser l'encoche du MacBook", "Trois étapes vers une encoche utile."),
            ("/learn/notch-nest-vs-boring-notch-vs-notchdrop/", "NotchNest vs Boring Notch vs NotchDrop", "Comparatif anglais."),
            ("/fr/", "Accueil NotchNest", "Page d'accueil française."),
        ],
    },
    "es-MX": {
        "title": "Las mejores apps de notch para macOS (2026) — NotchNest",
        "description": "Las mejores apps de notch para macOS en 2026: centros de productividad, controladores multimedia y bandejas de archivos para MacBook Pro y Air.",
        "og_title": "Las mejores apps de notch para macOS (2026)", "og_desc": "Selección de las mejores herramientas de notch para MacBook en 2026.",
        "jsonld_headline": "Las mejores apps de notch para macOS (2026)",
        "jsonld_desc": "Selección editorial de las mejores apps de notch para MacBook Pro y Air en 2026.",
        "kicker": "Selección", "h1": "Las mejores apps de notch para macOS (2026)",
        "lede": "La categoría de utilidades de notch maduró. Estas son las apps que de verdad valen la pena en 2026: centros de productividad versátiles, controladores multimedia enfocados y algunos especialistas.",
        "readtime": "6 min de lectura", "crumb_this": "Mejores apps de notch",
        "faq": [
            ("¿Cuál es la mejor app de notch gratis para Mac?", "NotchNest es la app gratuita más versátil: diez widgets, incluidos calendario, portapapeles con IA, notas, Pomodoro, música y AirDrop. Boring Notch es una gran opción gratuita de un solo propósito para el control multimedia."),
            ("¿Las apps de notch son seguras?", "Las apps de notch del Mac App Store como NotchNest están notarizadas, firmadas y en entorno aislado: la opción más segura. Las descargas directas de GitHub (Boring Notch, NotchNook) también son de confianza, pero no están aisladas."),
            ("¿Las apps de notch funcionan sin notch?", "Algunas. NotchNest aparece en MacBooks sin notch como un panel delgado arriba. Boring Notch es específico de notch. NotchDrop funciona en ambos casos."),
            ("¿Las apps de notch ralentizan el Mac?", "Las apps de notch nativas en SwiftUI usan unos pocos MB de RAM y quedan a cero de CPU con el panel cerrado. Sin impacto medible en batería o rendimiento."),
        ],
        "body": """<p>Si tienes un MacBook con notch y nunca instalaste una app de notch, quizá usas solo el 20 % de lo que el hardware permite. Apple entrega el notch como espacio decorativo; las apps de terceros lo hacen útil. Estas son las mejores opciones en tres categorías.</p>

    <h2>Mejor todo en uno: NotchNest</h2>
    <p><strong>Qué hace:</strong> reúne diez herramientas en el notch: portapapeles con IA, calendario con briefings de IA, notas rápidas con refinado por IA, temporizador Pomodoro, control de Spotify/Apple Music, arrastrar a AirDrop, bandeja de archivos, espejo de cámara, favoritos y un minijuego Infinity Run.</p>
    <p><strong>Por qué aquí:</strong> la única app del Mac App Store en entorno aislado que reúne widgets de productividad, control multimedia y AirDrop en un panel al pasar el cursor. Las funciones de IA corren por completo en el dispositivo con Apple Intelligence.</p>
    <p><strong>Precio:</strong> gratis. <strong>Instalación:</strong> <a href="%STORE%" target="_blank" rel="noopener">Mac App Store</a>.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>NotchNest — gratis en el Mac App Store</h3>
        <p>Diez herramientas. Un notch. macOS 14+.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descargar en el Mac App Store" /></a>
    </div>

    <h2>Mejor para multimedia: Boring Notch</h2>
    <p><strong>Qué hace:</strong> control multimedia estilo Dynamic Island alrededor del notch, con batería de los AirPods, carátula en reproducción y animaciones cuidadas.</p>
    <p><strong>Por qué aquí:</strong> para quien vive en la música y el video sin necesitar widgets de productividad, la interfaz multimedia de Boring Notch es la mejor de su clase. Código abierto. Gratis.</p>
    <p><strong>Desventaja:</strong> descarga directa desde GitHub, no aislada. Sin calendario, sin notas, sin AirDrop.</p>

    <h2>Mejor para archivos: NotchDrop</h2>
    <p><strong>Qué hace:</strong> convierte el notch en una bandeja de arrastrar y soltar. Suelta un archivo en el notch y reenvíalo a apps, AirDrop o servicios de subida.</p>
    <p><strong>Por qué aquí:</strong> para quien mueve archivos todo el día — diseñadores, editores, quien usa AirDrop diez veces al día — el modelo de bandeja de NotchDrop es el más limpio.</p>
    <p><strong>Precio:</strong> gratis con nivel Pro.</p>

    <h2>Menciones destacadas</h2>
    <h3>NotchNook</h3>
    <p>Pionero de la categoría. De pago, interfaz bonita, con bandeja de archivos y música. A mediados de 2026, sin una gran actualización desde hace meses.</p>
    <h3>Alcove</h3>
    <p>Ligero y minimalista. Enfocado en música con animaciones elegantes. Conjunto de widgets menor que NotchNest.</p>
    <h3>TopNotch</h3>
    <p>Otra categoría: oculta el notch tras una barra negra. Gratis. Si quieres quitarte el notch de encima — aunque nosotros sostenemos que es mejor hacerlo útil.</p>

    <h2>Cómo elegimos</h2>
    <ol>
      <li><strong>¿Merece el notch?</strong> ¿La app añade función real, no solo decoración?</li>
      <li><strong>¿Confiable?</strong> App del App Store en entorno aislado o proyecto de GitHub de código abierto conocido.</li>
      <li><strong>¿Sabe hacerse a un lado?</strong> Los paneles de notch deben aparecer cuando los quieres y desaparecer cuando no.</li>
    </ol>

    <h2>El veredicto honesto</h2>
    <p>Para la mayoría, <a href="/es-mx/">NotchNest</a> basta: cubre el terreno de las otras apps y añade herramientas de productividad que ninguna otra tiene. Para quien quiere solo música o bandeja de archivos, Boring Notch y NotchDrop son especialistas excelentes.</p>""",
        "related": [
            ("/es-mx/learn/how-to-use-the-macbook-notch/", "Usar el notch del MacBook", "Tres pasos hacia un notch útil."),
            ("/learn/notch-nest-vs-boring-notch-vs-notchdrop/", "NotchNest vs Boring Notch vs NotchDrop", "Comparativa en inglés."),
            ("/es-mx/", "Inicio de NotchNest", "Página de inicio en español."),
        ],
    },
    "pt-BR": {
        "title": "Os melhores apps de notch para macOS (2026) — NotchNest",
        "description": "Os melhores apps de notch para macOS em 2026: centrais de produtividade, controladores de mídia e bandejas de arquivos para MacBook Pro e Air.",
        "og_title": "Os melhores apps de notch para macOS (2026)", "og_desc": "Seleção das melhores ferramentas de notch para MacBook em 2026.",
        "jsonld_headline": "Os melhores apps de notch para macOS (2026)",
        "jsonld_desc": "Seleção editorial dos melhores apps de notch para MacBook Pro e Air em 2026.",
        "kicker": "Seleção", "h1": "Os melhores apps de notch para macOS (2026)",
        "lede": "A categoria de utilitários de notch amadureceu. Estes são os apps que realmente valem a pena em 2026: centrais de produtividade versáteis, controladores de mídia focados e alguns especialistas.",
        "readtime": "6 min de leitura", "crumb_this": "Melhores apps de notch",
        "faq": [
            ("Qual é o melhor app de notch grátis para Mac?", "O NotchNest é o app gratuito mais versátil: dez widgets, incluindo calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop. O Boring Notch é uma ótima opção gratuita de propósito único para controle de mídia."),
            ("Os apps de notch são seguros?", "Apps de notch da Mac App Store como o NotchNest são notarizados, assinados e em sandbox: a opção mais segura. Downloads diretos do GitHub (Boring Notch, NotchNook) também são confiáveis, mas não em sandbox."),
            ("Os apps de notch funcionam sem notch?", "Alguns. O NotchNest aparece em MacBooks sem notch como um painel fino no topo. O Boring Notch é específico de notch. O NotchDrop funciona nos dois casos."),
            ("Os apps de notch deixam o Mac lento?", "Apps de notch nativos em SwiftUI usam poucos MB de RAM e ficam em zero de CPU com o painel fechado. Nenhum impacto perceptível em bateria ou desempenho."),
        ],
        "body": """<p>Se você tem um MacBook com notch e nunca instalou um app de notch, talvez use só 20 % do que o hardware permite. A Apple entrega o notch como espaço decorativo; apps de terceiros o tornam útil. Estas são as melhores escolhas em três categorias.</p>

    <h2>Melhor tudo em um: NotchNest</h2>
    <p><strong>O que faz:</strong> reúne dez ferramentas no notch — área de transferência com IA, calendário com briefings de IA, notas rápidas com refinamento por IA, timer Pomodoro, controle de Spotify/Apple Music, arrastar para AirDrop, bandeja de arquivos, espelho da câmera, favoritos e um minijogo Infinity Run.</p>
    <p><strong>Por que aqui:</strong> o único app da Mac App Store em sandbox que reúne widgets de produtividade, controle de mídia e AirDrop num painel ao passar o cursor. Os recursos de IA rodam totalmente no dispositivo com o Apple Intelligence.</p>
    <p><strong>Preço:</strong> grátis. <strong>Instalação:</strong> <a href="%STORE%" target="_blank" rel="noopener">Mac App Store</a>.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>NotchNest — grátis na Mac App Store</h3>
        <p>Dez ferramentas. Um notch. macOS 14+.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Baixar na Mac App Store" /></a>
    </div>

    <h2>Melhor para mídia: Boring Notch</h2>
    <p><strong>O que faz:</strong> controle de mídia estilo Dynamic Island ao redor do notch, com bateria dos AirPods, capa em reprodução e animações caprichadas.</p>
    <p><strong>Por que aqui:</strong> para quem vive na música e no vídeo sem precisar de widgets de produtividade, a interface de mídia do Boring Notch é a melhor da categoria. Código aberto. Grátis.</p>
    <p><strong>Desvantagem:</strong> download direto do GitHub, sem sandbox. Sem calendário, sem notas, sem AirDrop.</p>

    <h2>Melhor para arquivos: NotchDrop</h2>
    <p><strong>O que faz:</strong> transforma o notch em uma bandeja de arrastar e soltar. Solte um arquivo no notch e encaminhe para apps, AirDrop ou serviços de upload.</p>
    <p><strong>Por que aqui:</strong> para quem move arquivos o dia todo — designers, editores, quem usa AirDrop dez vezes por dia — o modelo de bandeja do NotchDrop é o mais limpo.</p>
    <p><strong>Preço:</strong> grátis com nível Pro.</p>

    <h2>Menções honrosas</h2>
    <h3>NotchNook</h3>
    <p>Pioneiro da categoria. Pago, interface bonita, com bandeja de arquivos e música. Em meados de 2026, sem uma grande atualização há meses.</p>
    <h3>Alcove</h3>
    <p>Leve e minimalista. Focado em música com animações elegantes. Conjunto de widgets menor que o NotchNest.</p>
    <h3>TopNotch</h3>
    <p>Outra categoria: esconde o notch atrás de uma barra preta. Grátis. Se você quer se livrar do notch — embora defendamos que é melhor torná-lo útil.</p>

    <h2>Como escolhemos</h2>
    <ol>
      <li><strong>Merece o notch?</strong> O app adiciona função de verdade, não só decoração?</li>
      <li><strong>Confiável?</strong> App da App Store em sandbox ou projeto de código aberto conhecido no GitHub.</li>
      <li><strong>Sabe se conter?</strong> Painéis de notch devem aparecer quando você quer e sumir quando não.</li>
    </ol>

    <h2>O veredito honesto</h2>
    <p>Para a maioria, o <a href="/pt-br/">NotchNest</a> basta — ele cobre o terreno dos outros apps e adiciona ferramentas de produtividade que nenhum outro tem. Para quem quer só música ou bandeja de arquivos, Boring Notch e NotchDrop são especialistas excelentes.</p>""",
        "related": [
            ("/pt-br/learn/how-to-use-the-macbook-notch/", "Usar o notch do MacBook", "Três passos para um notch útil."),
            ("/learn/notch-nest-vs-boring-notch-vs-notchdrop/", "NotchNest vs Boring Notch vs NotchDrop", "Comparativo em inglês."),
            ("/pt-br/", "Início do NotchNest", "Página inicial em português."),
        ],
    },
    "pt-PT": {
        "title": "As melhores aplicações de notch para macOS (2026) — NotchNest",
        "description": "As melhores aplicações de notch para macOS em 2026: centrais de produtividade, controladores de multimédia e tabuleiros de ficheiros para MacBook Pro e Air.",
        "og_title": "As melhores aplicações de notch para macOS (2026)", "og_desc": "Seleção das melhores ferramentas de notch para MacBook em 2026.",
        "jsonld_headline": "As melhores aplicações de notch para macOS (2026)",
        "jsonld_desc": "Seleção editorial das melhores aplicações de notch para MacBook Pro e Air em 2026.",
        "kicker": "Seleção", "h1": "As melhores aplicações de notch para macOS (2026)",
        "lede": "A categoria de utilitários de notch amadureceu. Estas são as aplicações que valem mesmo a pena em 2026: centrais de produtividade versáteis, controladores de multimédia focados e alguns especialistas.",
        "readtime": "6 min de leitura", "crumb_this": "Melhores aplicações de notch",
        "faq": [
            ("Qual é a melhor aplicação de notch gratuita para Mac?", "O NotchNest é a aplicação gratuita mais versátil: dez widgets, incluindo calendário, área de transferência com IA, notas, Pomodoro, música e AirDrop. O Boring Notch é uma ótima opção gratuita de propósito único para controlo de multimédia."),
            ("As aplicações de notch são seguras?", "Aplicações de notch da Mac App Store como o NotchNest são notarizadas, assinadas e em sandbox: a opção mais segura. As transferências diretas do GitHub (Boring Notch, NotchNook) também são de confiança, mas não em sandbox."),
            ("As aplicações de notch funcionam sem notch?", "Algumas. O NotchNest aparece em MacBooks sem notch como um painel fino no topo. O Boring Notch é específico de notch. O NotchDrop funciona nos dois casos."),
            ("As aplicações de notch tornam o Mac mais lento?", "Aplicações de notch nativas em SwiftUI usam poucos MB de RAM e ficam a zero de CPU com o painel fechado. Sem impacto percetível na bateria ou no desempenho."),
        ],
        "body": """<p>Se tem um MacBook com notch e nunca instalou uma aplicação de notch, talvez use apenas 20 % do que o hardware permite. A Apple entrega o notch como espaço decorativo; as aplicações de terceiros tornam-no útil. Estas são as melhores escolhas em três categorias.</p>

    <h2>Melhor tudo-em-um: NotchNest</h2>
    <p><strong>O que faz:</strong> reúne dez ferramentas no notch — área de transferência com IA, calendário com briefings de IA, notas rápidas com aperfeiçoamento por IA, temporizador Pomodoro, controlo de Spotify/Apple Music, arrastar para AirDrop, tabuleiro de ficheiros, espelho da câmara, favoritos e um minijogo Infinity Run.</p>
    <p><strong>Porquê aqui:</strong> a única aplicação da Mac App Store em sandbox que reúne widgets de produtividade, controlo de multimédia e AirDrop num painel ao passar o cursor. As funcionalidades de IA correm totalmente no dispositivo com o Apple Intelligence.</p>
    <p><strong>Preço:</strong> gratuito. <strong>Instalação:</strong> <a href="%STORE%" target="_blank" rel="noopener">Mac App Store</a>.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>NotchNest — gratuito na Mac App Store</h3>
        <p>Dez ferramentas. Um notch. macOS 14+.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="Descarregar na Mac App Store" /></a>
    </div>

    <h2>Melhor para multimédia: Boring Notch</h2>
    <p><strong>O que faz:</strong> controlo de multimédia ao estilo Dynamic Island à volta do notch, com bateria dos AirPods, capa em reprodução e animações cuidadas.</p>
    <p><strong>Porquê aqui:</strong> para quem vive na música e no vídeo sem precisar de widgets de produtividade, a interface de multimédia do Boring Notch é a melhor da categoria. Código aberto. Gratuito.</p>
    <p><strong>Desvantagem:</strong> transferência direta do GitHub, sem sandbox. Sem calendário, sem notas, sem AirDrop.</p>

    <h2>Melhor para ficheiros: NotchDrop</h2>
    <p><strong>O que faz:</strong> transforma o notch num tabuleiro de arrastar e largar. Largue um ficheiro no notch e encaminhe-o para aplicações, AirDrop ou serviços de carregamento.</p>
    <p><strong>Porquê aqui:</strong> para quem move ficheiros o dia todo — designers, editores, quem usa AirDrop dez vezes por dia — o modelo de tabuleiro do NotchDrop é o mais limpo.</p>
    <p><strong>Preço:</strong> gratuito com nível Pro.</p>

    <h2>Menções honrosas</h2>
    <h3>NotchNook</h3>
    <p>Pioneiro da categoria. Pago, interface bonita, com tabuleiro de ficheiros e música. A meio de 2026, sem uma grande atualização há meses.</p>
    <h3>Alcove</h3>
    <p>Leve e minimalista. Focado em música com animações elegantes. Conjunto de widgets menor que o NotchNest.</p>
    <h3>TopNotch</h3>
    <p>Outra categoria: esconde o notch atrás de uma barra preta. Gratuito. Se quer livrar-se do notch — embora defendamos que é melhor torná-lo útil.</p>

    <h2>Como escolhemos</h2>
    <ol>
      <li><strong>Merece o notch?</strong> A aplicação acrescenta função a sério, não só decoração?</li>
      <li><strong>De confiança?</strong> Aplicação da App Store em sandbox ou projeto de código aberto conhecido no GitHub.</li>
      <li><strong>Sabe conter-se?</strong> Os painéis de notch devem aparecer quando os quer e desaparecer quando não.</li>
    </ol>

    <h2>O veredito honesto</h2>
    <p>Para a maioria, o <a href="/pt-pt/">NotchNest</a> chega — cobre o terreno das outras aplicações e acrescenta ferramentas de produtividade que nenhuma outra tem. Para quem quer só música ou tabuleiro de ficheiros, o Boring Notch e o NotchDrop são especialistas excelentes.</p>""",
        "related": [
            ("/pt-pt/learn/how-to-use-the-macbook-notch/", "Usar o notch do MacBook", "Três passos para um notch útil."),
            ("/learn/notch-nest-vs-boring-notch-vs-notchdrop/", "NotchNest vs Boring Notch vs NotchDrop", "Comparação em inglês."),
            ("/pt-pt/", "Início do NotchNest", "Página inicial em português."),
        ],
    },
    "ar": {
        "title": "أفضل تطبيقات النتش لنظام macOS (2026) — NotchNest",
        "description": "أفضل تطبيقات النتش لنظام macOS في 2026: مراكز إنتاجية ومتحكّمات وسائط وأدراج ملفات لأجهزة MacBook Pro وAir.",
        "og_title": "أفضل تطبيقات النتش لنظام macOS (2026)", "og_desc": "اختيارات لأفضل أدوات النتش لأجهزة MacBook في 2026.",
        "jsonld_headline": "أفضل تطبيقات النتش لنظام macOS (2026)",
        "jsonld_desc": "اختيار تحريري لأفضل تطبيقات النتش لأجهزة MacBook Pro وAir في 2026.",
        "kicker": "اختيارات", "h1": "أفضل تطبيقات النتش لنظام macOS (2026)",
        "lede": "نضجت فئة أدوات النتش. هذه هي التطبيقات التي تستحق فعلًا في 2026: مراكز إنتاجية متعددة الاستخدام، ومتحكّمات وسائط مركّزة، وبعض المتخصصين.",
        "readtime": "قراءة 6 دقائق", "crumb_this": "أفضل تطبيقات النتش",
        "faq": [
            ("ما أفضل تطبيق نتش مجاني للماك؟", "NotchNest هو التطبيق المجاني الأكثر تنوعًا — عشر أدوات تشمل التقويم والحافظة بالذكاء الاصطناعي والملاحظات وبومودورو والموسيقى وAirDrop. وBoring Notch خيار مجاني ممتاز أحادي الغرض للتحكم في الوسائط."),
            ("هل تطبيقات النتش آمنة؟", "تطبيقات النتش من Mac App Store مثل NotchNest موثّقة وموقّعة ومعزولة — الخيار الأكثر أمانًا. التنزيلات المباشرة من GitHub (Boring Notch وNotchNook) موثوقة أيضًا لكنها غير معزولة."),
            ("هل تعمل تطبيقات النتش بدون نتش؟", "بعضها. يظهر NotchNest على أجهزة الماك بوك بدون نتش كلوحة رفيعة في الأعلى. Boring Notch خاص بالنتش. NotchDrop يعمل في الحالتين."),
            ("هل تُبطئ تطبيقات النتش الماك؟", "تطبيقات النتش الأصلية بـ SwiftUI تستخدم بضعة ميغابايت من الذاكرة وتبقى عند صفر معالجة عند إغلاق اللوحة. لا تأثير ملموس على البطارية أو الأداء."),
        ],
        "body": """<p>إذا كان لديك ماك بوك بنتش ولم تثبّت تطبيق نتش قط، فقد تستخدم 20 % فقط مما يتيحه العتاد. تقدّم Apple النتش كمساحة زخرفية؛ وتطبيقات الطرف الثالث تجعله مفيدًا. هذه أفضل الاختيارات في ثلاث فئات.</p>

    <h2>الأفضل الكل في واحد: NotchNest</h2>
    <p><strong>ماذا يفعل:</strong> يجمع عشر أدوات في النتش — حافظة بالذكاء الاصطناعي، وتقويم بملخصات ذكية، وملاحظات سريعة بتحسين بالذكاء الاصطناعي، ومؤقت بومودورو، والتحكم في Spotify/Apple Music، والسحب إلى AirDrop، ودرج ملفات، ومرآة كاميرا، وإشارات مرجعية، ولعبة Infinity Run المصغّرة.</p>
    <p><strong>لماذا هنا:</strong> التطبيق الوحيد المعزول من Mac App Store الذي يجمع أدوات الإنتاجية والتحكم في الوسائط وAirDrop في لوحة تظهر بالتمرير. تعمل ميزات الذكاء الاصطناعي بالكامل على الجهاز عبر Apple Intelligence.</p>
    <p><strong>السعر:</strong> مجاني. <strong>التثبيت:</strong> <a href="%STORE%" target="_blank" rel="noopener">Mac App Store</a>.</p>

    <div class="inline-cta">
      <img class="inline-cta-icon" src="/assets/notchnest-icon.png" alt="NotchNest" width="56" height="56" />
      <div class="inline-cta-body">
        <h3>NotchNest — مجانًا على Mac App Store</h3>
        <p>عشر أدوات. نتش واحد. macOS 14+.</p>
      </div>
      <a href="%STORE%" target="_blank" rel="noopener"><img src="/assets/download-appstore.svg" alt="التنزيل من Mac App Store" /></a>
    </div>

    <h2>الأفضل للوسائط: Boring Notch</h2>
    <p><strong>ماذا يفعل:</strong> تحكّم في الوسائط بأسلوب Dynamic Island حول النتش، مع بطارية AirPods وصورة ما يُشغَّل الآن ورسوم متحركة أنيقة.</p>
    <p><strong>لماذا هنا:</strong> لمن يعيش في الموسيقى والفيديو دون حاجة لأدوات إنتاجية — واجهة الوسائط في Boring Notch هي الأفضل في فئتها. مفتوح المصدر. مجاني.</p>
    <p><strong>العيب:</strong> تنزيل مباشر من GitHub، غير معزول. لا تقويم ولا ملاحظات ولا AirDrop.</p>

    <h2>الأفضل للملفات: NotchDrop</h2>
    <p><strong>ماذا يفعل:</strong> يحوّل النتش إلى درج سحب وإفلات. أفلت ملفًا على النتش ثم مرّره إلى التطبيقات أو AirDrop أو خدمات الرفع.</p>
    <p><strong>لماذا هنا:</strong> لمن ينقل الملفات طوال اليوم — المصمّمون والمحرّرون وكل من يستخدم AirDrop عشر مرات يوميًا — نموذج الدرج في NotchDrop هو الأنظف.</p>
    <p><strong>السعر:</strong> مجاني مع مستوى Pro.</p>

    <h2>جديرة بالذكر</h2>
    <h3>NotchNook</h3>
    <p>رائد مبكر للفئة. مدفوع، واجهة جميلة، مع درج ملفات وموسيقى. في منتصف 2026، بلا تحديث كبير منذ أشهر.</p>
    <h3>Alcove</h3>
    <p>خفيف وبسيط. يركّز على الموسيقى برسوم أنيقة. مجموعة أدوات أصغر من NotchNest.</p>
    <h3>TopNotch</h3>
    <p>فئة مختلفة: يخفي النتش خلف شريط أسود. مجاني. إن أردت التخلّص من النتش — لكننا نرى أن جعله مفيدًا أفضل.</p>

    <h2>كيف اخترنا</h2>
    <ol>
      <li><strong>هل يستحق النتش؟</strong> هل يضيف التطبيق وظيفة فعلية، لا مجرد زينة؟</li>
      <li><strong>جدير بالثقة؟</strong> تطبيق معزول من App Store أو مشروع مفتوح المصدر معروف على GitHub.</li>
      <li><strong>هل يعرف كيف يتنحّى؟</strong> ينبغي أن تظهر لوحات النتش حين تريدها وتختفي حين لا تريدها.</li>
    </ol>

    <h2>الحكم الصادق</h2>
    <p>لمعظم الناس، يكفي <a href="/ar/">NotchNest</a> — فهو يغطي مجال التطبيقات الأخرى ويضيف أدوات إنتاجية لا يملكها غيره. ولمن يريد الموسيقى فقط أو درج الملفات، يقدّم Boring Notch وNotchDrop متخصصَين ممتازَين.</p>""",
        "related": [
            ("/ar/learn/how-to-use-the-macbook-notch/", "استخدام نتش الماك بوك", "ثلاث خطوات نحو نتش مفيد."),
            ("/learn/notch-nest-vs-boring-notch-vs-notchdrop/", "NotchNest vs Boring Notch vs NotchDrop", "مقارنة بالإنجليزية."),
            ("/ar/", "الصفحة الرئيسية لـ NotchNest", "الصفحة الرئيسية العربية."),
        ],
    },
}


def _assemble(slug, src, has_howto):
    out = {}
    for loc, d in src.items():
        row = dict(C[loc])
        row.update(d)
        row["author_h3"] = C[loc]["author_h3"]
        row["author_bio"] = (AUTHOR_LONG if has_howto else AUTHOR_SHORT)[loc]
        if has_howto:
            row["howto"] = {"name": d["howto_name"], "steps": d["howto_steps"]}
        out[loc] = row
    return out


ARTICLES = {
    "how-to-use-the-macbook-notch": _assemble("how-to-use-the-macbook-notch", HOWTO, True),
    "best-macos-notch-apps": _assemble("best-macos-notch-apps", BEST, False),
}
