# Hospital Management System (HMS)

A hospital management system built with FastAPI, SQLAlchemy, and PostgreSQL.

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
API_URL=http://localhost:8000
POSTGRES_URI=postgresql://username:password@localhost:5432/hospital_db
```

Adjust the PostgreSQL connection string according to your database setup.

## Running the Application

To start the application, run:

```bash
python -m hospital.entrypoints.main
```

The API will be available at http://localhost:8000.

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