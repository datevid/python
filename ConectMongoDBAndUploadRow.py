from pymongo import MongoClient
from typing import Dict, Any

# Configuración de MongoDB
MONGODB_URI = "DB_URI"

def connect_to_mongodb():
    """Establece una conexión con MongoDB."""
    try:
        client = MongoClient(MONGODB_URI)
        return client
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")
        return None

def insert_track(client, track_data: Dict[str, Any]) -> str:
    """
    Inserta un nuevo track en la base de datos MongoDB.
    
    :param client: Conexión al cliente MongoDB.
    :param track_data: Un diccionario con los datos del track.
    :return: ID del track insertado si fue exitoso, None en caso contrario.
    """
    try:
        db = client['tracks_db']
        collection = db['tracks']
        result = collection.insert_one(track_data)
        print(f"Track insertado con ID: {track_data['id']}")
        return track_data['id']
    except Exception as e:
        print(f"Error al insertar el track: {e}")
        return None

def get_track_by_id(client, track_id: str) -> Dict[str, Any]:
    """
    Recupera un track de la base de datos MongoDB por su ID personalizado.
    
    :param client: Conexión al cliente MongoDB.
    :param track_id: ID personalizado del track a buscar.
    :return: Diccionario con los datos del track si se encuentra, None en caso contrario.
    """
    try:
        db = client['tracks_db']
        collection = db['tracks']
        track = collection.find_one({"id": track_id})
        if track:
            track['_id'] = str(track['_id'])  # Convertir ObjectId a string para facilitar la serialización
        return track
    except Exception as e:
        print(f"Error al recuperar el track: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    client = connect_to_mongodb()
    if not client:
        print("No se pudo conectar a la base de datos. Saliendo...")
        exit(1)

    sample_track = {
        "id": "TRACK12345",  # ID personalizado
        "video_url": "https://example.com/video.mp4",
        "audio_url": "https://example.com/audio.mp3",
        "image_url": "https://example.com/image.jpg",
        "image_large_url": "https://example.com/image_large.jpg",
        "is_video_pending": False,
        "major_model_version": "1.0",
        "model_name": "SampleModel",
        "metadata": {
            "tags": "sample, test",
            "prompt": "A sample track",
            "type": "music",
            "duration": 180.5
        },
        "is_liked": False,
        "user_id": "user123",
        "display_name": "Sample User",
        "handle": "sampleuser",
        "is_handle_updated": True,
        "avatar_image_url": "https://example.com/avatar.jpg",
        "is_trashed": False,
        "created_at": "2023-07-19T12:00:00Z",
        "status": "active",
        "title": "Sample Track",
        "play_count": 0,
        "upvote_count": 0,
        "is_public": True
    }

    # Insertar un track
    inserted_id = insert_track(client, sample_track)
    if inserted_id:
        print(f"Track insertado exitosamente con ID: {inserted_id}")

        # Recuperar el track insertado usando el ID personalizado
        retrieved_track = get_track_by_id(client, inserted_id)
        if retrieved_track:
            print("Track recuperado:")
            print(retrieved_track)
        else:
            print("No se pudo recuperar el track.")
    else:
        print("No se pudo insertar el track.")

    # Cerrar la conexión
    client.close()