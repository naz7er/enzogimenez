"""Genera el sitio: index.html y una página por proyecto en proyectos/.

Todo el texto vive en este archivo. Para cambiar algo: editar acá y correr
`python tools/build.py`. Los estilos están en styles.css y el movimiento en main.js.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIL = "enzogimenez07.eg@gmail.com"
BEHANCE = "https://www.behance.net/enzogimenez2"
YOUTUBE = "https://www.youtube.com/@osogrosso"

PROJECTS = [
    {
        "slug": "osogrosso",
        "name": "OsoGrosso",
        "kind": "Personaje 3D y canal de YouTube",
        "year": "2026",
        "tile": {"video": "loop-oso.mp4", "poster": "poster-oso.jpg"},
        "lead": "Un canal de YouTube con consejos de gimnasio contados por un oso en 3D: el personaje, la animación, las miniaturas y el arte del canal.",
        "facts": [("Año", "2026"), ("Qué es", "Personaje y canal de YouTube"), ("Formatos", "Shorts verticales y videos largos"), ("Incluye", "Animación 3D, miniaturas y arte del canal")],
        "hero": {
            "type": "shorts",
            "title": "Los shorts",
            "intro": "Consejos de gimnasio en menos de un minuto. Tocá cualquiera para verlo con sonido.",
            "items": [
                ("Creatina", "oso-short-ep11.mp4", "oso-short-ep11.jpg"),
                ("Sentadilla", "oso-short-ep13.mp4", "oso-short-ep13.jpg"),
                ("¿Poleas o pesos libres?", "oso-short-ep14.mp4", "oso-short-ep14.jpg"),
                ("No necesitás 2 horas", "oso-short-ep10.mp4", "oso-short-ep10.jpg"),
            ],
        },
        "sections": [
            {
                "type": "thumbs",
                "title": "Videos largos",
                "intro": "Para los videos largos diseñé miniaturas que se entienden de un vistazo: el oso, una pregunta y un color fuerte.",
                "items": [
                    ("oso-thumb-hombro.jpg", "Tier list de hombro", "Video de 8:42"),
                    ("oso-thumb-calorias.jpg", "¿Cuántas calorías gastás?", "Video de 4:59"),
                ],
            },
            {
                "type": "text-image",
                "title": "El personaje",
                "text": [
                    "Un oso grande y amable, con vincha naranja y fondo azul, para que se reconozca en un segundo en el feed.",
                    "Se mueve como una persona: respira, gesticula cuando habla y reacciona a lo que cuenta.",
                ],
                "image": ("oso-perfil.jpg", "El oso de OsoGrosso con los brazos arriba, dentro de un círculo naranja"),
            },
            {
                "type": "wide",
                "title": "Arte del canal",
                "image": ("oso-banner.jpg", "Banner de YouTube de OsoGrosso: el oso junto al nombre del canal y el lema «Consejos de gym en menos de 1 minuto»"),
                "caption": "Banner del canal de YouTube.",
            },
        ],
        "link": (YOUTUBE, "Ver el canal en YouTube"),
    },
    {
        "slug": "sega-tv",
        "name": "SEGA TV",
        "kind": "Identidad para un canal de TV",
        "year": "2025",
        "tile": {"image": "cover-sega.jpg", "alt": "Portada de SEGA TV: el logo pixelado sobre un fondo de joysticks", "hover": "loop-sega.mp4"},
        "lead": "Un canal de televisión imaginario por los 65 años de SEGA: ocho piezas animadas y un manual de marca, todo en píxeles como las consolas de los 90.",
        "facts": [("Año", "2025"), ("Qué es", "Paquete gráfico para un canal de TV"), ("Incluye", "8 videos y un manual de marca"), ("Programas", "After Effects e Illustrator")],
        "hero": {"type": "video", "src": "full-sega-id.mp4", "poster": "piece-id.jpg", "label": "El ID del canal", "time": "0:21"},
        "cta": "Ver el video",
        "sections": [
            {
                "type": "text-image",
                "title": "La idea",
                "text": [
                    "Volver a las raíces de la marca para celebrar su historia. Tres colores: rojo, negro y blanco.",
                    "El logo clásico pasó a una versión de 8 bits, y todo el canal se arma con píxeles, joysticks y pantallas de carga.",
                ],
                "image": ("sega-manual-01.jpg", "Página del manual con el concepto del canal: los 65 años de SEGA y la estética de píxeles"),
            },
            {
                "type": "pieces",
                "title": "Las ocho piezas",
                "intro": "Un canal repite estas piezas todo el día, y cada una cumple una función distinta.",
                "items": [
                    ("ID", "La firma del canal. Arranca como una consola: carga, Start, Player 1 y el logo.", "full-sega-id.mp4", "piece-id.jpg", "0:21"),
                    ("Apertura", "La presentación de Check Point, el programa del canal: conductor, columnistas y secciones.", "full-sega-apertura.mp4", "piece-apertura.jpg", "0:24"),
                    ("Bumper", "El aviso de corte: «Ya volvemos», con el programa que sigue y su horario.", "full-sega-bumper.mp4", "piece-bumper.jpg", "0:08"),
                    ("Zócalo", "El cartel que dice quién habla en una entrevista y resume lo que dice.", "full-sega-zocalo.mp4", "piece-zocalo.jpg", "0:11"),
                    ("Separador", "Una transición corta entre dos bloques del programa.", "full-sega-separador.mp4", "piece-separador.jpg", "0:05"),
                    ("Contenedor", "El marco con la información del episodio que se está viendo.", "full-sega-contenedor.mp4", "piece-contenedor.jpg", "0:06"),
                    ("Contenedor de grilla", "La pausa que muestra lo que viene: programas y horarios.", "full-sega-contenedor2.mp4", "piece-contenedor2.jpg", "0:08"),
                    ("End tag", "El cierre de una promo, con la fecha y la hora del estreno.", "full-sega-endtag.mp4", "piece-endtag.jpg", "0:06"),
                ],
            },
            {
                "type": "gallery",
                "title": "El manual de marca",
                "intro": "Las reglas del canal en doce páginas: el concepto, el logo, los colores, las letras y cómo se ve en pantalla.",
                "items": [
                    ("sega-manual-01.jpg", "Concepto", "Los 65 años de SEGA: volver a los colores del inicio con una estética de píxeles retro."),
                    ("sega-manual-02.jpg", "Logotipo", "El logo clásico, llevado a píxeles en tres versiones."),
                    ("sega-manual-03.jpg", "Recursos gráficos", "Texturas de cartucho y de pantalla vieja, y la paleta: rojo, blanco y negro."),
                    ("sega-manual-04.jpg", "Patrón", "El fondo del canal: joysticks, círculos y píxeles."),
                    ("sega-manual-05.jpg", "Tipografías", "American Captain para los títulos y Avenir para los textos."),
                    ("sega-manual-06.jpg", "Bumper", "«Ya volvemos», con el programa que sigue y su horario."),
                    ("sega-manual-07.jpg", "Estreno", "La gráfica para anunciar el estreno de Knuckles."),
                    ("sega-manual-08.jpg", "Solo en SEGA", "La placa que firma el contenido exclusivo del canal."),
                    ("sega-manual-09.jpg", "Zócalo", "El nombre de quien habla y su frase, en una entrevista."),
                    ("sega-manual-10.jpg", "Pausa", "La grilla de lo que viene: programas y horarios."),
                    ("sega-manual-11.jpg", "Ya comienza", "El aviso de que arranca el programa."),
                    ("sega-manual-12.jpg", "Fechas especiales", "El saludo navideño y la marca aplicada en la web."),
                ],
            },
        ],
    },
    {
        "slug": "united-in-grief",
        "name": "United in Grief",
        "kind": "Videoclip en stop motion",
        "year": "2025",
        "tile": {"image": "cover-united.jpg", "alt": "Portada de United in Grief: una chica de espaldas frente a un espejo y el título escrito a mano en rojo", "hover": "loop-united.mp4"},
        "lead": "Un video para «United in Grief» de Kendrick Lamar, animado cuadro por cuadro con placas de vidrio superpuestas: una imagen manual, imperfecta y en capas.",
        "facts": [("Año", "2025"), ("Qué es", "Video animado para una canción"), ("Técnica", "Stop motion, vidrio por vidrio y collage"), ("Duración", "1:08")],
        "hero": {"type": "video", "src": "full-united.mp4", "poster": "united-1.jpg", "label": "Video completo", "time": "1:08"},
        "cta": "Ver el video",
        "sections": [
            {
                "type": "text-image",
                "title": "Cómo se hizo",
                "text": [
                    "En el vidrio por vidrio se apilan varias placas, cada una con una parte de la imagen: el fondo, los recortes, las letras.",
                    "Se saca una foto, se mueve algo un poquito y se saca otra. Esas fotos, una atrás de la otra, son la animación.",
                ],
                "image": ("united-3.jpg", "Cuadro del video: un collage en blanco y negro sobre fondo rojo"),
            },
            {
                "type": "stills",
                "title": "Cuadro a cuadro",
                "items": [
                    ("united-1.jpg", "Las letras aparecen pintadas delante del auto."),
                    ("united-2.jpg", "Los ojos, con la letra escrita encima."),
                    ("united-4.jpg", "El título final, armado con letras recortadas."),
                ],
            },
        ],
    },
    {
        "slug": "nn",
        "name": "N.N",
        "kind": "Corto animado en 2D",
        "year": "2025",
        "tile": {"video": "loop-nn.mp4", "poster": "poster-nn.jpg"},
        "lead": "Un corto policial con estética de cine negro, donde cada uno de los tres protagonistas tiene su color: rojo, verde o azul.",
        "facts": [("Año", "2025"), ("Qué es", "Corto animado"), ("Técnica", "Animación 2D con rotoscopia"), ("Duración", "0:48")],
        "hero": {"type": "video", "src": "full-nn.mp4", "poster": "nn-still-1.jpg", "label": "Corto completo", "time": "0:48"},
        "cta": "Ver el corto",
        "sections": [
            {
                "type": "text-image",
                "title": "Un color por personaje",
                "text": [
                    "Rojo, Verde y Azul se juntan en un bar lejos de la ciudad, y lo que empieza como una salida termina en una noche de traiciones en el bosque.",
                    "Todo lo demás está en blanco y negro: el color te dice quién está en escena y qué toca, sin que haga falta un diálogo.",
                ],
                "image": ("nn-personajes.jpg", "Página de personajes: Verde, Azul y Rojo pintados con su color"),
            },
            {
                "type": "stills",
                "title": "Cuadros del corto",
                "items": [
                    ("nn-still-1.jpg", "El auto de Rojo, en la niebla."),
                    ("nn-still-2.jpg", "Verde llega en la noche."),
                    ("nn-still-3.jpg", "Azul, camino al bosque."),
                ],
            },
            {
                "type": "gallery",
                "title": "La biblia de animación",
                "intro": "La biblia completa del corto, en el orden en que se entregó: historia, personajes, colores, cámara, mundo, storyboard y fondos. Tocá cualquier página para verla grande.",
                "items": [
                    ("nn-biblia-01.jpg", "Sinopsis", "La historia de la noche, en un párrafo."),
                    ("nn-biblia-02.jpg", "Colores", "Un color por personaje y el mundo en blanco y negro."),
                    ("nn-biblia-03.jpg", "Cámara y animación", "Planos americanos, cámara quieta y rotoscopia."),
                    ("nn-biblia-04.jpg", "Referencias", "El cine negro como punto de partida."),
                    ("nn-biblia-05.jpg", "Azul", "Frío, callado y calculador."),
                    ("nn-biblia-06.jpg", "Verde", "El corazón del grupo."),
                    ("nn-biblia-07.jpg", "Rojo", "Pura emoción e impulso."),
                    ("nn-biblia-08.jpg", "Mundo", "Una ciudad al borde del colapso y sus lugares."),
                    ("nn-biblia-09.jpg", "Interior", "El bar, por dentro."),
                    ("nn-biblia-10.jpg", "El bar", "La rocola y la luz del lugar, en blanco y negro."),
                    ("nn-biblia-11.jpg", "Exterior", "La ruta y el bosque de noche."),
                    ("nn-biblia-12.jpg", "El auto", "El auto de la noche, en neón rojo."),
                    ("nn-biblia-13.jpg", "Personajes", "Los primeros bocetos de los tres."),
                    ("nn-biblia-14.jpg", "Personajes en color", "Los tres, cada uno con su color."),
                    ("nn-biblia-15.jpg", "Storyboard", "Los planos del corto, viñeta por viñeta."),
                    ("nn-biblia-16.jpg", "Storyboard", "Segunda parte."),
                    ("nn-biblia-17.jpg", "Storyboard", "Tercera parte."),
                    ("nn-biblia-18.jpg", "Mapa", "El recorrido de la noche, del bar al bosque."),
                    ("nn-biblia-19.jpg", "Proceso y bocetado", "Los primeros bocetos a color."),
                    ("nn-biblia-20.jpg", "Escenas en color", "Cuadros clave, ya con su paleta."),
                    ("nn-biblia-21.jpg", "Fondos", "Primero en línea, después en blanco y negro."),
                    ("nn-biblia-22.jpg", "Fondos", "Bocetos y versión final de cada lugar."),
                    ("nn-biblia-23.jpg", "Noche en el bosque", "Un cuadro de la escena final, casi a oscuras."),
                    ("nn-biblia-24.jpg", "Póster", "Dos afiches, uno por personaje."),
                ],
            },
        ],
    },
    {
        "slug": "mi-pequeno",
        "name": "Mi pequeño",
        "kind": "Tipografía animada",
        "year": "2025",
        "tile": {"video": "loop-tipo.mp4", "poster": "poster-tipo.jpg"},
        "lead": "Una animación tipográfica para «Mi pequeño» de Ramma: la canción se cuenta solo con letras, en cuatro colores y con cortes al ritmo de la voz.",
        "facts": [("Año", "2025"), ("Qué es", "Animación tipográfica"), ("Duración", "0:10"), ("Programas", "After Effects e Illustrator")],
        "hero": {"type": "video", "src": "full-tipo.mp4", "poster": "tipo-2.jpg", "label": "Animación completa", "time": "0:10"},
        "cta": "Ver el video",
        "sections": [
            {
                "type": "text-image",
                "title": "La portada",
                "text": ["El título en letra gruesa e inclinada, en crema y magenta sobre azul: los mismos colores que después aparecen en la animación."],
                "image": ("cover-tipo.jpg", "Portada: Pequeño en letras crema y Ramma en magenta, sobre azul"),
            },
            {
                "type": "stills",
                "title": "Cuadros clave",
                "items": [
                    ("tipo-1.jpg", "Letra con serif sobre verde agua."),
                    ("tipo-2.jpg", "Dos tipos de letra en la misma frase."),
                    ("tipo-3.jpg", "El cierre, en azul y magenta."),
                ],
            },
        ],
    },
    {
        "slug": "sega-tv-web",
        "name": "SEGA TV web",
        "kind": "Diseño y desarrollo web",
        "year": "2025",
        "tile": {"video": "loop-web.mp4", "poster": "poster-web.jpg"},
        "lead": "La página del canal SEGA TV: estrenos, catálogo, noticias, planes y contacto. Diseñada para computadora, tablet y celular, y programada en HTML y CSS.",
        "facts": [("Año", "2025"), ("Qué es", "Sitio web del canal"), ("Pantallas", "Computadora, tablet y celular"), ("Código", "HTML, CSS y Bootstrap")],
        "hero": {"type": "live", "src": "sega-web/index.html"},
        "cta": "Usar la página",
        "sections": [
            {
                "type": "gallery",
                "title": "Bocetos",
                "intro": "Antes de programar, cada sección se probó en bocetos.",
                "items": [
                    ("web-boceto-1.jpg", "Inicio", "El estreno destacado arriba de todo."),
                    ("web-boceto-2.jpg", "Novedades", "Un carrusel con lo nuevo del canal."),
                    ("web-boceto-3.jpg", "Otra versión del inicio", "Con el menú centrado y la ciudad de fondo."),
                ],
            },
            {
                "type": "text-image",
                "title": "La grilla",
                "text": [
                    "Todo se ordena sobre una grilla de 12 columnas, con columnas de 70 px y separaciones de 30 px.",
                    "Así cada sección queda alineada con las demás, y la página se adapta a pantallas chicas sin desarmarse.",
                ],
                "image": ("web-grilla.jpg", "Diseño del inicio con la grilla de columnas marcada encima"),
            },
            {
                "type": "devices",
                "title": "En cada pantalla",
                "items": [("web-desktop.jpg", "Computadora"), ("web-tablet.jpg", "Tablet"), ("web-phone.jpg", "Celular")],
            },
        ],
    },
]

# La cinta que pasa entre el saludo y los trabajos
DISCIPLINES = ["Motion graphics", "Identidad de marca", "Animación 2D", "Stop motion", "Edición de video", "Miniaturas para YouTube", "Diseño web"]

# El orden en que aparecen en la grilla (y el de «Siguiente proyecto»)
ORDER = ["united-in-grief", "nn", "sega-tv", "sega-tv-web", "osogrosso", "mi-pequeno"]
PROJECTS.sort(key=lambda p: ORDER.index(p["slug"]))

# Piezas gráficas: miniaturas y portadas, agrupadas por para quién se hicieron
GRAPHICS = [
    ("The Axel Axe Show", "Miniaturas para un podcast de entrevistas en YouTube.", None, [
        ("axel-fight.jpg", "Fight to Survive", "Miniatura de The Axel Axe Show: «Fight to Survive», dos personas frente a un telón rojo"),
        ("axel-hollywood.jpg", "Hollywood is Ruthless", "Miniatura de The Axel Axe Show: «Hollywood is Ruthless», entrevista en un set con telón rojo"),
        ("axel-ai.jpg", "The AI Gold Rush", "Miniatura de The Axel Axe Show: «The AI Gold Rush», dos personas frente a un telón rojo"),
    ]),
    ("OsoGrosso", "Miniaturas para los videos largos del canal.", "osogrosso", [
        ("oso-thumb-hombro.jpg", "Tier list de hombro", "Miniatura de OsoGrosso: el oso junto al título «Tier list hombro» y las letras S, A, B y C"),
        ("oso-thumb-calorias.jpg", "¿Cuántas calorías gastás?", "Miniatura de OsoGrosso: el oso con anteojos y la pregunta «¿Cuántas calorías gastás?»"),
    ]),
    ("Portadas", "La tapa de cada proyecto.", None, [
        ("cover-united.jpg", "United in Grief", "Portada de United in Grief con el título escrito a mano en rojo"),
        ("cover-tipo.jpg", "Mi pequeño", "Portada de Mi pequeño: letras crema y magenta sobre azul"),
        ("cover-sega.jpg", "SEGA TV", "Portada del manual de SEGA TV: el logo pixelado sobre un fondo de joysticks"),
    ]),
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}


def e(text):
    return escape(text, quote=True)


def page(title, description, body, root, home, og_image):
    sec = (lambda i: f"#{i}") if home else (lambda i: f"{root}index.html#{i}")
    mark = "#top" if home else f"{root}index.html"
    links = "".join(f'<a href="{sec(i)}">{t}</a>' for i, t in [("trabajos", "Trabajos"), ("miniaturas", "Miniaturas"), ("sobre-mi", "Sobre mí"), ("contacto", "Contacto")])
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{root}media/{og_image}">
<meta name="theme-color" content="#f1f1ee">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}styles.css">
</head>
<body id="top">

<header class="bar">
  <a class="bar__mark" href="{mark}">Enzo Gimenez</a>
  <nav class="bar__links" aria-label="Secciones">{links}</nav>
  <details class="bar__menu">
    <summary>Menú</summary>
    <nav class="bar__sheet" aria-label="Secciones">{links}</nav>
  </details>
</header>

<main>
{body}
</main>

<footer class="foot">
  <p>Enzo Gimenez · Diseño multimedial · Moreno, Buenos Aires, 2026</p>
  <p class="foot__links"><a href="mailto:{MAIL}">Mail</a><a href="{root}media/Enzo-Gimenez-CV.pdf" download>CV</a><a href="{BEHANCE}" target="_blank" rel="noopener">Behance</a><a href="#top">Volver arriba</a></p>
  <p class="foot__note">SEGA TV y United in Grief no tienen relación oficial con SEGA ni con Kendrick Lamar.</p>
</footer>

<script src="{root}main.js"></script>
</body>
</html>
"""


def tile_media(p, root, hover=True):
    """El video en loop del proyecto, o su tapa (que muestra el video al pasar el mouse)."""
    t = p["tile"]
    if "video" in t:
        return f'<video src="{root}media/{t["video"]}" poster="{root}media/{t["poster"]}" autoplay muted loop playsinline preload="metadata" aria-hidden="true"></video>'
    img = f'<img src="{root}media/{t["image"]}" alt="{e(t["alt"])}" loading="lazy">'
    if hover and t.get("hover"):
        img += f'<video class="tile__hover" src="{root}media/{t["hover"]}" muted loop playsinline preload="none" aria-hidden="true"></video>'
    return img


def build_home():
    widths = ["w5", "w7", "w7", "w5", "w6", "w6"]
    tiles = "\n".join(
        f"""      <li class="tile tile--{w}">
        <a class="tile__link" href="proyectos/{p["slug"]}.html">
          <span class="tile__media">{tile_media(p, "")}</span>
          <span class="tile__cap"><span class="tile__name">{e(p["name"])} <span class="tile__arrow" aria-hidden="true">→</span></span><span class="tile__kind">{e(p["kind"])} · {p["year"]}</span></span>
        </a>
      </li>"""
        for p, w in zip(PROJECTS, widths)
    )
    groups = []
    for title, note, slug, items in GRAPHICS:
        figs = []
        for src, name, alt in items:
            img = f'<img src="media/{src}" alt="{e(alt)}" loading="lazy">'
            figs.append(f'<li class="gfx__item"><button class="gfx__media zoom" type="button" data-caption="{e(title)} · {e(name)}" aria-label="Ampliar: {e(name)}">{img}</button><p class="gfx__name">{e(name)}</p></li>')
        groups.append(f"""    <div class="gfx">
      <div class="gfx__head"><h3 class="gfx__title">{e(title)}</h3><p class="gfx__note">{e(note)}</p></div>
      <ul class="gfx__list gfx__list--{len(items)}">{"".join(figs)}</ul>
    </div>""")
    ribbon = "".join(f"<li>{e(d)}</li>" for d in DISCIPLINES)
    body = f"""  <section class="hero" aria-labelledby="hero-title">
    <h1 class="hero__title" id="hero-title">Hola, soy Enzo.</h1>
    <p class="hero__statement">Diseñador multimedial y técnico en Animación Digital. Hago motion graphics, identidad de marca y piezas para redes, de la idea al archivo final.</p>
    <div class="hero__foot">
      <p class="hero__status"><span class="dot" aria-hidden="true"></span>Disponibilidad completa</p>
      <p class="hero__actions"><a class="btn" href="#trabajos">Ver trabajos</a><a class="link" href="#contacto">Escribime</a></p>
    </div>
  </section>

  <div class="ribbon" role="region" aria-label="Disciplinas">
    <div class="ribbon__track">
      <ul class="ribbon__group">{ribbon}</ul>
      <ul class="ribbon__group" aria-hidden="true">{ribbon}</ul>
    </div>
  </div>

  <section class="work" id="trabajos" aria-labelledby="work-title">
    <div class="head">
      <h2 class="h2" id="work-title">Trabajos</h2>
      <p class="head__note">Una selección de proyectos de animación, identidad de marca y web. Tocá cualquiera para ver el video completo y cómo lo hice.</p>
    </div>
    <ul class="grid">
{tiles}
    </ul>
  </section>

  <section class="graphics" id="miniaturas" aria-labelledby="graphics-title">
    <div class="head">
      <h2 class="h2" id="graphics-title">Miniaturas y portadas</h2>
      <p class="head__note">Piezas gráficas para YouTube y para presentar cada proyecto.</p>
    </div>
{chr(10).join(groups)}
  </section>

  <section class="about" id="sobre-mi" aria-labelledby="about-title">
    <div class="about__side">
      <h2 class="h2" id="about-title">Sobre mí</h2>
      <img class="about__photo media" src="media/enzo.jpg" alt="Enzo Gimenez de frente, con campera azul, sobre una pared blanca" width="640" height="800" loading="lazy">
    </div>
    <div class="about__text">
      <p class="about__lead">Soy Enzo Gimenez, tengo 21 años y soy diseñador multimedial y técnico en Animación Digital. Hago piezas para redes, motion graphics e identidad de marca, de la idea al archivo final.</p>
      <p>Desde 2024 trabajo como diseñador freelance: armo identidades de marca completas y diseño miniaturas para YouTube. En la facultad hice animación digital, stop motion, maquetado web e interfaces interactivas.</p>
    </div>
    <dl class="about__list">
      <div><dt>Experiencia</dt><dd>Diseñador freelance, desde 2024</dd></div>
      <div><dt>Estudios</dt><dd>Diseño Multimedial (4.º año) y Técnico Universitario en Animación Digital, Universidad Nacional de Moreno</dd></div>
      <div><dt>Especialidades</dt><dd>Motion graphics, identidad de marca y edición de video</dd></div>
      <div><dt>Herramientas</dt><dd>After Effects, Photoshop, Illustrator, Premiere, HTML y CSS</dd></div>
      <div><dt>Idiomas</dt><dd>Español e inglés (A2)</dd></div>
      <div><dt>Base</dt><dd>Moreno, Buenos Aires</dd></div>
    </dl>
    <p class="about__cv"><a class="btn" href="media/Enzo-Gimenez-CV.pdf" download>Descargar CV (PDF)</a></p>
  </section>

  <section class="contact" id="contacto" aria-labelledby="contact-title">
    <h2 class="contact__title" id="contact-title">¿Hacemos algo juntos?</h2>
    <p class="contact__lead">Contame tu idea y te respondo.</p>
    <p class="contact__mail"><a href="mailto:{MAIL}">{MAIL}</a></p>
    <p class="contact__actions"><a class="btn btn--light" href="mailto:{MAIL}?subject=Hola%20Enzo">Mandame un mail</a><button class="btn btn--ghost" type="button" data-copy="{MAIL}" aria-live="polite">Copiar mail</button><a class="link" href="media/Enzo-Gimenez-CV.pdf" download>Descargar CV</a><a class="link" href="{BEHANCE}" target="_blank" rel="noopener">Behance</a><a class="link" href="{YOUTUBE}" target="_blank" rel="noopener">YouTube de OsoGrosso</a></p>
  </section>"""
    html = page(
        "Enzo Gimenez — Diseño multimedial",
        "Enzo Gimenez, diseñador multimedial y técnico en Animación Digital: motion graphics, identidad de marca, animación y web. Moreno, Buenos Aires.",
        body, "", True, "poster-oso.jpg",
    )
    (ROOT / "index.html").write_text(html, encoding="utf-8")


def hero_html(p, root):
    h = p["hero"]
    if h["type"] == "video":
        return f"""  <section class="case__hero" id="ver" aria-labelledby="ver-title">
    <h2 class="visually-hidden" id="ver-title">{e(h["label"])}</h2>
    <video class="media" src="{root}media/{h["src"]}" poster="{root}media/{h["poster"]}" controls playsinline preload="metadata" aria-label="{e(h["label"])} de {e(p["name"])}"></video>
    <p class="caption">{e(h["label"])} · {h["time"]} · con sonido</p>
  </section>"""
    if h["type"] == "live":
        return f"""  <section class="case__hero" id="ver" aria-labelledby="ver-title">
    <h2 class="visually-hidden" id="ver-title">La página funcionando</h2>
    <iframe class="media case__site" src="{root}{h["src"]}" title="La página de SEGA TV, funcionando"></iframe>
    <p class="caption">Es la página real: podés bajar, tocar los botones y recorrerla. <a href="{root}{h["src"]}" target="_blank" rel="noopener">Abrirla en otra pestaña</a></p>
  </section>"""
    if h["type"] == "shorts":
        items = "".join(
            f'<li class="short"><video class="media" src="{root}media/{v}" poster="{root}media/{poster}" controls playsinline preload="none" aria-label="Short: {e(t)}"></video><p class="short__name">{e(t)}</p></li>'
            for t, v, poster in h["items"]
        )
        return f"""  <section class="case__hero" id="ver" aria-labelledby="ver-title">
    <div class="sec__head"><h2 class="h3" id="ver-title">{e(h["title"])}</h2><p class="sec__intro">{e(h["intro"])}</p></div>
    <ul class="shorts">{items}</ul>
  </section>"""
    raise ValueError(h["type"])


def zoom(src, alt, caption, root):
    """Una imagen que se amplía con un clic (el visor está en main.js)."""
    return (f'<button class="zoom" type="button" data-caption="{e(caption)}" aria-label="Ampliar: {e(caption)}">'
            f'<img class="media" src="{root}media/{src}" alt="{e(alt)}" loading="lazy"></button>')


def section_html(s, root):
    t = s["type"]
    title = f'<h2 class="h3">{e(s["title"])}</h2>'
    intro = f'<p class="sec__intro">{e(s["intro"])}</p>' if s.get("intro") else ""
    head = f'<div class="sec__head">{title}{intro}</div>'
    if t == "text-image":
        src, alt = s["image"]
        paras = "".join(f"<p>{e(x)}</p>" for x in s["text"])
        return f"""  <section class="sec sec--split">
    <div class="sec__copy">{title}{paras}</div>
    {zoom(src, alt, alt, root)}
  </section>"""
    if t == "pieces":
        items = "\n".join(
            f"""      <li class="piece"><video class="media" src="{root}media/{v}" poster="{root}media/{poster}" controls playsinline preload="none" aria-label="{e(name)}"></video>
        <p class="piece__name">{e(name)} <span>{time}</span></p><p class="piece__text">{e(text)}</p></li>"""
            for name, text, v, poster, time in s["items"]
        )
        return f"""  <section class="sec">
    {head}
    <ol class="pieces">
{items}
    </ol>
  </section>"""
    if t == "gallery":
        items = "\n".join(
            f"""      <li class="gal__item">{zoom(src, f"{name}: {text}", name, root)}<p class="gal__name">{e(name)}</p><p class="gal__text">{e(text)}</p></li>"""
            for src, name, text in s["items"]
        )
        return f"""  <section class="sec">
    {head}
    <ol class="gal">
{items}
    </ol>
  </section>"""
    if t == "stills":
        items = "".join(f"<figure>{zoom(src, text, text, root)}<figcaption>{e(text)}</figcaption></figure>" for src, text in s["items"])
        return f"""  <section class="sec">
    {head}
    <div class="stills">{items}</div>
  </section>"""
    if t == "devices":
        items = "".join(
            f'<figure class="device device--{i}">{zoom(src, f"La página de SEGA TV en {label.lower()}", label, root)}<figcaption>{e(label)}</figcaption></figure>'
            for i, (src, label) in enumerate(s["items"])
        )
        return f"""  <section class="sec">
    {head}
    <div class="devices">{items}</div>
  </section>"""
    if t == "thumbs":
        items = "".join(
            f'<figure>{zoom(src, f"Miniatura de YouTube: {name}", name, root)}<figcaption><span class="thumb__name">{e(name)}</span> <span class="thumb__meta">{e(meta)}</span></figcaption></figure>'
            for src, name, meta in s["items"]
        )
        return f"""  <section class="sec">
    {head}
    <div class="thumbs">{items}</div>
  </section>"""
    if t == "wide":
        src, alt = s["image"]
        return f"""  <section class="sec">
    {head}
    <figure class="wide">{zoom(src, alt, s["caption"], root)}<figcaption>{e(s["caption"])}</figcaption></figure>
  </section>"""
    raise ValueError(t)


def build_project(i):
    p = PROJECTS[i]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    root = "../"
    facts = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["facts"])
    sections = "\n\n".join(section_html(s, root) for s in p["sections"])
    cta = f'<p><a class="btn" href="#ver">{e(p["cta"])}</a></p>' if p.get("cta") else ""
    link = ""
    if p.get("link"):
        href, label = p["link"]
        link = f'\n\n  <p class="case__out"><a class="btn" href="{href}" target="_blank" rel="noopener">{e(label)}</a></p>'
    body = f"""  <section class="case__head" aria-labelledby="p-title">
    <h1 class="case__title" id="p-title">{e(p["name"])}</h1>
    <p class="case__lead">{e(p["lead"])}</p>
    <dl class="facts">{facts}</dl>
    {cta}
  </section>

{hero_html(p, root)}

{sections}{link}

  <section class="next" aria-labelledby="next-title">
    <h2 class="next__title" id="next-title"><a href="{nxt["slug"]}.html">Siguiente: {e(nxt["name"])}</a></h2>
    <a class="next__media" href="{nxt["slug"]}.html" tabindex="-1" aria-hidden="true">{tile_media(nxt, root, hover=False)}</a>
    <p class="next__back"><a class="link" href="{root}index.html#trabajos">Volver a todos los trabajos</a></p>
  </section>"""
    og = p["tile"].get("poster") or p["tile"].get("image")
    html = page(f"{p['name']} — Enzo Gimenez", p["lead"], body, root, False, og)
    (ROOT / "proyectos").mkdir(exist_ok=True)
    (ROOT / "proyectos" / f"{p['slug']}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build_home()
    for i in range(len(PROJECTS)):
        build_project(i)
    print("listo:", 1 + len(PROJECTS), "páginas")
