# KeltCon Expo — Descarga web

## Origen
- **URL origen:** https://keltcon.info/
- **Fecha de descarga:** 2026-06-29
- **Carpeta destino:** `docs/CLAUDE/Projects/KELTCON/descarga web/`

## Tecnologías detectadas
- **CMS:** WordPress
- **Theme / Page builder:** Divi 5.0.0-public-beta.9 — Elegant Themes
- **Plugin de formulario:** Hostinger Reach (`hostinger-reach`) — formulario de suscripción/contacto
- **Librerías JS:** jQuery 3.7.1 + jquery-migrate, scripts del builder Divi 5
- **Tipografías:** Google Fonts (Open Sans, Inter, Urbanist, AR One Sans, Abhaya Libre) + fuente de iconos de Divi (`modules.woff`)
- **Renderizado:** HTML del lado servidor (no es SPA). No hay React / Next.js / Vue / Angular, por tanto no existe bundle de build tipo SPA que recuperar.

## Estructura de carpetas
```
descarga web/
├── README.md
├── index.source.html              # HTML fuente original (copia fiel, SIN tocar)
├── index.rendered.html            # HTML renderizado, con rutas reescritas a local
├── index.rendered.original.html   # Backup del rendered antes de reescribir
├── download_keltcon.sh            # Script original de descarga
├── rewrite_paths.sh               # Script original de reescritura
└── assets/
    ├── css/      (5 archivos)
    ├── js/       (13 archivos)
    ├── img/      (12 imágenes)
    └── fonts/
        ├── modules.woff           # fuente de iconos de Divi
        ├── google-fonts-1.css     # Google Fonts (familia completa) — rutas locales
        ├── google-fonts-2.css     # Google Fonts (Open Sans) — rutas locales
        └── woff2/  (56 archivos)  # .woff2 de Google Fonts descargados localmente
```

## Assets descargados (89 archivos en total, todos HTTP 200)

### CSS — `assets/css/` (5)
- `subscription.css` (plugin Hostinger Reach)
- `et-divi-dynamic-tb-134-52.css`
- `et-core-unified-52.min.css`
- `et-core-unified-tb-134-deferred-52.min.css`
- `module-style-static-background-parallax.css` (Divi builder-5)

### JS — `assets/js/` (13)
- `jquery.min.js`, `jquery-migrate.min.js`
- `subscription-view.js` (plugin Hostinger Reach)
- `theme-scripts-library-base.js`, `theme-scripts-library-menu.js`
- `script-library-frontend-global-functions.js`, `script-library-ext-waypoint.js`,
  `script-library-link.js`, `script-library.js`, `module-script-background-parallax.js`,
  `script-library-frontend-scripts.js`, `script-library-multi-view.js` (Divi builder-5)
- `common.js` (Divi core admin)

### Imágenes — `assets/img/` (12)
`Diseno-sin-titulo.png`, `Imagen20.jpg`, `Imagen21.jpg`, `Imagen13.jpg`,
`KeltCon-Expo-2026-Logo-e1771754172437.png`, `KeltCon-Logo-General-e1771180329372.png`,
`hero-image.jpeg`, `non-profit-illustration-02-1-scaled.png`,
`Logo_FundacioPortAventura-e1772464838436.png`, `Ocine_Logo.svg_.png`,
`logoBetania-e1772464880749.png`, `sant_joan_de_deu_1669114427-e1772464919390.png`

> **Nota imágenes:** el servidor sirve estas imágenes como **WebP** aunque la extensión
> diga `.png` / `.jpg` / `.jpeg`. Se guardan con el nombre original tal cual (la
> extensión puede no coincidir con el formato real, pero el navegador las muestra igual).
> Las variantes responsive del `srcset` (p.ej. `-480x270`) se han remapeado en el HTML
> a la imagen original a tamaño completo, ya que solo se descargó esa versión.

### Fuentes — `assets/fonts/` (1 icono + 2 CSS + 56 woff2)
- `modules.woff` — fuente de iconos de Divi.
- **Google Fonts localizadas:** las 2 hojas `css?family=...` de `fonts.googleapis.com`
  se descargaron como `google-fonts-1.css` y `google-fonts-2.css`, se descargaron sus
  56 `.woff2` únicos de `fonts.gstatic.com` a `assets/fonts/woff2/`, y las rutas dentro
  de ambos CSS se reescribieron para apuntar a los `.woff2` locales. **Ya no dependen de
  Google.** (El número real de woff2 es 56, no 6: Google genera un @font-face por cada
  peso × subconjunto latin / latin-ext / vietnamese.)

## Reescritura de rutas
- `index.rendered.html`: todas las URLs absolutas `https://keltcon.info/...` y de Google
  Fonts de los assets descargados se reemplazaron por rutas locales `assets/...`,
  quitando los sufijos `?ver=...`. Los bloques `<style>`/`<script>` inline se conservan
  dentro del HTML; no contienen URLs a assets locales que reescribir.
- `index.source.html`: **NO se ha tocado** — copia fiel del HTML original.
- Las URLs `chrome-extension://...` **no se han tocado** (pertenecen a extensiones del
  navegador del usuario, no a la web).

## Dependencias externas restantes
- **Endpoint POST del formulario (Hostinger Reach):**
  `https://keltcon.info/wp-json/hostinger-reach/v1/contact` (y `admin-ajax.php`).
  Es **backend de WordPress**, NO reconstruible en local. Se deja documentado pero
  **el formulario de suscripción no es funcional** offline.
- **Enlaces de navegación / API de WordPress:** `/blog/`, `/expo/`, `/contacto/`,
  `/wp-json/`, `/xmlrpc.php`, oEmbed, etc. se dejan como URLs absolutas a `keltcon.info`
  (son enlaces de página / metadatos, no assets estáticos).
- **Google Fonts:** ✅ localizadas (ya NO quedan como dependencia externa).

## Recursos NO descargables / no incluidos
- **Favicon:** no hay favicon descargable — `/favicon.ico` devuelve **404**. Las
  referencias `cropped-Sin-titulo-2-2-*.png` del `<head>` quedan apuntando a
  `keltcon.info` (404 en local).
- **Assets base del builder Divi** referenciados solo como rutas en config inline
  (`.../Divi/images`, `.../builder-5/images`, `.../vendors`, `preloader.gif`): no se
  cargan para esta página, se dejan como URLs externas (impacto visual nulo/mínimo).

## Notas finales
- Código minificado/empaquetado (Divi builder, jQuery) se conserva **tal cual**.
- **No se ha inventado ni reconstruido ningún backend privado.**
