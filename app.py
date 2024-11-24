from flask import Flask, jsonify, request
from flask_cors import CORS
from tmdbv3api import TMDb, Movie,Discover

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitudes desde el frontend

# Configura tu clave de API de TMDB
tmdb = TMDb()
tmdb.api_key = '77682c0ab6a19877ca4446c021d638f0'
tmdb.language = 'en'  # Configura el idioma


movie = Movie()
discover = Discover()

@app.route('/search_movie', methods=['GET'])
def search_movie():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({"error": "El parámetro 'query' es obligatorio"}), 400

    try:
        # Buscar películas basadas en la popularidad y calificación
        search_results = discover.discover_movies({
            "sort_by": "popularity.desc",  # Ordenar por popularidad descendente
            "vote_average.gte": 5,        # Filtrar por calificación >= 5
            "with_keywords": query        # Buscar por palabra clave
        })

        results = []

        for m in search_results:
            # Filtrar por campos no nulos
            if m.overview and m.poster_path and m.backdrop_path:
                # Obtener los géneros si están disponibles
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

        return jsonify(results), 200

    except Exception as e:
        # Manejo de errores generales
        return jsonify({"error": "Error al procesar la solicitud", "details": str(e)}), 500
