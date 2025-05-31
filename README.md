# Data Processing Web Application

A Flask-based web application that allows users to manage and process personal data with a clean, modern interface. The application stores data in a SQLite database and can export it to Excel format.

## Features

- Modern web interface with Bootstrap 5
- Data entry form with dynamic row addition
- SQLite database for persistent storage
- Excel export functionality
- Database query interface
- RESTful API endpoints
- Flash messages for user feedback

## Tech Stack

- Python 3.9+
- Flask
- SQLAlchemy
- Pandas
- Bootstrap 5
- SQLite

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [repository-name]
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8080
```

3. To query the database using SQL:
```bash
./query_db.sh
```

## Database Operations

The application includes a set of SQL queries for database inspection. To run them:

1. Make the query script executable:
```bash
chmod +x query_db.sh
```

2. Run the queries:
```bash
./query_db.sh
```

Available queries include:
- View all records
- Get age statistics
- View city-wise distribution
- Sort by various fields
- Filter by conditions

## Project Structure

```
├── app.py              # Main Flask application
├── models.py           # Database models
├── hello_world.py      # Data processing logic
├── requirements.txt    # Python dependencies
├── database_queries.sql # SQL queries for database inspection
├── query_db.sh        # Shell script to run SQL queries
└── templates/         # HTML templates
    ├── index.html    # Main page template
    └── cancel.html   # Cancel page template
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 