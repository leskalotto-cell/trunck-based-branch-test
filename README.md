# Flask API Applikation

En simpel Flask API til at starte med.

## Installation

1. Installer Python (version 3.7 eller nyere)

2. Opret en virtuel miljø (anbefalet):
```bash
python -m venv venv
```

3. Aktivér den virtuelle miljø:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Installer de nødvendige pakker:
```bash
pip install flask
```

## Brug

1. Start applikationen:
```bash
python app.py
```

2. API'en vil være tilgængelig på `http://localhost:5000`

## API Endpoints

- **GET /**: Velkomstbesked
- **GET /api/hello**: Returnerer en hilsen
- **GET /api/hello/<name>**: Returnerer en personaliseret hilsen
- **POST /api/data**: Modtager JSON data og returnerer den tilbage

## Eksempler

### GET /
```bash
curl http://localhost:5000/
```

### GET /api/hello
```bash
curl http://localhost:5000/api/hello
```

### GET /api/hello/John
```bash
curl http://localhost:5000/api/hello/John
```

### POST /api/data
```bash
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello API"}'
```

## Struktur

```
project/
├── app.py
├── README.md
└── venv/
```

## Noter

- Applikationen kører i debug-mode som standard
- I produktion bør debug være deaktiveret
- Standard host er localhost (127.0.0.1) på port 5000
