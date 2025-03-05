# metric_extraction.py

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

# Define the template
TEMPLATE = {
    # Visual and Aesthetic Quality
    "Graphics": [
        "Masterpiece - You forget what reality is",
        "Beautiful and immersive",
        "Good visuals",
        "Decent, gets the job done",
        "Outdated and dull",
        "Bad - Looks like MS-DOS",
    ],
    # Gameplay Mechanics and Enjoyment
    "Gameplay": [
        "Incredible - Truly unforgettable",
        "Very good and engaging",
        "Good but nothing groundbreaking",
        "Decent but repetitive",
        "Boring, better to watch paint dry",
        "Frustrating and unplayable",
    ],
    # Sound Design and Audio Experience
    "Audio": [
        "Eargasmic - Simply amazing",
        "Very good sound quality",
        "Good, adds to the experience",
        "Not bad but forgettable",
        "Poor sound design",
        "Terrible - You might want earplugs",
    ],
    # System Resource Demands
    "PC Requirements": [
        "Runs on anything - Even a toaster",
        "Low requirements - Potato-friendly",
        "Reasonable for most PCs",
        "Fast but needs a decent machine",
        "Rich boi territory - High-end rig required",
        "Ask NASA for a computer",
    ],
    # Game Difficulty
    "Difficulty": [
        "Too easy - Just press 'W'",
        "Casual - Good for beginners",
        "Balanced - Easy to learn, hard to master",
        "Challenging but fair",
        "Brutal difficulty - Significant brain usage",
        "Insane - Dark Souls level",
    ],
    # Effort Required for Progression
    "Grind": [
        "No grind - Progress is smooth",
        "Minimal grind - Optional for ranks",
        "Moderate grind - Feels natural",
        "Average grind level - Manageable",
        "Heavy grind - Feels excessive",
        "Grindfest - Requires a second life",
    ],
    # Storyline and Narrative Quality
    "Story": [
        "Nonexistent - No story at all",
        "Minimal - Some lore here and there",
        "Average - Serves its purpose",
        "Good - Well-written and engaging",
        "Lovely - Emotionally impactful",
        "Masterpiece - Replaces your real life",
    ],
    # Duration of Playtime
    "Game Time": [
        "Short - Enough for a cup of coffee",
        "Brief - You'll finish in a few hours",
        "Average length - Decent playtime",
        "Long - Lots to explore",
        "Endless - To infinity and beyond",
    ],
    # Value for Money
    "Price": [
        "Free - No brainer!",
        "Worth every penny",
        "Good if on sale",
        "Fair if you have spare money",
        "Overpriced - Not recommended",
        "Burn your money instead",
    ],
    # Bugs and Stability
    "Bugs": [
        "Flawless - Never heard of bugs",
        "Minor bugs - Barely noticeable",
        "Occasional bugs - Can get annoying",
        "Buggy - ARK: Survival Evolved level",
        "Unplayable - Full of game-breaking bugs",
    ],
    # Overall Rating
    "Rating": [
        "1 - Terrible",
        "2 - Poor",
        "3 - Below Average",
        "4 - Mediocre",
        "5 - Average",
        "6 - Decent",
        "7 - Good",
        "8 - Very Good",
        "9 - Excellent",
        "10 - Masterpiece",
    ],
}


# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens


# Matching logic
def match_review_to_category(review, category, responses):
    tokens = preprocess_text(review)
    response_scores = {response: 0 for response in responses}
    for response in responses:
        response_tokens = preprocess_text(response)
        response_scores[response] = sum(
            1 for token in tokens if token in response_tokens
        )
    best_response = max(response_scores, key=response_scores.get)
    return best_response if response_scores[best_response] > 0 else None


# Aggregation logic
def analyze_reviews(reviews, template):
    analysis = defaultdict(str)
    for category, responses in template.items():
        category_matches = []
        for review in reviews:
            match = match_review_to_category(review, category, responses)
            if match:
                category_matches.append(match)
        if category_matches:
            analysis[category] = max(set(category_matches), key=category_matches.count)
    return analysis
