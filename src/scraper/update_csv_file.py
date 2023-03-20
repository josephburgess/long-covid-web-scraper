import pandas as pd


def update_csv_file(file_path, new_articles):
    # Read the existing CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame()

    # Convert the DataFrame into a list of dictionaries
    existing_articles = df.to_dict(orient='records')

    # Combine the list of dictionaries from the DataFrame with the new articles
    combined_articles = existing_articles + new_articles

    # Remove duplicates based on the title
    seen_titles = set()
    deduplicated_articles = []
    for article in combined_articles:
        if article['title'] not in seen_titles:
            seen_titles.add(article['title'])
            deduplicated_articles.append(article)

    # Create a new DataFrame with the combined and deduplicated list
    updated_df = pd.DataFrame(deduplicated_articles)

    # Write the new DataFrame to the CSV file
    updated_df.to_csv(file_path, index=False)


# In your main function or after you have scraped the articles
