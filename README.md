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
PostgreSQL (Trigger)
        ↓
NOTIFY Event
        ↓
FastAPI Listener (asyncpg)
        ↓
WebSocket Server
        ↓
Connected Clients (Real-Time Updates)

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

### 1. Install dependencies
pip install fastapi uvicorn asyncpg

### 2. Start backend server
uvicorn main:app --reload

### 3. Open frontend
Open client.html in your browser

## Example
UPDATE orders SET status = 'Shipped' WHERE id = 1;
This update will instantly reflect in the UI without refreshing.

## Key Concepts Used
- Event-driven architecture
- Push-based communication (WebSockets)
- Database triggers for real-time systems
- Efficient data propagation without polling

## Conclusion
This project demonstrates how to build a scalable and efficient real-time system using database-level events and WebSockets, eliminating the need for polling and reducing system load.

## Author
Aditya Ingle
