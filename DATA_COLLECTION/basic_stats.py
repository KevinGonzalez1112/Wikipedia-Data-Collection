
import requests
import json


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the basic
    stats for a page such as grade and page views.
----------------------------------------------------------------------------
"""


def get_page_basic_stats(article):

    # Link to the articles page on Xtools API

    link = 'https://xtools.wmcloud.org/api/page/articleinfo/enwiki/' + article

    # Using requests to get the API data from response

    response = requests.get(link).text

    # Converting the response data to JSON format

    response_info = json.loads(response)

    # Assigning the required features from JSON dictionary

    grade = response_info['assessment']['value']

    page_views = response_info['pageviews']

    page_watchers = response_info['watchers']

    # Return the articles basic stats

    return grade, page_views, page_watchers
