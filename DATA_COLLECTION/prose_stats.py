
import requests
import json


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the prose
    stats for a page such as size and sections.
----------------------------------------------------------------------------
"""


def get_prose_stats(article):

    # Link to the articles page on Xtools API

    link = 'https://xtools.wmcloud.org/api/page/prose/enwiki/' + article

    # Using requests to get the API data from response

    response = requests.get(link).text

    # Converting the response data to JSON format

    response_info = json.loads(response)

    # Assigning the required features from JSON dictionary

    size = response_info['bytes']

    characters = response_info['characters']

    words = response_info['words']

    references = response_info['references']

    unique_references = response_info['unique_references']

    sections = response_info['sections']

    # Return the articles prose stats

    return size, characters, words, references, unique_references, sections
