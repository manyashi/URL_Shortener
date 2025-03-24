**URL SHORTENER API**

1. **Description**

A simple URL shortening service similar to Bit.ly, built using FastAPI and PostgreSQL.

2. **Features**

- Shorten long URLs into short, easy-to-share links.

- Redirect users from short URLs to original long URLs.

- Track the number of times a short URL has been visited.

- FastAPI provides an interactive API documentation.

3. **API Endpoints**

Shorten a URL

Endpoint: POST /shorten

Request Body:

**{
  "long_url": "https://example.com"
}**

Response:

**{
  "short_url": "https://url-shortener-2-uyh8.onrender.com/c984d0",
  "long_url": "https://example.com",
  "visit_count": 0
}**

Redirect to Long URL

Endpoint: GET /{short_code}

Example: GET /c984d0

Redirects the user to the original URL.

4. **API Documentation**

Once the server is running, visit:

FastAPI Documentation : https://url-shortener-2-uyh8.onrender.com/docs#/default/redirect_url__short_code__get

5. **Deployment**

Deploy the API using Render

Deploy to Render

Create a new Web Service on Render.

Set the Build Command: pip install -r requirements.txt

Set the Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Set Environment Variables:

DATABASE_URL → Your PostgreSQL URL from Render.
