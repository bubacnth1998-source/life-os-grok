# LIFE OS — Grok Edition

**Implementación independiente de Grok (xAI).**  
No comparte código ni repositorio con las versiones de ChatGPT o Claude.

Un usuario · Un ecosistema · Todo conectado.

## Stack (gratis, Chromebook + iPhone)

- Backend: FastAPI + SQLAlchemy + SQLite
- Frontend: HTML/JS/Tailwind (PWA instalable en iPhone)
- Auth: JWT + PBKDF2
- AI: reglas offline (LLM opcional sin dependencia)
- Sin Docker obligatorio · Sin servicios de pago

## Arranque (Chromebook Linux)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="${PWD}/backend"
python3 scripts/seed.py
./scripts/start.sh
```

Abre http://127.0.0.1:8000 — demo: `demo@lifeos.local` / `demo12345`

## Módulos

Auth · Dashboard · Finance · Projects · Personal · Business · Knowledge · Learning · Automation · Media · AI · System (export/privacy)

## Tests

```bash
export PYTHONPATH="${PWD}/backend"
pytest tests/ -v
```

## Docs

- [INSTALL](docs/INSTALL.md)
- [ARCHITECTURE](docs/ARCHITECTURE.md)
- [SECURITY_AUDIT](docs/SECURITY_AUDIT.md)
- [CHROMEBOOK](docs/CHROMEBOOK.md)
- [IPHONE](docs/IPHONE.md)

## Autor

Grok (xAI) — repositorio exclusivo `life-os-grok`
