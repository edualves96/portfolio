"""Content for the project pages, English and Portuguese side by side.

Edit text here, then run:  python -I tools/build_projects.py
Each text is a pair: ("English", "Português").
Body blocks: ("p", pair) | ("ul", [pair, ...]) | ("specs", [(pair_label, pair_value), ...])
             | ("table", {"head": [pair, ...], "rows": [[pair, ...], ...]})
             | ("flow", [(pair_title, pair_detail), ...]) | ("note", pair) | ("devices", None) | ("hand", None)
Gallery items: {"src", "w", "h", "kind": "wide" | "phone", "cap": pair}
"""

ORDER = ["ezluga", "upcc", "findyourclub", "hands-3d", "football-bets", "homecontrol", "hand-gestures", "drive-helper"]

PROJECTS = {
    # ------------------------------------------------------------------ EZLuga
    "ezluga": {
        "name": "EZLuga",
        "section": "products",
        "live": ("https://ezluga.pt", ("Visit ezluga.pt", "Visitar ezluga.pt")),
        "lead": (
            "A marketplace where people and companies in Portugal rent out equipment they already own, from a drill to a mini excavator. I co-founded it with a friend and built the product end to end.",
            "Um marketplace onde pessoas e empresas em Portugal alugam o equipamento que já têm, de um berbequim a uma mini escavadora. Cofundei-o com um amigo e construí o produto de ponta a ponta.",
        ),
        "facts": [
            (("Role", "Papel"), ("Co-founder & developer", "Cofundador e programador")),
            (("Team", "Equipa"), ("Two co-founders", "Dois cofundadores")),
            (("Status", "Estado"), ("Live in Portugal", "No ar em Portugal")),
        ],
        "stack": ["React", "TypeScript", "Go", "PostgreSQL", "Redis", "MinIO", "Docker", "Claude API", "Playwright"],
        "cover": {"src": "hero.webp", "w": 1600, "h": 1000, "alt": ("EZLuga home page: search, equipment categories and EZLuga Ads", "Página inicial da EZLuga: pesquisa, categorias de equipamento e EZLuga Ads")},
        "sections": [
            (("The idea", "A ideia"), [
                ("p", (
                    "Most equipment is bought for one job and then sits idle for months. EZLuga lets owners list it and lets anyone nearby find it, compare it and ask for it, with no middleman and no commission. Rental companies get a profile and visibility; private owners get extra income from what they already have.",
                    "A maioria do equipamento é comprado para uma obra e depois fica parado durante meses. A EZLuga deixa os donos anunciá-lo e qualquer pessoa por perto encontrá-lo, compará-lo e pedi-lo, sem intermediários e sem comissões. As empresas de aluguer ganham perfil e visibilidade; os particulares ganham um rendimento extra com o que já têm.",
                )),
            ]),
            (("What I built", "O que construí"), [
                ("ul", [
                    ("Public site in Portuguese, English and Spanish: search by district, category and price, listing pages, favourites, reviews, reports and verified profiles.",
                     "Site público em português, inglês e espanhol: pesquisa por distrito, categoria e preço, páginas de anúncio, favoritos, avaliações, denúncias e perfis verificados."),
                    ("A step-by-step listing wizard that works on a phone and only asks you to sign in when you publish.",
                     "Um assistente de criação de anúncios passo a passo, pensado para o telemóvel, que só pede para iniciar sessão no momento de publicar."),
                    ("A request list: add several items, choose the dates and send everything in one go.",
                     "Uma lista de pedido: juntas vários equipamentos, escolhes as datas e envias tudo de uma vez."),
                    ("EZLuga Facilita: when a search finds nothing, describe what you need and the team looks for it.",
                     "EZLuga Facilita: quando a pesquisa não encontra nada, descreves o que precisas e a equipa procura por ti."),
                    ("A staff admin with three role levels: users, listings, reports, reviews, revenue, promotions, a supplier map and an audit log.",
                     "Um painel de administração com três níveis de permissões: utilizadores, anúncios, denúncias, avaliações, receitas, promoções, um mapa de fornecedores e um registo de auditoria."),
                    ("EZLuga Ads, paid placements for brands, and ZÉ, an AI assistant in testing that asks a few questions, recommends the right machine, searches live listings and drafts the request.",
                     "EZLuga Ads, espaços pagos para marcas, e o ZÉ, um assistente de IA em testes que faz algumas perguntas, recomenda a máquina certa, pesquisa anúncios reais e prepara o pedido."),
                ]),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("Site", "Site"), ("React 18, TypeScript, Vite, TanStack Query, shadcn/ui and Tailwind; its own i18n with a test that keeps the three languages in sync", "React 18, TypeScript, Vite, TanStack Query, shadcn/ui e Tailwind; i18n próprio com um teste que mantém as três línguas alinhadas")),
                    (("Admin", "Admin"), ("React 19 and TypeScript with Recharts; every permission is enforced by the API, not the browser", "React 19 e TypeScript com Recharts; todas as permissões são verificadas pela API, não pelo browser")),
                    (("API", "API"), ("Go with Echo and raw SQL on PostgreSQL 16 (no ORM), Redis for caching and rate limits, MinIO for photos; two databases, product and admin, with separate sign-in", "Go com Echo e SQL puro sobre PostgreSQL 16 (sem ORM), Redis para cache e limites de pedidos, MinIO para fotografias; duas bases de dados, produto e administração, com autenticação separada")),
                    (("Sign-in", "Autenticação"), ("Short-lived access tokens kept in memory, rotating refresh tokens in httpOnly cookies, two-factor codes for staff", "Tokens de acesso de curta duração guardados em memória, refresh tokens rotativos em cookies httpOnly, códigos de dois fatores para a equipa")),
                    (("Services", "Serviços"), ("Eupago payments, Resend email, Web Push notifications, Prometheus metrics", "Pagamentos Eupago, email Resend, notificações Web Push, métricas Prometheus")),
                    (("Quality", "Qualidade"), ("About 90 Go test files, Vitest with property-based tests, a Playwright end-to-end suite, the whole stack in Docker Compose", "Cerca de 90 ficheiros de testes em Go, Vitest com testes baseados em propriedades, uma suite end-to-end em Playwright, todo o sistema em Docker Compose")),
                ]),
            ]),
            (("Beyond the code", "Para lá do código"), [
                ("p", (
                    "A marketplace is half product, half getting the word out, so I built the tools around it too: a supplier map that finds rental companies from the business registry and Google Places (with a quota cap), an Instagram pipeline that renders HTML designs to images with Playwright (more than 50 posts and carousels so far), and a short launch film made in code.",
                    "Um marketplace é metade produto, metade divulgação, por isso também construí as ferramentas à volta: um mapa de fornecedores que encontra empresas de aluguer a partir do registo comercial e do Google Places (com limite de quota), um processo para o Instagram que transforma desenhos em HTML em imagens com o Playwright (mais de 50 publicações e carrosséis até agora) e um pequeno filme de lançamento feito em código.",
                )),
            ]),
        ],
        "gallery": [
            {"src": "search.webp", "w": 1600, "h": 1000, "kind": "wide", "cap": ("Search with filters by place, price and subcategory.", "Pesquisa com filtros por local, preço e subcategoria.")},
            {"src": "listing.webp", "w": 1600, "h": 1000, "kind": "wide", "cap": ("A listing: photos, the advertiser's profile and Add to request list.", "Um anúncio: fotografias, perfil do anunciante e Adicionar ao pedido.")},
            {"src": "request.webp", "w": 1600, "h": 1000, "kind": "wide", "cap": ("Choosing the dates before sending a request.", "Escolher as datas antes de enviar o pedido.")},
            {"src": "facilita.webp", "w": 1600, "h": 1000, "kind": "wide", "cap": ("EZLuga Facilita: describe what you can't find and the team looks for it.", "EZLuga Facilita: descreves o que não encontras e a equipa procura por ti.")},
            {"src": "m-create.webp", "w": 600, "h": 1222, "kind": "phone", "cap": ("Listing wizard on a phone: choosing the category.", "Criar anúncio no telemóvel: escolher a categoria.")},
            {"src": "m-details.webp", "w": 600, "h": 1222, "kind": "phone", "cap": ("Adding photos, title and description.", "Juntar fotografias, título e descrição.")},
            {"src": "m-partners.webp", "w": 600, "h": 1222, "kind": "phone", "cap": ("The page for rental companies that join as partners.", "A página para empresas de aluguer que se juntam como parceiras.")},
        ],
    },

    # ------------------------------------------------------------------ upcc.pt
    "upcc": {
        "name": "upcc.pt",
        "section": "products",
        "live": ("https://upcc.pt", ("Visit upcc.pt", "Visitar upcc.pt")),
        "lead": (
            "A self-protection app for the parish of Caranguejeira, in Leiria: today's warnings, what to do in an emergency and a family plan, in an app anyone can install straight from the website.",
            "Uma app de autoproteção para a freguesia de Caranguejeira, em Leiria: os avisos do dia, o que fazer numa emergência e um plano familiar, numa app que qualquer pessoa instala diretamente a partir do site.",
        ),
        "facts": [
            (("Role", "Papel"), ("Outside developer for the local civil protection unit", "Programador externo para a unidade local de proteção civil")),
            (("Client", "Cliente"), ("Unidade Local de Proteção Civil de Caranguejeira", "Unidade Local de Proteção Civil de Caranguejeira")),
            (("Status", "Estado"), ("Live, installable on Android and iPhone", "No ar, instalável em Android e iPhone")),
        ],
        "stack": ["PWA", "JavaScript", "Service worker", "GitHub Actions", "GitHub Pages", "Pages CMS", "IPMA", "Fogos.pt"],
        "cover": {"phones": [
            {"src": "home.webp", "alt": ("upcc.pt home: no warnings and no fires nearby", "Início do upcc.pt: sem avisos nem incêndios perto")},
            {"src": "avisos.webp", "alt": ("Weather warnings for the Leiria district", "Avisos do tempo para o distrito de Leiria")},
            {"src": "agir.webp", "alt": ("What to do if…: one guide per risk", "O que fazer se…: um guia por risco")},
        ], "w": 600, "h": 1298},
        "sections": [
            (("Why", "Porquê"), [
                ("p", (
                    "When a storm or a wildfire hits, people need clear, local information fast, often on a bad connection. I built this app for the Unidade Local de Proteção Civil de Caranguejeira as an outside developer: the unit owns the content and the message, I build and run the app.",
                    "Quando chega uma tempestade ou um incêndio, as pessoas precisam de informação clara e local, depressa, muitas vezes com pouca rede. Construí esta app para a Unidade Local de Proteção Civil de Caranguejeira como programador externo: o conteúdo e a mensagem são da unidade, eu construo e mantenho a app.",
                )),
            ]),
            (("What it does", "O que faz"), [
                ("ul", [
                    ("Home shows the situation now: IPMA weather warnings for the district and active wildfires from Fogos.pt.",
                     "O início mostra a situação agora: avisos do IPMA para o distrito e incêndios ativos do Fogos.pt."),
                    ("'What to do if…' guides for earthquakes, rural fires, floods, extreme heat, storms, cold and more, written from official guidance.",
                     "Guias «O que fazer se…» para sismos, incêndios rurais, cheias, calor extremo, tempestades, frio e outros, escritos a partir das orientações oficiais."),
                    ("Emergency kit and grab-bag checklists that adjust to how many people live in the house, and a family plan with meeting points.",
                     "Listas do kit de emergência e da mochila que se ajustam a quantas pessoas vivem em casa, e um plano familiar com pontos de encontro."),
                    ("A drill timer and a short quiz to practise, plus 'warn the family', which sends your location by text message.",
                     "Um cronómetro de simulacro e um pequeno quiz para treinar, e «avisar a família», que envia a tua localização por SMS."),
                    ("A call-112 button always at the bottom of the screen.",
                     "Um botão para ligar 112 sempre no fundo do ecrã."),
                ]),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("App", "App"), ("Plain HTML, CSS and JavaScript, no framework; a service worker caches it so it opens without a connection", "HTML, CSS e JavaScript simples, sem framework; um service worker guarda-a em cache para abrir sem rede")),
                    (("Content", "Conteúdo"), ("Kit, contacts, guides and texts are JSON files the unit's editors change through Pages CMS forms; each save is a commit, live about a minute later", "Kit, contactos, guias e textos são ficheiros JSON que os editores da unidade alteram em formulários do Pages CMS; cada gravação é um commit, publicado cerca de um minuto depois")),
                    (("Wildfires", "Incêndios"), ("A GitHub Actions job fetches the Fogos.pt API every 10 minutes with a secret key, so the key never reaches the public app; an external timer keeps it on schedule", "Uma tarefa no GitHub Actions vai buscar a API do Fogos.pt de 10 em 10 minutos com uma chave secreta, para a chave nunca chegar à app pública; um temporizador externo mantém o horário")),
                    (("Trust", "Confiança"), ("Only contacts the unit has confirmed show a number and can be called", "Só os contactos confirmados pela unidade mostram número e podem ser chamados")),
                    (("Hosting", "Alojamento"), ("GitHub Pages on its own domain with HTTPS; installs on Android with one tap and on iPhone with a short guide", "GitHub Pages com domínio próprio e HTTPS; instala-se no Android com um toque e no iPhone com um pequeno guia")),
                ]),
            ]),
        ],
        "gallery": [
            {"src": "home.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Home: no warnings, no fires nearby, and how prepared your family is.", "Início: sem avisos, sem incêndios perto, e quão preparada está a família.")},
            {"src": "avisos.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("IPMA weather warnings for the district, for the next three days.", "Avisos do IPMA para o distrito, nos próximos três dias.")},
            {"src": "fogos.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Active wildfires in the Leiria district, from Fogos.pt.", "Incêndios ativos no distrito de Leiria, do Fogos.pt.")},
            {"src": "agir.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("What to do if…: one guide per risk.", "O que fazer se…: um guia por risco.")},
            {"src": "kit.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Emergency kit: a checklist that adjusts to the household.", "Kit de emergência: uma lista que se ajusta ao agregado.")},
            {"src": "mochila.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Grab bag: what to take if you have to leave in minutes.", "Mochila: o que levar se tiveres de sair em minutos.")},
            {"src": "plano.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Family plan: who lives with you and what each person needs.", "Plano da família: quem vive contigo e o que cada pessoa precisa.")},
            {"src": "simulacro.webp", "w": 600, "h": 1298, "kind": "phone", "cap": ("Drill mode with a timer.", "Simulacro com cronómetro.")},
        ],
    },

    # ------------------------------------------------------------------ FindYourClub
    "findyourclub": {
        "name": "FindYourClub",
        "section": "products",
        "live": ("https://findyourclub.pt", ("Visit findyourclub.pt", "Visitar findyourclub.pt")),
        "lead": (
            "A recruitment platform for sport: players, coaches, clubs and scouts post opportunities, apply and talk, in English and Portuguese. It launches with football and is built for any sport.",
            "Uma plataforma de recrutamento desportivo: jogadores, treinadores, clubes e olheiros publicam oportunidades, candidatam-se e conversam, em inglês e português. Arranca com o futebol e está feita para qualquer desporto.",
        ),
        "facts": [
            (("Role", "Papel"), ("Built solo: product, code, deploy and brand", "Feito a solo: produto, código, deploy e marca")),
            (("Users", "Utilizadores"), ("Players, coaches, clubs and scouts", "Jogadores, treinadores, clubes e olheiros")),
            (("Status", "Estado"), ("Online at findyourclub.pt", "Online em findyourclub.pt")),
        ],
        "stack": [".NET 10", "Blazor WebAssembly", "ASP.NET Core", "EF Core", "SQL Server", "Stripe", "Docker", "Caddy"],
        "cover": {"src": "hero.webp", "w": 1280, "h": 720, "alt": ("An opportunity on FindYourClub: a club looking for a forward (demo data)", "Uma oportunidade no FindYourClub: um clube à procura de um avançado (dados de demonstração)")},
        "sections": [
            (("The idea", "A ideia"), [
                ("p", (
                    "Grassroots and semi-professional sport still recruits through word of mouth and group chats. FindYourClub gives each side a profile and a place to say what they're looking for: a club that needs a goalkeeper coach, a player looking for a team, a scout looking for talent. It comes from my own life in football: I coach goalkeepers, and my first software project in school was a club management app.",
                    "O desporto de formação e semiprofissional ainda recruta de boca em boca e em grupos de mensagens. O FindYourClub dá a cada parte um perfil e um sítio para dizer o que procura: um clube que precisa de treinador de guarda-redes, um jogador à procura de equipa, um olheiro à procura de talento. Vem da minha vida no futebol: treino guarda-redes, e o meu primeiro projeto de software na escola foi uma aplicação de gestão de clubes.",
                )),
            ]),
            (("What I built", "O que construí"), [
                ("ul", [
                    ("Four profile types, player, coach, club and scout, with fields for each role, a completion bar and highlight-reel videos.",
                     "Quatro tipos de perfil, jogador, treinador, clube e olheiro, com campos próprios, barra de perfil completo e vídeos de destaques."),
                    ("An opportunity feed with infinite scroll and filters for wage, age, nationality, league level and distance, up to 500 km.",
                     "Um feed de oportunidades com scroll infinito e filtros por salário, idade, nacionalidade, nível de liga e distância, até 500 km."),
                    ("Applications with a chat per application, and ratings from both sides once one is accepted.",
                     "Candidaturas com um chat por candidatura e avaliações das duas partes depois de aceite."),
                    ("Ranks, Bronze to Platinum, that set the limits, a Stripe store to upgrade, boosted and pinned posts, and a 5% affiliate programme.",
                     "Ranks, do Bronze à Platina, que definem os limites, uma loja Stripe para subir de rank, publicações em destaque e afixadas, e um programa de afiliados com 5%."),
                    ("An admin area: post review queue, user management, verified badges and per-rank store settings.",
                     "Uma área de administração: fila de revisão de publicações, gestão de utilizadores, selos de verificado e configuração da loja por rank."),
                    ("Emails in both languages for every key event, and posts that expire on their own through a background worker.",
                     "Emails nas duas línguas para cada momento importante e publicações que expiram sozinhas através de um processo em segundo plano."),
                ]),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("Interface", "Interface"), ("Blazor WebAssembly on .NET 10 with Syncfusion components and English/Portuguese dictionaries", "Blazor WebAssembly em .NET 10 com componentes Syncfusion e dicionários de inglês e português")),
                    (("API", "API"), ("ASP.NET Core with EF Core code-first on SQL Server, ASP.NET Identity and JWT", "ASP.NET Core com EF Core code-first sobre SQL Server, ASP.NET Identity e JWT")),
                    (("Shared", "Partilhado"), ("One project of DTOs and constants used by both the API and the interface", "Um projeto de DTOs e constantes usado pela API e pela interface")),
                    (("Location", "Localização"), ("Profile locations geocoded with Nominatim to power the distance filter", "Localizações dos perfis geocodificadas com o Nominatim para o filtro por distância")),
                    (("Hosting", "Alojamento"), ("Docker Compose on a Hetzner server behind Caddy, deployed with a pull and a rebuild", "Docker Compose num servidor Hetzner atrás do Caddy, publicado com um pull e um rebuild")),
                ]),
            ]),
        ],
        "gallery": [
            {"src": "browse.webp", "w": 700, "h": 720, "kind": "wide", "cap": ("The opportunity feed (demo data).", "O feed de oportunidades (dados de demonstração).")},
            {"src": "dashboard.webp", "w": 1280, "h": 720, "kind": "wide", "cap": ("Dashboard: profile views, post views and applications over seven days.", "Dashboard: visitas ao perfil, às publicações e candidaturas em sete dias.")},
            {"src": "create.webp", "w": 1280, "h": 720, "kind": "wide", "cap": ("Posting an opportunity.", "Publicar uma oportunidade.")},
            {"src": "store.webp", "w": 1280, "h": 720, "kind": "wide", "cap": ("The store: four ranks and what each one unlocks.", "A loja: quatro ranks e o que cada um desbloqueia.")},
            {"src": "soon.webp", "w": 1280, "h": 632, "kind": "wide", "cap": ("The early-access page used before launch.", "A página de acesso antecipado usada antes do lançamento.")},
        ],
    },

    # ------------------------------------------------------------------ Hands 3D
    "hands-3d": {
        "name": "Hands 3D",
        "section": "lab",
        "live": None,
        "lead": (
            "Webcam hand tracking in the browser: put an IKEA LACK table together with your bare hands, pull it apart into a hologram, or draw in the air.",
            "Deteção das mãos pela webcam, no browser: monta uma mesa LACK do IKEA com as mãos, desmonta-a em holograma ou desenha no ar.",
        ),
        "facts": [
            (("Role", "Papel"), ("Personal project", "Projeto pessoal")),
            (("Runs", "Corre"), ("In the browser and as a Windows app", "No browser e como app para Windows")),
            (("Input", "Entrada"), ("Any webcam, or the mouse", "Qualquer webcam, ou o rato")),
        ],
        "stack": ["three.js", "MediaPipe", "TypeScript", "Vite", "Node single executable"],
        "cover": {"src": "hero.webp", "w": 1440, "h": 900, "alt": ("Explode mode: both hands pulling a table apart into a blue hologram", "Modo explodir: as duas mãos a afastar as peças de uma mesa em holograma azul")},
        "sections": [
            (("Why", "Porquê"), [
                ("p", (
                    "It started as one mode of my Hand Gestures desktop app and outgrew it. I wanted to see how far a plain webcam can go as a 3D input device, with no gloves and no depth camera.",
                    "Começou como um modo da minha app Hand Gestures e acabou por crescer sozinho. Queria ver até onde uma webcam normal chega como dispositivo de entrada 3D, sem luvas e sem câmara de profundidade.",
                )),
            ]),
            (("Three modes", "Três modos"), [
                ("ul", [
                    ("Build: the loose pieces lie in a row and a green shape shows where each one goes. Bring a piece there and it snaps in, through the manual's eight steps, with the manual page beside you.",
                     "Montar: as peças soltas estão em fila e uma forma verde mostra onde vai cada uma. Leva a peça até lá e ela encaixa, ao longo dos oito passos do manual, com a página do manual ao lado."),
                    ("Explode: pinch with both hands and pull to take the table apart layer by layer, push together to put it back. Each part shows its real part number.",
                     "Explodir: faz pinça com as duas mãos e puxa para desmontar a mesa camada a camada, junta-as para a voltar a montar. Cada peça mostra o seu número real."),
                    ("Canvas: draw in the air with your index finger, or load a 3D file and move, turn and resize it with pinches.",
                     "Tela: desenha no ar com o indicador, ou abre um ficheiro 3D e move-o, roda-o e redimensiona-o com pinças."),
                    ("No webcam? A mouse mode does the same with clicks.",
                     "Sem webcam? Um modo com rato faz o mesmo com cliques."),
                ]),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("Tracking", "Deteção"), ("MediaPipe hand landmarks through the open-source-hands kit, smoothed every frame", "Pontos das mãos do MediaPipe através do kit open-source-hands, suavizados a cada frame")),
                    (("3D", "3D"), ("three.js scenes per mode; pieces snap by type, so any piece fits any free place of its kind", "Cenas three.js por modo; as peças encaixam por tipo, por isso qualquer peça serve em qualquer lugar livre do seu tipo")),
                    (("Data", "Dados"), ("Part shapes and manual pages from Stanford's IKEA-Manual research dataset (102 products). It has no licence, so it's never bundled: a setup script downloads it on the user's own machine", "Formas das peças e páginas dos manuais do conjunto de dados de investigação IKEA-Manual de Stanford (102 produtos). Não tem licença, por isso nunca é incluído: um script descarrega-o no próprio computador")),
                    (("Desktop", "Desktop"), ("A 140 MB Windows exe (a Node single executable) that serves the app locally and opens it in its own window; a headless check drives the built exe", "Um exe para Windows de 140 MB (um executável único de Node) que serve a app localmente e a abre numa janela própria; um teste sem ecrã controla o exe já construído")),
                ]),
            ]),
        ],
        "gallery": [
            {"src": "holding.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("Holding a piece: the green marker shows where it goes.", "A segurar uma peça: o marcador verde mostra onde encaixa.")},
            {"src": "brackets.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("Step 4 of 8, with the manual page in the corner.", "Passo 4 de 8, com a página do manual no canto.")},
            {"src": "done.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("Finished.", "Montada.")},
            {"src": "manual.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("The manual page at full size.", "A página do manual em tamanho grande.")},
            {"src": "apart.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("All 22 pieces apart, labelled with their part numbers.", "As 22 peças afastadas, com os números das peças.")},
            {"src": "white.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("The same view in light mode.", "A mesma vista em modo claro.")},
            {"src": "draw.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("Canvas: drawing in the air.", "Tela: desenhar no ar.")},
            {"src": "model.webp", "w": 1440, "h": 900, "kind": "wide", "cap": ("Canvas: a 3D model moved and turned with pinches.", "Tela: um modelo 3D movido e rodado com pinças.")},
        ],
    },

    # ------------------------------------------------------------------ Football Bets
    "football-bets": {
        "name": "Football Bets",
        "section": "lab",
        "live": None,
        "lead": (
            "A desktop app that lists today's football games, has a Claude agent analyse the ones you pick and suggest three bets, then keeps score of whether its estimates actually beat the bookmakers'.",
            "Uma app de desktop que lista os jogos de futebol do dia, pede a um agente Claude que analise os que escolhes e sugira três apostas, e depois vai medindo se as estimativas batem mesmo as das casas de apostas.",
        ),
        "facts": [
            (("Role", "Papel"), ("Personal project, for fun with friends", "Projeto pessoal, para diversão entre amigos")),
            (("Runs", "Corre"), ("Windows installer, no admin rights needed", "Instalador para Windows, sem permissões de administrador")),
            (("Cost", "Custo"), ("About 0.2 cents per game analysed", "Cerca de 0,2 cêntimos por jogo analisado")),
        ],
        "stack": ["Electron", "React", "TypeScript", "Claude Haiku", "football-data.org", "API-Football", "Excel export"],
        "cover": {"src": "hero.webp", "w": 1180, "h": 900, "alt": ("Football Bets main screen: today's games, the Mission and recent picks", "Ecrã principal do Football Bets: jogos do dia, a Missão e as escolhas recentes")},
        "sections": [
            (("How an analysis works", "Como funciona uma análise"), [
                ("ul", [
                    ("Gather: standings, recent form and head-to-head from football-data.org; prediction, team stats, injuries and odds from API-Football. Every source is cached and can fail on its own.",
                     "Recolher: classificação, forma recente e confrontos diretos do football-data.org; previsão, estatísticas, lesões e odds da API-Football. Cada fonte tem cache e pode falhar sozinha."),
                    ("Analyse: one Claude Haiku call returns a fixed JSON shape: summary, key factors, data gaps, three bets (low, medium and high risk) and a top pick. The model refers to odds by reference, so it can't invent a number.",
                     "Analisar: uma chamada ao Claude Haiku devolve um JSON com forma fixa: resumo, fatores-chave, dados em falta, três apostas (risco baixo, médio e alto) e uma escolha de topo. O modelo refere as odds por referência, por isso não consegue inventar números."),
                    ("Assess: you type the odd you'd bet at, and the app works out risk and value from the estimated chance and shows the lowest odd still worth taking.",
                     "Avaliar: escreves a odd a que apostarias e a app calcula o risco e o valor a partir da probabilidade estimada e mostra a odd mínima que ainda compensa."),
                ]),
            ]),
            (("Keeping it honest", "Sem ilusões"), [
                ("ul", [
                    ("Learn from results: per risk level, how often bets won against how often the analysis said they would.",
                     "Aprender com os resultados: por nível de risco, quantas apostas ganharam face às que a análise previa."),
                    ("Is the analysis better than the market? Brier scores for the analysis against the bookmakers' own chances with the margin removed.",
                     "A análise é melhor do que o mercado? Brier scores da análise contra as probabilidades das casas de apostas sem margem."),
                    ("Closing line value: compares the odd you took with the last odds before kick-off.",
                     "Closing line value: compara a odd que apanhaste com as últimas odds antes do jogo."),
                    ("A Mission mode with a hard bankroll limit, a weekly report and an assistant chat on every screen.",
                     "Um modo Missão com limite fixo de banca, um relatório semanal e um assistente em conversa em todos os ecrãs."),
                ]),
                ("note", ("Built for fun among friends. It can't make the analysis know more about football; it only shows when it's too sure of itself.",
                          "Feito para diversão entre amigos. Não faz a análise saber mais de futebol; só mostra quando está demasiado confiante.")),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("App", "App"), ("Electron, React and TypeScript with electron-vite; API keys stored encrypted with the operating system's keychain", "Electron, React e TypeScript com electron-vite; chaves de API guardadas encriptadas no cofre do sistema operativo")),
                    (("Limits", "Limites"), ("A rate limiter and a quota guard counted from each API's response headers, with a reserve so the games list always loads; cache per data type, from 10 minutes for odds to 24 hours for head-to-head", "Um limitador de pedidos e um controlo de quota contado a partir dos cabeçalhos de cada API, com reserva para a lista de jogos carregar sempre; cache por tipo de dados, de 10 minutos para odds a 24 horas para confrontos diretos")),
                    (("Data", "Dados"), ("Picks exported to Excel, a daily backup, and the app keeps working in the tray to fetch results", "Escolhas exportadas para Excel, uma cópia de segurança diária, e a app continua no tabuleiro do sistema a buscar resultados")),
                    (("Tests", "Testes"), ("Unit tests for merge logic, odds, risk, cache and quota; a self-test that runs one real analysis; a packaging check that no keys or data end up in the installer", "Testes unitários para junção de dados, odds, risco, cache e quota; um autoteste que corre uma análise real; uma verificação de que nenhuma chave ou dado vai parar ao instalador")),
                ]),
            ]),
        ],
        "gallery": [
            {"src": "suggested.webp", "w": 1180, "h": 900, "kind": "wide", "cap": ("Suggested bets with price badges: green when the odd is at or above its value line.", "Apostas sugeridas com selos de preço: verde quando a odd está na linha de valor ou acima.")},
            {"src": "reliability.webp", "w": 1180, "h": 900, "kind": "wide", "cap": ("Reliability: estimated chance against how often bets really won.", "Fiabilidade: probabilidade estimada face às vezes que as apostas ganharam mesmo.")},
            {"src": "assistant.webp", "w": 1084, "h": 742, "kind": "wide", "cap": ("The assistant: ask for a pick and add it to the Mission.", "O assistente: pede uma escolha e junta-a à Missão.")},
            {"src": "mission.webp", "w": 980, "h": 800, "kind": "wide", "cap": ("Mission: the bankroll over time, in the light theme.", "Missão: a banca ao longo do tempo, no tema claro.")},
            {"src": "mybets.webp", "w": 1180, "h": 900, "kind": "wide", "cap": ("My bets: profit over time and closing line value.", "As minhas apostas: lucro ao longo do tempo e closing line value.")},
        ],
    },

    # ------------------------------------------------------------------ HomeControl
    "homecontrol": {
        "name": "HomeControl",
        "section": "lab",
        "live": None,
        "lead": (
            "One control panel for the living room: the TV, the TV box, three air conditioners and the robot vacuum, on the PC and on our phones, with the same setup everywhere.",
            "Um único painel para a sala: a TV, a box, três ares condicionados e o robô aspirador, no PC e nos nossos telemóveis, com a mesma configuração em todo o lado.",
        ),
        "facts": [
            (("Role", "Papel"), ("Personal project, used at home", "Projeto pessoal, usado em casa")),
            (("Runs", "Corre"), ("Windows app and Android app", "App para Windows e para Android")),
            (("Devices", "Dispositivos"), ("Five brands, five protocols", "Cinco marcas, cinco protocolos")),
        ],
        "stack": ["Python", "aiohttp", "Android", "Chaquopy", "MQTT over mTLS", "PyInstaller", "AES-GCM"],
        "cover": {"fragment": "devices"},
        "sections": [
            (("Why", "Porquê"), [
                ("p", (
                    "Five devices meant five apps, some of them only on one phone. I wanted one page that controls everything on the local network, works for both of us with our own layouts, and keeps working when the router gives a device a new address.",
                    "Cinco dispositivos eram cinco apps, algumas só num telemóvel. Queria uma página que controlasse tudo na rede de casa, servisse os dois com a disposição de cada um e continuasse a funcionar quando o router dá um endereço novo a um dispositivo.",
                )),
            ]),
            (("How each device is controlled", "Como cada dispositivo é controlado"), [
                ("table", {
                    "head": [("Device", "Dispositivo"), ("How", "Como")],
                    "rows": [
                        [("Hisense TV", "TV Hisense"), ("MQTT over mutual TLS with a paired client certificate; Wake-on-LAN to switch it on", "MQTT sobre TLS mútuo com um certificado emparelhado; Wake-on-LAN para a ligar")],
                        [("MEO TV box", "Box MEO"), ("Android TV Remote protocol v2, paired once", "Protocolo Android TV Remote v2, emparelhado uma vez")],
                        [("Two Midea ACs", "Dois AC Midea"), ("Local network on port 6444, with the device key fetched once from the cloud", "Rede local na porta 6444, com a chave do aparelho obtida uma vez na cloud")],
                        [("Samsung AC", "AC Samsung"), ("SmartThings API", "API SmartThings")],
                        [("Roomba", "Roomba"), ("iRobot cloud through its AWS IoT endpoint, since it refuses local control", "Cloud da iRobot através do endpoint AWS IoT, já que recusa controlo local")],
                    ],
                }),
            ]),
            (("What it does", "O que faz"), [
                ("ul", [
                    ("Two profiles, each with a PIN and its own card names, order and hidden cards.",
                     "Dois perfis, cada um com PIN e com os nomes, a ordem e os cartões escondidos que quiser."),
                    ("Every card has More options built from what the device itself reports: modes, sources, apps.",
                     "Cada cartão tem Mais opções construídas a partir do que o próprio aparelho indica: modos, fontes, apps."),
                    ("Finds devices again by MAC address when their IP changes.",
                     "Volta a encontrar os dispositivos pelo endereço MAC quando o IP muda."),
                    ("Sync between the PC and the phones: each setting remembers when it changed and the newest wins, encrypted with a shared passphrase (PBKDF2 and AES-GCM) before it leaves a device.",
                     "Sincronização entre o PC e os telemóveis: cada definição lembra quando mudou e ganha a mais recente, encriptada com uma frase-passe partilhada (PBKDF2 e AES-GCM) antes de sair do aparelho."),
                ]),
            ]),
            (("Under the hood", "Por dentro"), [
                ("specs", [
                    (("PC", "PC"), ("A Python aiohttp server on the machine and one HTML page in an Edge app window; a PyInstaller exe that stays in the tray while phones sync", "Um servidor Python aiohttp no computador e uma página HTML numa janela de app do Edge; um exe PyInstaller que fica no tabuleiro enquanto os telemóveis sincronizam")),
                    (("Android", "Android"), ("The same Python server running inside the phone with Chaquopy, shown in a WebView; a release-signed APK", "O mesmo servidor Python a correr dentro do telemóvel com o Chaquopy, mostrado numa WebView; um APK assinado")),
                    (("Secrets", "Segredos"), ("Windows Credential Manager on the PC, private app storage on Android; device keys are never written to the logs", "Gestor de credenciais do Windows no PC, armazenamento privado da app no Android; as chaves dos aparelhos nunca vão para os logs")),
                ]),
            ]),
        ],
        "gallery": [],
    },

    # ------------------------------------------------------------------ Hand Gestures
    "hand-gestures": {
        "name": "Hand Gestures",
        "section": "lab",
        "live": None,
        "lead": (
            "Control the PC with webcam hand gestures. Face recognition knows who is in front of the camera, switches to their gestures, and locks everything for anyone it doesn't know.",
            "Controla o PC com gestos à frente da webcam. O reconhecimento facial sabe quem está à frente da câmara, muda para os gestos dessa pessoa e bloqueia tudo para quem não conhece.",
        ),
        "facts": [
            (("Role", "Papel"), ("Personal project", "Projeto pessoal")),
            (("Runs", "Corre"), ("Windows app, configured with one JSON file", "App para Windows, configurada com um ficheiro JSON")),
            (("Privacy", "Privacidade"), ("No photos stored", "Não guarda fotografias")),
        ],
        "stack": ["Python", "OpenCV", "MediaPipe", "YuNet", "SFace", "Claude API", "PyInstaller"],
        "cover": {"fragment": "hand"},
        "sections": [
            (("How it works", "Como funciona"), [
                ("ul", [
                    ("Hold a pose for about half a second to fire it, sweep an open hand to switch windows, and chain quick poses into combos.",
                     "Mantém uma pose cerca de meio segundo para a ativar, varre a mão aberta para mudar de janela e encadeia poses rápidas em combos."),
                    ("A profile per person and sub-profiles per context, such as work, media and home, switched by holding an L shape.",
                     "Um perfil por pessoa e subperfis por contexto, como trabalho, multimédia e casa, trocados mantendo a forma de um L."),
                    ("Two-hand gestures, like pointing at your own wrist with the other hand.",
                     "Gestos com as duas mãos, como apontar para o próprio pulso com a outra mão."),
                    ("An on-screen keyboard, and a gesture list in the preview that lights up the pose you're holding.",
                     "Um teclado no ecrã e uma lista de gestos na pré-visualização que acende a pose que estás a fazer."),
                ]),
            ]),
            (("Gesture map", "Mapa de gestos"), [
                ("table", {
                    "head": [("Gesture", "Gesto"), ("Work", "Trabalho"), ("Media", "Multimédia")],
                    "rows": [
                        [("Thumbs up", "Polegar para cima"), ("Opens VS Code", "Abre o VS Code"), ("Volume up", "Aumenta o volume")],
                        [("Call (thumb and pinky)", "Telefone (polegar e mindinho)"), ("Opens SQL Server Management Studio", "Abre o SQL Server Management Studio"), ("Previous track", "Faixa anterior")],
                        [("Peace (index and middle)", "Paz (indicador e médio)"), ("Opens a terminal running Claude Code", "Abre um terminal com o Claude Code"), ("Next track", "Faixa seguinte")],
                        [("Fist", "Punho"), ("Opens the work tab group in Chrome", "Abre o grupo de separadores de trabalho no Chrome"), ("Play / pause", "Reproduzir / pausa")],
                        [("Point (index only)", "Apontar (só indicador)"), ("—", "—"), ("Mute", "Silenciar")],
                    ],
                }),
            ]),
            (("Faces and privacy", "Rostos e privacidade"), [
                ("ul", [
                    ("YuNet finds faces and SFace recognises them, twice a second in the background.",
                     "O YuNet encontra os rostos e o SFace reconhece-os, duas vezes por segundo em segundo plano."),
                    ("Only enrolled people can fire gestures, and with nobody in view for 10 seconds it pauses.",
                     "Só pessoas registadas podem ativar gestos, e se ninguém estiver à frente durante 10 segundos, pausa."),
                    ("No photos are stored: a face becomes a signature of 128 numbers that can't be turned back into a picture, kept outside the project folder.",
                     "Não guarda fotografias: um rosto passa a ser uma assinatura de 128 números que não se consegue voltar a transformar em imagem, guardada fora da pasta do projeto."),
                ]),
            ]),
            (("Canvas and Claude", "Tela e Claude"), [
                ("ul", [
                    ("Canvas mode: draw in the air, or hold an object up with both hands to scan it into a rough 3D model.",
                     "Modo tela: desenha no ar, ou segura um objeto com as duas mãos para o digitalizar num modelo 3D aproximado."),
                    ("Press I and the Claude API identifies the scanned object with web search, finds its manual and a matching 3D model on Sketchfab, Printables or 3dassets.dev, with the author's licence shown.",
                     "Carrega no I e a API do Claude identifica o objeto digitalizado com pesquisa na web, encontra o manual e um modelo 3D no Sketchfab, Printables ou 3dassets.dev, com a licença do autor visível."),
                ]),
            ]),
        ],
        "gallery": [],
    },

    # ------------------------------------------------------------------ Drive Helper
    "drive-helper": {
        "name": "Drive Helper",
        "section": "lab",
        "live": None,
        "lead": (
            "Talk to Alexa and let a Claude agent work with your Google Docs: find a file, read it aloud, summarise it or edit it, with every change waiting for a spoken yes.",
            "Fala com a Alexa e deixa um agente Claude trabalhar com os teus Google Docs: encontrar um ficheiro, lê-lo em voz alta, resumi-lo ou editá-lo, com cada alteração à espera de um «sim» dito em voz alta.",
        ),
        "facts": [
            (("Role", "Papel"), ("Personal prototype", "Protótipo pessoal")),
            (("Status", "Estado"), ("Tested live against Google Docs", "Testado ao vivo com Google Docs")),
            (("Limit", "Limite"), ("Answers inside Alexa's ~8 s window", "Responde dentro da janela de ~8 s da Alexa")),
        ],
        "stack": ["Alexa Skills Kit", "AWS Lambda", "Node.js", "Claude API", "Google Drive API", "Google Docs API"],
        "cover": {"fragment": "flow"},
        "sections": [
            (("How it flows", "Como funciona"), [
                ("flow", [
                    (("You speak", "Falas"), ("“Alexa, ask Drive Helper to read my meeting notes.”", "«Alexa, pede ao Drive Helper para ler as notas da reunião.»")),
                    (("Alexa skill", "Skill da Alexa"), ("Turns speech into text and back.", "Transforma a fala em texto e o texto em fala.")),
                    (("AWS Lambda", "AWS Lambda"), ("A Claude tool-use loop with four tools: search files, read a file, append to a doc, replace in a doc.", "Um ciclo de ferramentas do Claude com quatro ferramentas: pesquisar ficheiros, ler um ficheiro, acrescentar a um doc, substituir num doc.")),
                    (("Google Drive and Docs", "Google Drive e Docs"), ("Through a service account that only sees files you share with it.", "Através de uma conta de serviço que só vê os ficheiros partilhados com ela.")),
                    (("Spoken reply", "Resposta falada"), ("Long documents are read in about one-minute chunks; say “next” to continue.", "Documentos longos são lidos em blocos de cerca de um minuto; diz «seguinte» para continuar.")),
                ]),
            ]),
            (("What you can say", "O que podes dizer"), [
                ("table", {
                    "head": [("You say", "Dizes"), ("What happens", "O que acontece")],
                    "rows": [
                        [("“Find my invoice from March”", "«Encontra a minha fatura de março»"), ("Searches Drive by name and content", "Pesquisa no Drive por nome e conteúdo")],
                        [("“What does the contract say about payment terms?”", "«O que diz o contrato sobre prazos de pagamento?»"), ("Claude reads the file and answers", "O Claude lê o ficheiro e responde")],
                        [("“Summarise the project brief”", "«Resume o briefing do projeto»"), ("A spoken summary", "Um resumo falado")],
                        [("“Add buy milk to my shopping list”", "«Junta comprar leite à lista de compras»"), ("Stages the edit, asks “Should I go ahead?” and writes only after “yes”", "Prepara a alteração, pergunta «Posso avançar?» e só escreve depois do «sim»")],
                    ],
                }),
            ]),
            (("Safety", "Segurança"), [
                ("ul", [
                    ("The service account only sees files explicitly shared with it, only Google Docs can be edited, and there's an optional allow-list of users.",
                     "A conta de serviço só vê ficheiros partilhados explicitamente, só os Google Docs podem ser editados e há uma lista opcional de utilizadores autorizados."),
                    ("Every edit is staged and needs a spoken yes; Google Docs version history is the undo button.",
                     "Cada alteração fica preparada e precisa de um «sim» falado; o histórico de versões do Google Docs é o botão de desfazer."),
                    ("An offline test suite with mocked services, plus a live check against Google; runs on AWS Lambda or as an Alexa-hosted skill.",
                     "Uma suite de testes offline com serviços simulados, mais uma verificação ao vivo com a Google; corre em AWS Lambda ou como skill alojada pela Alexa."),
                ]),
            ]),
        ],
        "gallery": [],
    },
}
