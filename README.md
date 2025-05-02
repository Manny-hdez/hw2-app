ECS162 HW2

# HW2 App

https://github.com/Manny-hdez/hw2-app

## Running the Application

1. Ensure Docker Desktop is running.
2. Run `docker compose up --build` in the project root directory.
3. Access the application at [http://localhost:80](http://localhost:80) (or the mapped port).

## Running Tests

### Backend Tests (pytest)

1. Navigate to the `backend` directory: `cd backend`
2. Install dependencies (ideally in a virtual environment):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run tests from the `backend` directory:
   ```bash
   pytest
   ```
   (Or run from project root: `pytest backend/tests`)

### Frontend Tests (Vitest)

1. Navigate to the `frontend` directory: `cd frontend`
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run tests:
   ```bash
   npm test
   ```

## Notes

- Backend API runs on port 8000 inside the container.
- Frontend is served by the backend (Flask) after being built.
- Ensure you have an `NYT_API_KEY` environment variable set (e.g., in a `.env` file in the project root or `backend` directory) for the backend to function correctly when run locally or for tests that don't mock the API key usage.
