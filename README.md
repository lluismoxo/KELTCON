# KeltCon Expo — Sitio estático (migración desde WordPress/Hostinger)

Copia **estática completa** de https://keltcon.info/ (WordPress + Divi 5), lista para
servir en GitHub Pages sin servidor ni base de datos.

- **Web en vivo:** https://lluismoxo.github.io/KELTCON/
- **Repo:** https://github.com/lluismoxo/KELTCON (público)
- **Origen:** https://keltcon.info/ (WordPress + tema Divi 5.0.0-public-beta.9)
- **Fecha migración:** 2026-06-29

## Qué es esto
El sitio original es WordPress (se genera en el servidor y se edita con el panel Divi).
Aquí está convertido a **HTML estático**: se ve y navega igual, pero NO necesita
servidor. Contrapartida: no hay panel de edición visual; cambiar contenido = editar el
HTML. Backend NO reconstruido (ver "Formularios").

## Páginas incluidas (11)
`/` · `/expo/` · `/club/` · `/contacto/` · `/faq/` · `/sobre-nosotros/` · `/blog/` ·
`/privacy-policy/` · `/inicio/barcelona/` · `/keltconexpo-iii-2026/` (post) ·
`/lanzamiento-de-nuestra-nueva-web/` (post)

Cada página vive en `slug/index.html` para respetar los permalinks de WordPress, de
modo que el menú navega dentro del sitio.

## Estructura
```
/  (raíz del repo = raíz publicada por Pages, servida en /KELTCON/)
├── .nojekyll                 # imprescindible: hace que Pages sirva _gfonts/
├── index.html                # home
├── expo/index.html, club/index.html, ... (resto de páginas)
├── inicio/barcelona/index.html
├── wp-content/               # CSS, JS, imágenes, fuentes (estructura WP original)
├── wp-includes/              # jQuery, etc.
├── _gfonts/                  # Google Fonts localizadas (8 CSS + woff2/ con 84 fuentes)
└── _legacy/                  # primera descarga (1 página aplanada) — archivo histórico
```

## Tecnologías detectadas en el original
- **CMS:** WordPress · **Page builder:** Divi 5.0.0-public-beta.9
- **Plugin formulario:** Hostinger Reach (bloque de suscripción)
- **Form de contacto:** form custom del tema (`keltcon_form_unificado`, PHP del servidor)
- **WooCommerce:** instalado pero SIN tienda activa (no hay productos/carrito/pagos)
- **JS:** jQuery 3.7.1 + scripts de Divi
- **Fuentes:** Google Fonts (Open Sans, Inter, Urbanist, AR One Sans, Abhaya Libre,
  Lato, Arvo, ABeeZee según página) + fuente de iconos de Divi + FontAwesome

## Rutas y Pages
- El sitio se sirve en la subruta `/KELTCON/`. Todas las URLs internas se reescribieron
  de `https://keltcon.info/...` a `/KELTCON/...` (absolutas con prefijo). Funcionan igual
  desde cualquier página sin importar su profundidad.
- `.nojekyll` evita que GitHub Pages (Jekyll) ignore la carpeta `_gfonts/`.

## Formularios (IMPORTANTE — no funcionales aún)
Los formularios necesitan un servidor para enviar el email; en estático no lo hay.
**Backend NO reconstruido** (decisión: dejarlos sin envío por ahora).
- **Form de contacto** (`/contacto/`): neutralizado — muestra aviso y no recarga.
- **Form de suscripción** (footer): su JS intenta el endpoint original y falla en
  silencio.

### Cómo activarlos (futuro, ~10 min, gratis)
1. Crear una *access key* en https://web3forms.com con el email de destino.
2. En el `<form>` del contacto: cambiar `action`/`onsubmit` por el endpoint de Web3Forms
   y añadir un input oculto `access_key`. (Se puede hacer bajo pedido.)

## Verificación
- Las 11 páginas y los 162 assets referenciados verificados **HTTP 200** (servidor local
  y luego en vivo en Pages). 0 enlaces rotos a assets.

## Dependencias externas / no incluido
- **Google Fonts:** ✅ localizadas (ya NO dependen de Google).
- **Endpoint POST de formularios:** backend WordPress, NO reconstruible / no incluido.
- **Favicon:** `/favicon.ico` daba 404 en origen.
- **Panel de edición Divi / base de datos:** no aplican a un sitio estático.

## Nota sobre imágenes
Algunas imágenes se sirven como WebP aunque la extensión sea `.png`/`.jpg`; se conservan
con el nombre original. Las variantes responsive (`-480x270`, etc.) se descargaron o se
remapearon a la versión disponible.
