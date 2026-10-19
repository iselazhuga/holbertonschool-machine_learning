#!/usr/bin/env python3
"""Return the starships that can hold a given number of passengers."""
import requests


def availableShips(passengerCount):
    """Return the names of ships that can carry at least passengerCount.

    Follows the pagination of the SWAPI starships endpoint and
    returns an empty list if no ship is available.
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []
    while url:
        data = requests.get(url).json()
        for ship in data.get("results", []):
            passengers = ship.get("passengers", "").replace(",", "")
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship.get("name"))
        url = data.get("next")
    return ships
