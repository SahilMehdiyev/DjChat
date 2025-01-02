# djChat: Full Stack - React Django DRF Channels Project

Welcome to **djChat**, a full-stack chat application built using **React**, **Django**, **Django REST Framework (DRF)**, and **Django Channels**. This project showcases a live chat system that is scalable and feature-rich, leveraging the power of real-time communication.

## Features

- **Real-Time Chat**: Powered by Django Channels for WebSocket support.
- **User Authentication**: Secure login and registration system.
- **Server and Channels**: Organize conversations into servers and channels.
- **Message History**: Persistent message storage.
- **Responsive Design**: A seamless user experience on all devices.

## Tech Stack

### Backend:
- **Django**: Backend framework.
- **Django REST Framework**: API creation.
- **Django Channels**: Real-time WebSocket communication.

### Frontend:
- **React**: Frontend framework.
- **Axios**: API requests.
- **CSS/Bootstrap**: Styling and responsiveness.

### Database:
- **SQLite** (default, for development).
- Easily configurable to PostgreSQL or MySQL.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Ensure you have the following installed:

- Python (3.8 or higher)
- Node.js (14 or higher)
- npm or yarn
- Virtual environment tool (optional, recommended)

### Installation

#### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SahilMehdiyev/DjChat
   cd djChat
   ```

2. Install Poetry:
   ```bash
   pip install poetry
   ```

3. Install backend dependencies using Poetry:
   ```bash
   poetry install
   ```

4. Apply database migrations:
   ```bash
   poetry run python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   poetry run python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   poetry run python manage.py runserver
   ```

#### Frontend Setup

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install frontend dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

### Access the Application

- **Frontend**: Navigate to `http://localhost:3000`
- **Backend**: Navigate to `http://localhost:8000`

## Usage

1. Register as a new user or log in with existing credentials.
2. Create servers and channels to organize your chats.
3. Start chatting with other users in real time!

## Screenshots

_Include screenshots of the application here to showcase the interface._

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


