<h1 align="center">
AnimeHoshi LiveChat API
</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-%23339933.svg?style=for-the-badge&logo=python&logoColor=%23ffffff"/></a>
  <a href="#"><img src="https://img.shields.io/badge/fastapi-%2300C6A0.svg?style=for-the-badge&logo=fastapi&logoColor=white"/></a>
  <a href="#"><img src="https://img.shields.io/badge/redis-%23DC382D.svg?style=for-the-badge&logo=redis&logoColor=white"/></a>
</p>

<p align="center">
  <a href="#">
    <img src="https://thullydev.github.io/thullyDevStatics/images/animehoshi-logo.png" alt="Logo" width="200"/>
  </a>
</p>

## What is AnimeHoshi LiveChat API?

**AnimeHoshi LiveChat API** is a component of the AnimeHoshi project, designed to manage real-time chat functionality. This API allows users to create chat rooms, send, edit, and delete messages, and view active rooms, all managed through FastAPI with Redis for caching.

## Features

- **Create Room**: Generate a new chat room with unique identifiers and metadata.
- **Get Room**: Retrieve information about a specific chat room.
- **View Active Rooms**: List all active rooms and their user counts.
- **Send Message**: Post new messages to a chat room with user validation.
- **Edit Message**: Modify existing messages within a chat room.
- **Delete Message**: Remove messages from a chat room.

## API Endpoints and Usage Guide

### 1. Create Room
- **Route**: `/room/create/`
- **Method**: GET
- **Description**: Creates a new chat room with a unique ID and code. The room will be deleted after 24 hours.

### 2. Get Room
- **Route**: `/room/`
- **Method**: POST
- **Parameters**: 
  - `room_id`: ID of the chat room
  - `room_code`: Code for validating the room
- **Description**: Retrieves details of a specific chat room.

### 3. View Active Rooms
- **Route**: `/rooms_views/`
- **Method**: GET
- **Description**: Lists all active chat rooms and their current number of users.

### 4. Send Message
- **Route**: `/room/message/send`
- **Method**: POST
- **Parameters**: 
  - `room_id`: ID of the chat room
  - `room_code`: Code for validating the room
  - `user_id`: ID of the user sending the message
  - `display_name`: Display name of the user (optional)
  - `token`: User's authentication token
  - `message`: The content of the message
- **Description**: Sends a new message to a chat room.

### 5. Edit Message
- **Route**: `/room/message/edit/`
- **Method**: POST
- **Parameters**: 
  - `room_id`: ID of the chat room
  - `room_code`: Code for validating the room
  - `user_id`: ID of the user editing the message
  - `token`: User's authentication token
  - `message_id`: ID of the message to be edited
  - `message`: New content of the message
- **Description**: Edits an existing message in a chat room.

### 6. Delete Message
- **Route**: `/room/message/delete/`
- **Method**: POST
- **Parameters**: 
  - `room_id`: ID of the chat room
  - `room_code`: Code for validating the room
  - `user_id`: ID of the user deleting the message
  - `token`: User's authentication token
  - `message_id`: ID of the message to be deleted
- **Description**: Deletes a message from a chat room.

## Installation and Local Development 💻

### Clone the Repository

```bash
git clone https://github.com/thullyDev/liveChat.git

cd liveChat

touch .env

pip install -r requirements.txt

python -m venv env

uvicorn app.main:app --reload --port 8001
```

###### .env (change accordingly)
```
REDIS_PORT=****
REDIS_HOST=****
REDIS_PASSWORD=****
```
