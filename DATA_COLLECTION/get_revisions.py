
import pywikibot as pwb


"""
----------------------------------------------------------------------------
    Creating the function that will extract every revision made
    to a page using the PyWikiBot API.
----------------------------------------------------------------------------
"""


def get_page_revisions(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Getting all the revisions made to a page

    revisions = page.revisions()

    # Converting these to a list to make further work simpler

    revisions_list = list(revisions)

    # Return all the revisions made to a page and their details

    return revisions_list
