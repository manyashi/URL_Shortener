URL Shortener API

Description

A simple URL shortening service similar to Bit.ly, built using FastAPI and PostgreSQL.

Features

Shorten long URLs into short, easy-to-share links.

Redirect users from short URLs to original long URLs.

Track the number of times a short URL has been visited.

FastAPI provides an interactive API documentation.

Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/url-shortener.git
cd url-shortener

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up the Database

Create a PostgreSQL database and update your environment variables:

export DATABASE_URL="postgresql://user:password@localhost/shortener"

On Windows (PowerShell):

$env:DATABASE_URL="postgresql://user:password@localhost/shortener"

5. Run Database Migrations

alembic upgrade head

6. Start the API Server

uvicorn app.main:app --reload

API Endpoints

Shorten a URL

Endpoint: POST /shorten

Request Body:

{
  "long_url": "https://example.com"
}

Response:

{
  "short_url": "https://your-deployment-url.com/abc123",
  "long_url": "https://example.com",
  "visit_count": 0
}

Redirect to Long URL

Endpoint: GET /{short_code}

Example: GET /abc123

Redirects the user to the original URL.

API Documentation

Once the server is running, visit:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

Deployment

Deploy the API using Render, Railway.app, or Fly.io.

Deploy to Render

Create a new Web Service on Render.

Set the Build Command: pip install -r requirements.txt

Set the Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Set Environment Variables:

DATABASE_URL → Your PostgreSQL URL from Render.
