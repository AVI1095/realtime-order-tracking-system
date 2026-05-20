# Real-Time Order Tracking System

## Overview
This project implements a real-time order tracking system using an event-driven architecture.  
Clients automatically receive updates whenever the database changes — without relying on polling.

## Problem Statement
Design a system where database updates are propagated to connected clients in real-time efficiently, without frequent polling.

## Tech Stack
- PostgreSQL (Triggers, LISTEN/NOTIFY)
- FastAPI (Backend)
- WebSockets (Real-time communication)
- HTML/CSS/JavaScript (Frontend)

## Architecture
```
PostgreSQL (Trigger)
        ↓
NOTIFY Event
        ↓
FastAPI Listener (asyncpg)
        ↓
WebSocket Server
        ↓
Connected Clients (Real-Time Updates)
```
## Features
- Real-time updates (no polling)
- Event-driven architecture
- WebSocket-based live dashboard
- User-specific filtering (only relevant updates shown)
- Order status tracking
- Order history logging (timeline support)
- Automatic reconnection handling

## How It Works

1. A change occurs in the database (INSERT/UPDATE)
2. PostgreSQL trigger fires automatically
3. NOTIFY event is generated
4. FastAPI listens using LISTEN
5. Backend pushes update via WebSocket
6. Client UI updates instantly

## How to Run

### 1. Clone Repository
git clone https://github.com/AVI1095/realtime-order-tracking-system.git

### 2. Install Dependencies
pip install fastapi uvicorn asyncpg

### 3. Configure Database
- Create a PostgreSQL database
- Add required tables and triggers

### 4. Run Backend
uvicorn main:app --reload

### 5. Run Frontend
Open client.html in your browser

## Example Query
UPDATE orders SET status = 'Shipped' WHERE id = 1;
This update will instantly reflect in the UI without refreshing.

## Key Concepts Used
- Event-driven architecture
- Push-based communication (WebSockets)
- Database triggers for real-time systems
- Efficient data propagation without polling

## Why This Project Matters
Traditional systems rely on polling, which increases load and latency.  
This project demonstrates how to build a scalable real-time system using database-driven events, reducing unnecessary queries and improving performance.

## Conclusion
This project demonstrates how to build a scalable and efficient real-time system using database-level events and WebSockets, eliminating the need for polling and reducing system load.

## Author
Aditya Ingle
