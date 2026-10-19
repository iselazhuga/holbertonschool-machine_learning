#!/usr/bin/env python3
"""Return the home planets of all sentient species."""
import requests


def sentientPlanets():
    """Return the names of the home planets of all sentient species.

    A species is sentient if the word appears in its classification
    or its designation. Follows the pagination of the species endpoint,
    remembers planets already fetched and lists each planet once.
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []
    cache = {}
    while url:
        data = requests.get(url).json()
        for species in data.get("results", []):
            kind = "{} {}".format(species.get("classification", ""),
                                  species.get("designation", "")).lower()
            if "sentient" not in kind:
                continue
            homeworld = species.get("homeworld")
            if not homeworld:
                continue
            if homeworld not in cache:
                cache[homeworld] = requests.get(homeworld).json().get("name")
                planets.append(cache[homeworld])
        url = data.get("next")
    return planets
