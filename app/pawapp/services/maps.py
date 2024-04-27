import geocoder
import httpx


def get_location() -> list[float]:
    g = geocoder.ip('me')
    return g.latlng

"""
curl -X POST -d '{
  "includedTypes": ["restaurant"],
  "maxResultCount": 10,
  "locationRestriction": {
    "circle": {
      "center": {
        "latitude": 37.7937,
        "longitude": -122.3965},
      "radius": 500.0
    }
  }
}' \
-H 'Content-Type: application/json' -H "X-Goog-Api-Key: API_KEY" \
-H "X-Goog-FieldMask: places.displayName" \
https://places.googleapis.com/v1/places:searchNearby

"""

def get_shops_near(lat: float, lng: float):
    response = httpx.post(
        url='https://places.googleapis.com/v1/places:searchNearby',
        data={
            "includedTypes": ["restaurant"],
            "maxResultCount": 10,
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": 37.7937,
                        "longitude": -122.3965
                    },
                    "radius": 50.0
                }
            }
        }
        #https://developers.google.com/maps/documentation/places/web-service/nearby-search?hl=ru
    )

    print(response.json())
