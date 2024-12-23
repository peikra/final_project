# Football Match Management System

## Description
This is a backend system for managing football teams, match invitations, chat functionalities, and tournaments. The project is built using Django and Django REST Framework (DRF), and it includes functionalities such as:
- User registration and authentication
- Team management
- Match invitations between teams
- Chat system for match-related communication
- Tournament creation and management

The system allows users to register, create teams, send match invitations, communicate through chat, and manage tournaments. The backend is built with APIs that are ready to be integrated with a frontend application, providing a full-stack solution for football match management.

## Features
- **User Authentication**: 
  - Register new users, login, and token refresh.
  - Manage user details (e.g., team membership).
  
- **Team Management**: 
  - Create, update, and manage teams.
  - Each team has an owner who can invite other teams to matches.

- **Match Invitations**: 
  - Send and receive match invitations between teams.
  - Accept or reject invitations.
  
- **Chat**: 
  - Chat functionality for communication between teams once a match invitation is accepted.

- **Tournaments**:
  - Create and manage tournaments.
  - Add and remove teams from tournaments.

## Technologies
- **Django**: Web framework for the backend.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **Celery**: For handling asynchronous tasks (e.g., sending email notifications).
- **Swagger**: For API documentation.
- **Django Debug Toolbar**: For debugging during development.

## Setup

### Requirements
- Python 3.x
- Django 4.x
- Django REST Framework
- Celery
- Redis (for Celery)
- drf-spectacular (for API schema generation)
- django-debug-toolbar (for debugging)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>

2. **Create a virtual environment**:
     python -m venv venv

3. **Install dependencies**:
     pip install -r requirements.txt

## Development Tools

- **Django Debug Toolbar**:  
  If you want to use the debug toolbar during development, make sure the `DEBUG` setting in your `settings.py` file is set to `True`. The toolbar will provide valuable debugging information on each page.

- **Swagger Documentation**:  
  Once the server is running, you can view the Swagger documentation by navigating to `/api/swagger` in your browser.

- **Redoc Documentation**:  
  An alternative API documentation interface is available at `/api/schema/redoc/`.

## API Endpoints

### User App
- **POST `/api/user/register/`**: Register a new user.
- **POST `/api/user/login/`**: Login and get an authentication token.
- **POST `/api/user/token-refresh/`**: Refresh the authentication token.

### Team App
- **GET `/api/team/`**: List all teams.
- **POST `/api/team/`**: Create a new team.
- **PUT `/api/team/{team_id}/`**: Update team details.
- **DELETE `/api/team/{team_id}/`**: Delete a team.

### Match App
- **POST `/api/match/send-invitation/`**: Send a match invitation from one team to another.
- **GET `/api/match/get-invitations/`**: Get received match invitations for the authenticated user.
- **PUT `/api/match/update-status/{invitation_id}/`**: Update the status of a match invitation (accept or reject).

### Chat App
- **GET `/api/match/{invitation_id}/chat/`**: Get the chat messages for a specific match invitation.
- **POST `/api/match/{invitation_id}/chat/send/`**: Send a message in the chat for a specific match invitation.

### Tournament App
- **POST `/api/tournaments/`**: Create a new tournament.
- **GET `/api/tournaments/`**: List all tournaments.
- **POST `/api/tournaments/{tournament_id}/add-team/`**: Add a team to a tournament.
- **POST `/api/tournaments/{tournament_id}/remove-team/`**: Remove a team from a tournament.

## Tasks
- **Send Invitation Email**: When a match invitation is sent, an email notification is sent to the receiving team.
- **Send Status Email**: When the status of a match invitation is updated, an email notification is sent to the sending team.

