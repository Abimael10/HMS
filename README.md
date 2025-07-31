# Hospital Management System (HMS)

A hospital management system built with FastAPI, SQLAlchemy, and PostgreSQL. The idea behind this repo is to find a common ground for scalable architecture (at least with Python and this specific library) and not just build the system itself since (me personally) do not have a market to make business in this domain.

So far the only working component is the patients CRUD, with some other either started but unfinished and not a working system to claim it an MVP. NOTE: This is far from being an MVP since I just put it up here as a reference for future implementations.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd HMS
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```
API_URL=API URL LOCAL OR PROD
POSTGRES_URI=postgresql://username:password@localhost:5432/hospital_db
```

Adjust the PostgreSQL connection string according to your database setup.

## Running the Application

To start the application, run:

```bash
python -m hospital.entrypoints.main
```

The API will be available at http://localhost:8001.

## Running Tests

To run the tests:

```bash
pytest
```

## Project Structure

- `hospital/adapters`: Database and external systems adapters
- `hospital/domain`: Domain models, entities, and value objects
- `hospital/entrypoints`: API endpoints and interfaces
- `hospital/service_layer`: Application business logic
- `hospital/tests`: Test suite 
