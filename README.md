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

## Inventory with Elasticsearch and Pytest

> A simple inventory management system using Elasticsearch for indexing and searching, and Pytest for testing the application’s functionality.

## Table of Contents

- [djChat: Full Stack - React Django DRF Channels Project](#djchat-full-stack---react-django-drf-channels-project)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
    - [Backend:](#backend)
    - [Frontend:](#frontend)
    - [Database:](#database)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Backend Setup](#backend-setup)
      - [Frontend Setup](#frontend-setup)
    - [Access the Application](#access-the-application)
  - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [Contributing](#contributing)
  - [License](#license)
  - [Inventory with Elasticsearch and Pytest](#inventory-with-elasticsearch-and-pytest)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features-1)
  - [Technologies Used](#technologies-used)
  - [Requirements](#requirements)
  - [Installation](#installation-1)

---

## About

This project is a simple inventory management system that uses **Elasticsearch** to index and search inventory items. It allows users to perform CRUD (Create, Read, Update, Delete) operations on inventory items and integrates Elasticsearch for efficient searching. The project also includes tests written using **Pytest** to verify the correctness of the implementation.

---

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on inventory items.
- **Elasticsearch Integration**: Leverage Elasticsearch to store and search inventory data efficiently.
- **Pytest for Testing**: Ensure the reliability of the application through unit and integration tests.

---

## Technologies Used

- **Python 3.7+**: The backend of the application is built using Python 3.7 or higher.
- **Elasticsearch**: Used as the primary search engine to store and search inventory items.
- **Pytest**: Testing framework used for writing unit and integration tests.
- **FastAPI** (optional): If applicable, FastAPI is used to build the REST API endpoints for the inventory management system.

---

## Requirements

To run this project, you need the following tools and libraries:

- **Python 3.7+**: Python 3.7 or higher is required.
- **Elasticsearch**: You should have an Elasticsearch instance running. You can download and set it up from [here](https://www.elastic.co/downloads/elasticsearch).
- **pip**: Python package manager to install the dependencies.

---

## Installation

Follow these steps to get the project up and running on your local machine.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SahilMehdiyev/Inventory-with-Elasticsearch-and-Pytest.git
   cd Inventory-with-Elasticsearch-and-Pytest
   ```

2. **Install Poetry**:
   ```bash
   pip install poetry
   ```

3. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

4. **Run Elasticsearch**:
   Ensure you have Elasticsearch running locally or remotely.

5. **Run the application**:
   ```bash
   poetry run python app.py
   ```

6. **Run tests**:
   ```bash
   poetry run pytest
   ```

