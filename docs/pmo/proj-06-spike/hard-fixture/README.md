# Acme Sync Server

A lightweight REST API server providing user authentication, session
management, and real-time data sync over WebSocket.

## Run

```
python server.py --port 8080
```

Then POST to `/api/login` with credentials to obtain a session token.

## Status

v0.3 — auth and sync stable, WebSocket layer in progress.
