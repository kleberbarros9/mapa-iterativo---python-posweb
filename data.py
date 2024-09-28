import geopandas as gpd
import json

# Função para carregar o shapefile e converter para GeoJSON
def carregar_dados():
    # Carregar o shapefile com geopandas
    shapefile_path = 'PE_UF_2022/PE_UF_2022.shp'
    pe = gpd.read_file(shapefile_path)

    # Dados dos municípios (essa parte pode ser movida para um banco de dados no futuro)
    municipios = [
        {
            "municipio": "Bonito",
            "apicultores": 50,
            "mulheres": 30,
            "producao": "10 mil litros",
            "lng": -35.7265,
            "lat": -8.47038
        },

        {
            "municipio": "Oricuri",
            "apicultores": 90,
            "mulheres": 50,
            "producao": "15 mil litros",
            "lng": -40.0783,
            "lat": -7.87793
        },


        {
            "municipio": "Barreiros",
            "apicultores": 100,
            "mulheres": 60,
            "producao": "10 mil litros",
            "lng": -35.1901,
            "lat": -8.80765
        },
        {
            "municipio": "Serra Talhada",
            "apicultores": 50,
            "mulheres": 30,
            "producao": "10 mil litros",
            "lng": -38.2929,
            "lat": -7.98526
        }
    ]

    # Converter shapefile para GeoJSON
    pe_geojson = pe.to_json()

    # Retornar os dados dos municípios e do shapefile
    return {
        "municipios": municipios,
        "pe_geojson": json.loads(pe_geojson)
    }
