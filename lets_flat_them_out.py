from typing import Dict

x = {
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"
            }
        }
    }

def flatten(dictionary: Dict):

    updated_dict = {}

    for key, value in dictionary.items():
        print(key, value)


flatten(x)



