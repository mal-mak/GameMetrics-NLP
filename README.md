# GameMetrics-NLP
Analyze Steam game reviews to generate aggregated metrics using NLP.

## Features
- Scrapes game reviews from Steam:
	* Using ```steamreviews``` package
	* Strore the reviews in ```/data/raw```
- Preprocesses reviews into a clean corpus:
	* Split lines
	* Remove unnecessary information
	* Store in ```/data/processed```
- Extract the metrics that are interesting for us:
	* Using ```nltk word_tokenize``` and ```nltk stopwords```
	* 
- Aggregates, for each game, detailed metrics like gameplay, graphics, and more:
	* Store results in ```/outputs/summaries```
	* The results will be in the following format :
	```
		---{ Graphics }---  
		☐ Masterpiece - You forget what reality is  
		☐ Beautiful and immersive  
		☑ Good visuals  
		☐ Decent, gets the job done  
		☐ Outdated and dull  
		☐ Looks like MS-DOS  

		---{ Gameplay }---
		☐ Incredible - Truly unforgettable
		☑ Very good and engaging
		☐ Good but nothing groundbreaking
		☐ Decent but repetitive
		☐ Boring, better to watch paint dry
		☐ Frustrating and unplayable

		---{ Audio }---
		☐ Eargasmic - Simply amazing
		☑ Very good sound quality
		☐ Good, adds to the experience
		☐ Not bad but forgettable
		☐ Poor sound design
		☐ Terrible - You might want earplugs

		---{ PC Requirements }---
		☑ Runs on anything - Even a toaster
		☐ Low requirements - Potato-friendly
		☐ Reasonable for most PCs
		☐ Fast but needs a decent machine
		☐ Rich boi territory - High-end rig required
		☐ Ask NASA for a computer

		---{ Difficulty }---
		☐ Too easy - Just press 'W'
		☑ Casual - Good for beginners
		☐ Balanced - Easy to learn, hard to master
		☐ Challenging but fair
		☐ Brutal difficulty - Significant brain usage
		☐ Insane - Dark Souls level

		---{ Grind }---
		☐ No grind - Progress is smooth
		☐ Minimal grind - Optional for ranks
		☐ Moderate grind - Feels natural
		☐ Average grind level - Manageable
		☐ Heavy grind - Feels excessive
		☑ Grindfest - Requires a second life

		---{ Story }---
		☐ Nonexistent - No story at all
		☐ Minimal - Some lore here and there
		☐ Average - Serves its purpose
		☑ Good - Well-written and engaging
		☐ Lovely - Emotionally impactful
		☐ Masterpiece - Replaces your real life

		---{ Game Time }---
		☐ Short - Enough for a cup of coffee
		☑ Brief - You'll finish in a few hours
		☐ Average length - Decent playtime
		☐ Long - Lots to explore
		☐ Endless - To infinity and beyond

		---{ Price }---
		☐ Free - No brainer!
		☐ Worth every penny
		☑ Good if on sale
		☐ Fair if you have spare money
		☐ Overpriced - Not recommended
		☐ Burn your money instead

		---{ Bugs }---
		☐ Flawless - Never heard of bugs
		☐ Minor bugs - Barely noticeable
		☑ Occasional bugs - Can get annoying
		☐ Buggy - ARK: Survival Evolved level
		☐ Unplayable - Full of game-breaking bugs

		---{ Rating }---
		☐ 1 - Terrible
		☐ 2 - Poor
		☐ 3 - Below Average
		☐ 4 - Mediocre
		☐ 5 - Average
		☐ 6 - Decent
		☑ 7 - Good
		☐ 8 - Very Good
		☐ 9 - Excellent
		☐ 10 - Masterpiece
```
## Requirements
```python version 3.11.10```

## Installation
```bash
pip install -r requirements.txt