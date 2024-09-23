
from DATA_COLLECTION.get_articles import *

from DATA_COLLECTION.get_revisions import *

from DATA_COLLECTION.basic_stats import *

from DATA_COLLECTION.prose_stats import *

from DATA_COLLECTION.edit_and_editor_stats import *

from DATA_COLLECTION.further_edit_stats import *

from DATA_COLLECTION.content_stats import *

from DATA_COLLECTION.temporal_stats import *


if __name__ == '__main__':

    # Create empty DataFrame to store metadata

    dataframe_data = []

    # Get list of articles

    articles = get_articles('JSON_FILES/TESTING_ARTICLES.json')

    for article in articles:

        basic_stats = get_page_basic_stats(article)

        prose_stats = get_prose_stats(article)

        page_age = get_page_age(article)

        revisions = get_page_revisions(article)

        total_revisions = get_page_total_revisions(revisions)

        anon_stats = get_page_anon_stats(revisions)

        bot_stats = get_page_bot_stats(article)

        registered_edits = (total_revisions - anon_stats[0] - bot_stats[0])

        major_minor = get_major_or_minor(revisions)

        edit_size_stats = get_edit_size_stats(revisions)

        avg_time_btwn_edits = get_avg_time_between_edits(revisions)

        avg_edits_per = get_avg_edits_per(revisions)

        lull_stats = get_lull_stats(revisions)

        total_contributors = get_page_total_contributors(article)

        registered_contributors = (total_contributors - anon_stats[1] - bot_stats[1])

        img_count = get_page_images(article)

        backlinks = get_page_backlinks(article)

        ext_links = get_page_ext_links(article)

        linked_pages = get_page_linked_pages(article)

        # Add the data to the initial array

        dataframe_data.append([article,
                               basic_stats[0],
                               prose_stats[0],
                               prose_stats[1],
                               prose_stats[2],
                               prose_stats[5],
                               page_age,
                               basic_stats[1],
                               basic_stats[2],
                               total_revisions,
                               registered_edits,
                               anon_stats[0],
                               bot_stats[0],
                               major_minor[0],
                               major_minor[1],
                               edit_size_stats[0],
                               edit_size_stats[1],
                               edit_size_stats[2],
                               avg_time_btwn_edits[0],
                               avg_time_btwn_edits[1],
                               avg_time_btwn_edits[2],
                               avg_edits_per[0],
                               avg_edits_per[1],
                               avg_edits_per[2],
                               avg_edits_per[3],
                               avg_edits_per[4],
                               avg_edits_per[5],
                               lull_stats[0],
                               lull_stats[1],
                               lull_stats[2],
                               lull_stats[3],
                               total_contributors,
                               registered_contributors,
                               anon_stats[1],
                               bot_stats[1],
                               img_count,
                               backlinks,
                               ext_links,
                               linked_pages,
                               prose_stats[3],
                               prose_stats[4]
                               ])

    # Convert the initial array into a DataFrame and include the titles

    articles_df = pd.DataFrame(data = dataframe_data,
                               columns =
                               [
                                   'Title',
                                   'Assessment Grade',
                                   'Page Size',
                                   'Character Count',
                                   'Word Count',
                                   'Section Count',
                                   'Page Age',
                                   'Page Views',
                                   'Page Watchers',
                                   'Total Edits',
                                   'Registered Edits',
                                   'Anon Edits',
                                   'Bot Edits',
                                   'Major Edits',
                                   'Minor Edits',
                                   'Edit Size (25th PRC)',
                                   'Edit Size (Median)',
                                   'Edit Size (75th PRC)',
                                   'Time Btwn Edits (25th)',
                                   'Time Btwn Edits (Median)',
                                   'Time Btwn Edits (75th)',
                                   'Edits per Month (25th)',
                                   'Edits per Month (Median)',
                                   'Edits per Month (75th)',
                                   'Edits per Year (25th)',
                                   'Edits per Year (Median)',
                                   'Edits per Year (75th)',
                                   'Lull Count',
                                   'Lull Duration (25th)',
                                   'Lull Duration (Median)',
                                   'Lull Duration (75th)',
                                   'Total Contributors',
                                   'Registered Contributors',
                                   'Anon Contributors',
                                   'Bot Contributors',
                                   'Image Count',
                                   'Backlinks',
                                   'External Links',
                                   'Internal Links',
                                   'References',
                                   'Unique References'
                               ])

    # Save dataframe to a CSV file
    # Change this path to the place you wish to save your outputted file

    articles_df.to_csv(r'C:\Users\Kevin\Desktop\TEST.csv', index = False, header = True)