# -*- coding: utf-8 -*-

"""Console script for red_scare_tour_dates."""
import sys
import json
import subprocess
from names import dataFolder
import os
from red_scare import RedScare


def main(args=None):
    """Console script for red_scare_tour_dates."""

    redScare = RedScare()

    concerts = redScare.parseTourPage()

    resultsJsonFile = os.path.join(dataFolder, 'results.json')

    with open(resultsJsonFile, 'w+') as f:
        results = []
        for concert in concerts:
            cJSON = json.dumps(concert.__dict__)
            cJSON = cJSON.replace('\"', '"')
            cJSON = cJSON.replace('"{', '{')
            cJSON = cJSON.replace('}"', '}')
            results.append(cJSON)
        json.dump(results, f, ensure_ascii=False, indent=4, sort_keys=True)


    bash4 = f"scp {resultsJsonFile} droplet:/var/www/html/shows/index.json"
    subprocess.run(bash4.split())

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
