import os
import json
from steamreviews import download_reviews_for_app_id_batch

# Configuration
OUTPUT_DIR = "data/raw"  # Directory to save the raw reviews


def scrape_reviews(output_dir):
    """
    Scrape Steam reviews for a specific app and save them locally.

    Args:
        app_id (int): The Steam App ID of the game.
        output_dir (str): Directory to save the raw reviews.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    request_params = dict()
    request_params["language"] = "english"
    request_params['filter'] = 'all'
    request_params["day_range"] = "10"

    print(f"Starting to scrape reviews ...")
    try:
        # Call download_reviews_for_app_id_batch to get the reviews
        _, query_summary = download_reviews_for_app_id_batch(
            verbose=True, chosen_request_params=request_params
        )

        # Generate the file path to save the reviews
        # reviews_path = os.path.join(output_dir, f"{app_id}.json")

        # Save the reviews to the file
        # save_reviews_to_file(app_id, reviews, reviews_path)

        # Print query summary
        print("Summary of fetched reviews:")
        print(query_summary)

    except Exception as e:
        print(f"An error occurred while scraping reviews: {e}")


if __name__ == "__main__":
    scrape_reviews(OUTPUT_DIR)
