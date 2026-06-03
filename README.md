# 🕷️ Iron Gwazi Web Scraper

Mi primer web scraper en Python, inspirado en el libro **"Web Scraping with Python" de Ryan Mitchell**.

## ¿Qué hace este proyecto?

Extrae información de la página de Wikipedia de la montaña rusa <a href="https://en.wikipedia.org/wiki/Iron_Gwazi" target="_blank">**Iron Gwazi**</a>
- Título de la página
- Primer párrafo de contenido 

## Tecnologías utilizadas

- Python 3.12.6
- BeautifulSoup4
- urllib

## Conceptos aplicados

- Peticiones HTTP con headers personalizados (`User-Agent`)
- Parseo de HTML con BeautifulSoup
- Manejo de estructuras HTML (etiquetas `p` con y sin clase)
- Limpieza de texto con `.strip()`
- Uso de condicionales para prevenir errores

## Cómo ejecutar el proyecto

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/LovecraftianCode/Iron-Gwazi-Web-Scraper.git
cd iron-gwazi-scraper
```

### 2. Instalar dependencias

```bash
pip install beautifulsoup4
```

### 3. Ejecutar el script
```bash
python Iron-Gwazi-Web-Scraper.py
```

## Ejemplo de salida
<img width="1624" height="91" alt="img" src="https://github.com/user-attachments/assets/eeaceec6-1af1-4372-a0c5-53994c3fb65e" />

## Nota sobre scraping ético
Este script:
- Respeta el archivo robots.txt de Wikipedia
- No satura el servidor (solo una petición)
- Utiliza un User-Agent real para identificarse como navegador

## Próximos pasos
- Extraer más datos (fecha de apertura, altura, velocidad)
- Guardar la información en un archivo CSV
- Agregar manejo de errores (timeouts, 404, etc.)
- Rotación de User-Agents para múltiples peticiones

## Inspiración
Basado en el libro "Web Scraping with Python" de Ryan Mitchell (O'Reilly).
