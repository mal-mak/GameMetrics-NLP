import os
import json

INPUT_DIR = "data/raw"
OUTPUT_DIR = "data/processed"

def remove_lines_with_unchecked(review_text):
    # Split the review into individual lines
    lines = review_text.split("\n")
    
    # Filter out lines that contain the ☐ symbol (unchecked items)
    filtered_lines = [line for line in lines if "☐" not in line]
    
    # Join the filtered lines back into a single string
    filtered_review = "\n".join(filtered_lines)
    
    return filtered_review

def extract_reviews_for_game(input_dir, output_dir, app_id):
    # Construct the file path for the current game
    file_path = os.path.join(input_dir, f"review_{app_id}.json")
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            reviews_data = []
            
            # Extract reviews from the JSON data
            for review_id, review_info in data.get("reviews", {}).items():
                review_text = review_info.get("review", "")
                
                # Remove lines with unchecked items (☐)
                filtered_review = remove_lines_with_unchecked(review_text)
                
                # Add the filtered review to the list
                reviews_data.append(filtered_review)
        
        # Save the reviews to a text file with double newlines separating reviews
        output_file = os.path.join(output_dir, f"review_{app_id}_processed.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(reviews_data))
        
        print(f"Reviews for game {app_id} extracted and saved to {output_file}")
    else:
        print(f"File for game {app_id} not found!")

def process_all_games(input_dir, output_dir):
    # Loop through all files in the directory and process each game based on its file name
    for file_name in os.listdir(input_dir):
        if file_name.startswith("review_") and file_name.endswith(".json"):
            print(f"Processing file: {file_name}")  # Debug statement
            app_id = file_name.split("_")[1].split(".")[0]  # Extract the app_id from the file name
            extract_reviews_for_game(input_dir, output_dir, app_id)
        else:
            print(f"Skipping non-review file: {file_name}")  # Debug statement

if __name__ == "__main__":
    # Directory containing the raw reviews
    print(os.getcwd())
    process_all_games(INPUT_DIR, OUTPUT_DIR)