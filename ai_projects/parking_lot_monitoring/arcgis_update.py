from arcgis.gis import GIS
import requests

gis = GIS("https://www.arcgis.com", "SurajitPatra", "JH05ct@1031")
item = gis.content.get("your_feature_layer_id")
layer = item.layers[0]

def update_parking_layer():
    response = requests.get("http://127.0.0.1:8000/get_parking_status/")
    parking_status = response.json()

    features = []
    for feature in layer.query().features:
        spot_id = feature.attributes["SpotID"]  # Ensure your ArcGIS layer has a "SpotID" field
        if spot_id in parking_status:
            feature.attributes["Status"] = parking_status[spot_id]  # 1 for occupied, 0 for empty
            features.append(feature)

    if features:
        layer.edit_features(updates=features)
        print("ArcGIS map updated successfully.")

update_parking_layer()
