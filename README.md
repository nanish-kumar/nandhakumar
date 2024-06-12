# Address Book API

This is an address book API built with FastAPI and SQLite.

## Setup

1. Clone the repository:
   ```sh
   git clone <repository-link>
   cd address_book
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /addresses/`: Create a new address.
- `PUT /addresses/{address_id}`: Update an existing address.
- `DELETE /addresses/{address_id}`: Delete an address.
- `GET /addresses/`: Retrieve addresses within a given distance from specified coordinates.
