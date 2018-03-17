import json

class Concert(object):
    def __init__(self, band=None, venue=None, date=None):
        self.band = band
        self.venue = venue
        self.date = date

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
