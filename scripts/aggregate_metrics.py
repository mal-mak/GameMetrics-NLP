import os
from metric_extraction import analyze_reviews, TEMPLATE

def load_reviews(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().split("\n\n")  # Assuming double newline separates reviews

def format_analysis(analysis, template):
    report = []
    for category, response in analysis.items():
        responses = template[category]
        formatted_responses = [
            f"☑ {r}" if r == response else f"☐ {r}" for r in responses
        ]
        report.append(f"---{{ {category} }}---\n" + "\n".join(formatted_responses))
    return "\n\n".join(report)

def process_game_reviews(input_dir, output_dir):
    for file_name in os.listdir(input_dir):
        if file_name.endswith("_processed.txt"):
            file_path = os.path.join(input_dir, file_name)
            reviews = load_reviews(file_path)
            analysis = analyze_reviews(reviews, TEMPLATE)
            formatted_report = format_analysis(analysis, TEMPLATE)
            
            game_id = file_name.split("_")[1]  # Extract app_id
            output_file = os.path.join(output_dir, f"game_{game_id}_analysis.txt")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(formatted_report)
            print(f"Analysis saved for game {game_id} in {output_file}")

if __name__ == "__main__":
    INPUT_DIR = "data/processed"
    OUTPUT_DIR = "outputs/summaries"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    process_game_reviews(INPUT_DIR, OUTPUT_DIR)