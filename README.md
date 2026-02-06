# Holydays API

A FastAPI-based REST API for retrieving public holiday information for 119 countries on the planet based on the current year. The purpose of this API is to serve as a data bridge for the frontend of the app.

## Features

- Retrieve public holiday data for all 119 countries
- Built with modern Python async patterns
- Select individual public holidays to view more details.
- Representative images for every holiday description.

## Technologies & Libraries Used.

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

- Interactive docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

## Endpoints

- `GET /countries/:country_name/holidays/:holiday_name` - Retrieve all public holidays occurring in the selected country for the current year.

- `GET /image/countries/:country_name/holidays/:holiday_name` - Search for and return representational image data for the selected public holiday and country. The data will be in JSON format.

## License

MIT
