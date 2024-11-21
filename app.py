from flask import Flask, jsonify, request
from flask_cors import CORS
from tmdbv3api import TMDb, Movie

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitudes desde el frontend

# Configura tu clave de API de TMDB
tmdb = TMDb()
tmdb.api_key = '77682c0ab6a19877ca4446c021d638f0'
tmdb.language = 'en'  # Configura el idioma

movie = Movie()

@app.route('/search_movie', methods=['GET'])
def search_movie():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Se necesita un parámetro de búsqueda"}), 400

    try:
        # Usa tmdbv3api para buscar la película
        search_results = movie.search(query)
        results = []

        for m in search_results:
            # Obtener los géneros por nombre
            genres = [g['name'] for g in m.genres] if hasattr(m, 'genres') and m.genres else []

            # Crear el diccionario de resultados
            result = {
                "title": m.title,
                "release_date": m.release_date,
                "overview": m.overview,
                "rating": m.vote_average,
                "vote_average": m.vote_average,
                "backdrop_url": f"https://image.tmdb.org/t/p/w500{m.backdrop_path}" if m.backdrop_path else None,
                "poster_url": f"https://image.tmdb.org/t/p/w500{m.poster_path}" if m.poster_path else None,
                "genres": genres
            }
            results.append(result)

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
