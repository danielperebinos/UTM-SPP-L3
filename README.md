# URL Shortener API

This API allows you to shorten long URLs into concise and shareable links. With this URL Shortener API, you can generate
shortened URLs that redirect to the original long URLs.

## Getting Started

To use this URL Shortener API, follow these steps:

### Prerequisites

- Python 3.x installed on your system.
- Django and Django Rest Framework (DRF) installed in your Python environment.

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/url-shortener-api.git
```

2. Navigate to the project directory:

```bash
cd url-shortener-api
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the Django development server:

```bash
python manage.py runserver
```

2. Use the API endpoints to interact with the URL Shortener:

- **Generate Shortened URL**
- Endpoint: `POST http://localhost/shortner/generate`
- Description: Create a shortened URL from a long URL.
- Request Body:
```json
{
"url": "https://example.com/very/long/url/to/shorten"
}
```
- Response:
```json
{
"url": "https://example.com/very/long/url/to/shorten",
"shorted": "http://localhost/shortner/abc123"
}
```

- **Retrieve Original URL**
- Endpoint: `GET http://localhost/shortner/{short_code}`
- Description: Retrieve the original URL associated with a short code.

### API Documentation

For detailed API documentation and interactive testing, refer to the Swagger documentation:

- Swagger UI: [http://localhost/swagger-ui](http://localhost/swagger-ui)

### Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you have any suggestions, improvements, or bug
fixes.

## License

This project is licensed under the [MIT License](LICENSE).