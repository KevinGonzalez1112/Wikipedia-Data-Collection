
import requests
import json
import pywikibot as pwb


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the edit and 
    editor details for the revisions made to each page.
----------------------------------------------------------------------------
"""


def get_page_total_revisions(revisions):

    # Return the total number of revisions made to a page

    return len(revisions)


def get_page_total_contributors(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Use PyWikiBot to find the total number of editors

    contributors = page.contributors()

    # Return the total number of editors for a page

    return len(contributors)


def get_page_anon_stats(revisions):

    anon_edits = 0

    # Creating an array to store the editors associated with each edit

    anon_editors = []

    # Adding the revisions that have been made by anonymous or IP contributor to an array

    for Revision in revisions:

        if Revision.anon:

            anon_edits = anon_edits + 1

            anon_editors.append(Revision.user)

    # Converting this array into a set to only keep unique instance of the users id

    unique_anon_contributors = set(anon_editors)

    # Finding the length to return the number of unique contributors

    anon_contributors = len(unique_anon_contributors)

    # Return the anon editors stats

    return anon_edits, anon_contributors


def get_page_bot_stats(article):

    bot_edits = 0

    unique_bot_count = 0

    # Link to the articles page on Xtools API

    link = 'https://xtools.wmcloud.org/api/page/bot_data/enwiki/' + article

    # Using requests to get the API data from response

    response = requests.get(link).text

    # Converting the response data to JSON format

    response_info = json.loads(response)

    # Loop through the dictionary containing bots and their edits

    for bot in response_info['bots']:

        # Add the number of edits made by the bot to total

        bot_edits = bot_edits + response_info['bots'][bot]['count']

        # Then increment the unique bot counter by 1

        unique_bot_count = unique_bot_count + 1

    # Return the bot editors stats

    return bot_edits, unique_bot_count
