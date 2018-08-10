""" Map class get any address informations who exist on OpenStreetMap.org """

import requests

class Map():
    """ Manage the call and results of OpenStreetMap.org API """

    def __init__(self, address_keyword):
        self.address_keyword = address_keyword
        self._result = self._get_map_informations()

    def _get_map_informations(self):
        """
        Call OpenStreetMap.org API with address keyword
        Return the first address informations in json
        """

        _r = requests.get("https://nominatim.openstreetmap.org/search/?format=json&q="
                          + self.address_keyword +
                          "&addressdetails=1&limit=1")
        _result = _r.json()

        return _result
    
    @property
    def latitude(self):
        """ Return the address latitude """
        return self._result[0]["lat"]

    @property
    def longitude(self):
        """ Return the address longitude """
        return self._result[0]["lon"]

    @property
    def details(self):
        """ Return a dictionnary with address details (house number, street, city...) """
        return self._result[0]["address"]
