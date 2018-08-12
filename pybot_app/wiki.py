""" Wiki class get any informations on a object from Wikipédia.org """

import requests

class Wiki():
    """ Manage the call and results of Wiki Media API """

    def __init__(self, address_keyword):
        self.address_keyword = address_keyword
        self._result = self._get_wiki_informations()

    def _get_wiki_informations(self):
        """
        Call Wiki Media API with address keyword
        Return the first address informations in json
        """

        _r = requests.get("https://fr.wikipedia.org/w/api.php?format=json&action=opensearch&search="
                          + self.address_keyword +
                          "&limit=1")
        _result = _r.json()

        return _result
    
    @property
    def entity(self):
        """ Return the object entity """
        return self._result[1][0]

    @property
    def details(self):
        """ Return the object details """
        return self._result[2][0]
    
    @property
    def wiki_link(self):
        """ Return the object Wikipedia link """
        return self._result[3][0]