#!/usr/bin/env bash
# Reescribe rutas absolutas de keltcon.info a rutas locales en los HTML
set -e
ROOT="docs/CLAUDE/Projects/KELTCON/descarga web"
for f in "$ROOT/index.source.html" "$ROOT/index.rendered.html"; do
  [ -f "$f" ] || continue
  # CSS/JS/imagenes a carpetas locales (nombres originales, sin querystring)
  sed -E -i.bak \
    -e 's#https?://keltcon\.info/[^"'"'"' ]*/([^/"'"'"' ]+\.(css))(\?[^"'"'"' ]*)?#assets/css/\1#g' \
    -e 's#https?://keltcon\.info/[^"'"'"' ]*/([^/"'"'"' ]+\.(js))(\?[^"'"'"' ]*)?#assets/js/\1#g' \
    -e 's#https?://keltcon\.info/[^"'"'"' ]*/([^/"'"'"' ]+\.(png|jpe?g|gif|webp|svg|ico))(\?[^"'"'"' ]*)?#assets/images/\1#g' \
    -e 's#https?://keltcon\.info/[^"'"'"' ]*/([^/"'"'"' ]+\.(woff2?|ttf|otf))(\?[^"'"'"' ]*)?#assets/fonts/\1#g' \
    "$f"
done
echo "Rutas reescritas (copias .bak creadas)."
