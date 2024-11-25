
# Movie Search API

This project is a **Flask-based API** for searching movies using the **TMDb API**. It supports searching for movies by title and returns detailed information such as release date, overview, ratings, genres, and poster/backdrop images. The API includes support for **CORS** to integrate seamlessly with front-end applications.

---

## Features

- Search for movies by title using a query parameter.
- Fetch details such as:
  - Title
  - Release date
  - Overview
  - Rating
  - Genres
  - Poster and backdrop images.
- Configurable API language (default: English).
- Error handling for invalid or empty search queries.

---

## Requirements

- Python 3.8+
- TMDb API key (you can sign up for one [here](https://www.themoviedb.org/documentation/api)).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/israwss/cinema_back.git
   cd cinema_back
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your TMDb API key:
   - Replace `'api_key'` in the `tmdb.api_key` line with your own TMDb API key.

---

## Usage

1. Run the API:
   ```bash
   python app.py
   ```

2. Access the API endpoint:

   - **Search Movies**:  
     URL: `http://127.0.0.1:5000/search_movie`  
     Method: `GET`  
     Query Parameters:  
     - `query` (required): The movie title to search for.

     Example:
     ```bash
     curl "http://127.0.0.1:5000/search_movie?query=inception"
     ```

3. Response example:
   ```json
   [
       {
           "title": "Inception",
           "release_date": "2010-07-15",
           "overview": "Cobb, a skilled thief who commits corporate espionage...",
           "rating": 8.3,
           "vote_average": 8.3,
           "backdrop_url": "https://image.tmdb.org/t/p/w500/some-backdrop.jpg",
           "poster_url": "https://image.tmdb.org/t/p/w500/some-poster.jpg",
           "genres": ["Action", "Science Fiction"]
       }
   ]
   ```

---

## Configuration

- **Language**: Modify `tmdb.language` to set the desired language for API responses (e.g., `'en'`, `'es'`).
- **CORS**: The `Flask-CORS` library is enabled by default for cross-origin requests.

---

## Dependencies

- **Flask**: Web framework.
- **Flask-CORS**: CORS support for front-end integration.
- **tmdbv3api**: Python wrapper for the TMDb API.

Install all dependencies via:
```bash
pip install Flask Flask-CORS tmdbv3api
```

---

## Error Handling

- **400 Error**: Missing or invalid query parameter.
  ```json
  {"error": "Se necesita un parámetro de búsqueda"}
  ```

- **500 Error**: Internal server error (e.g., TMDb API issues).
  ```json
  {"error": "Error message"}
  ```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for details.
