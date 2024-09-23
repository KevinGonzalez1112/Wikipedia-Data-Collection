
import pywikibot as pwb


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the page  
    content statistics.
----------------------------------------------------------------------------
"""


def get_page_images(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Get the number of images as a list

    images = list(page.imagelinks())

    # Return the number of images

    return len(images)


def get_page_backlinks(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Get the number of backlinks as a list

    back_links = list(page.backlinks())

    # Return the number of backlinks

    return len(back_links)


def get_page_ext_links(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Get the number of external links as a list

    ext_links = list(page.extlinks())

    # Return the number of external links

    return len(ext_links)


def get_page_linked_pages(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Get the number of internal links as a list

    linked_pages = list(page.linkedPages())

    # Return the number of internal links

    return len(linked_pages)
