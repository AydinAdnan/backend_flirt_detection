import random
import pandas as pd

def generate_flirtation_dataset(num_entries=2000):
    """
    Generate a dataset of messages with flirtation scores (0-100)
    
    Score ranges:
    0-15: Neutral/Professional messages
    16-40: Friendly messages
    41-70: Mildly flirtatious
    71-90: Clearly flirtatious
    91-100: Very flirtatious/romantic
    """
    
    # Message templates organized by flirtation level
    neutral_professional = [
        "Can you send me the report by tonight?",
        "Did you finish the homework?",
        "Don't forget about tomorrow's meeting",
        "Thanks for the reminder",
        "What time is the presentation?",
        "Can we schedule a call for next week?",
        "Please review the attached document",
        "The deadline is approaching",
        "Can you help me with this task?",
        "Let me know if you need any clarification",
        "Can we work on the project together?",
        "What's the status on that assignment?",
        "Did you get my email?",
        "The meeting has been moved to 3 PM",
        "Please confirm your attendance",
        "I need the files by Friday",
        "Can you double-check these numbers?",
        "The client wants to reschedule",
        "Have you seen the latest updates?",
        "Let's discuss this in detail tomorrow"
    ]
    
    friendly = [
        "Hey, how are you doing?",
        "Good morning, hope you have a great day!",
        "What's your favorite movie?",
        "Haha that was funny 😂",
        "Thanks for helping me out",
        "I appreciate your advice",
        "That joke cracked me up haha",
        "You're really talented",
        "That's so thoughtful of you",
        "Hope you're having a good week",
        "Hope your day is going well!",
        "That was a great presentation",
        "You did really well on that project",
        "Thanks for being so helpful",
        "You're such a good friend",
        "I enjoy our conversations",
        "You have a great sense of humor",
        "That's a really good point",
        "You're very insightful",
        "I love your positive energy",
        "What's the vibe today? 😊",
        "Just dropping in to say hey! 👋",
        "That was a whole mood, lol.",
        "Your energy is a total W. ✨",
        "Lowkey glad we're on the same team.",
        "That's a slay, no cap.",
        "I'm dead, that's so funny 😂💀",
        "Hope your day is bussin' 🙌",
        "This convo is lowkey a good vibe.",
        "You're not giving basic at all.",
        "I stan your work ethic.",
        "That's so real, fr fr.",
        "On God, you're a good person.",
        "You're not sus, you're just cool.",
        "Thanks for the tea, spill it all! ☕"
    ]
    
    mildly_flirtatious = [
        "Wanna grab lunch sometime?",
        "I had fun hanging out with you",
        "Let's go for coffee sometime ☕",
        "You're really fun to be around",
        "Let's hang out soon",
        "Wanna grab a drink tonight?",
        "I admire how talented you are",
        "You always make me laugh",
        "Want to catch a movie this weekend?",
        "You have great taste in music",
        "We should do this more often",
        "I really enjoy spending time with you",
        "You make work more enjoyable",
        "Want to try that new restaurant?",
        "You brighten up the room",
        "I always look forward to seeing you",
        "You have such a warm personality",
        "We have so much in common",
        "You're really easy to talk to",
        "I feel so comfortable around you",
        "Let's grab a coffee or something sometime. No cap.",
        "I'm not gonna lie, you're pretty cool. 😉",
        "Lowkey been thinking about that convo we had.",
        "You're giving main character energy.",
        "I'm highkey excited to see you.",
        "I'm not even trying to rizz you up, but you're a vibe.",
        "Your 'fit was fire today, no cap.",
        "You looked like a whole snack today.",
        "My day was mid until I saw your text.",
        "I'm lowkey catching feelings, lol.",
        "You have a mad good aura.",
        "Just saying, you're not like everyone else.",
        "You're a whole W in my book.",
        "I'm so glad we're talking. ✨",
        "I'm on a no-rizz streak, but you're making it hard."
    ]
    
    clearly_flirtatious = [
        "You look amazing in that dress",
        "You've got the most beautiful smile 😊",
        "You looked really cute today",
        "You're so cute when you laugh",
        "Wanna watch a movie at my place?",
        "That dress suits you so well",
        "You make everything better when you're around",
        "You looked fire 🔥 today",
        "I can't stop smiling when I'm with you",
        "Looking at you makes my day better",
        "You have the most beautiful laugh",
        "You look incredible today",
        "That color looks amazing on you",
        "You have such pretty hair",
        "Your smile is contagious",
        "You're absolutely radiant",
        "You have such beautiful features",
        "You look stunning as always",
        "You're so photogenic",
        "You have the prettiest eyes",
        "You're giving me all the feels. ❤️",
        "Your smile hits different, for real.",
        "I'm not trying to be delulu, but I think you're stunning.",
        "I'm so glad I slid into your DMs. 😉",
        "You're a whole mood and a whole snack.",
        "Stop making me blush, you're too cute.",
        "You have so much rizz, it's not fair.",
        "Every time you text me, my phone does a happy dance.",
        "You're my favorite notification.",
        "I think about you when I'm bored. And when I'm not. 😉",
        "I'm lowkey obsessed with you.",
        "I can't get over how good you look.",
        "Your energy is so attractive, it's wild.",
        "If you're ever free, I'm dtf... to define the relationship. 😉",
        "I'm not even playing, you're a perfect 10."
    ]
    
    very_flirtatious = [
        "Wow, you're absolutely gorgeous 😍",
        "I'm so lucky to know you ❤️",
        "I think I'm starting to like you a lot 💕",
        "You make my heart race every time I see you",
        "Your eyes are mesmerizing 👀",
        "Hey gorgeous, what are you up to?",
        "I'd love to spend more time with you ❤️",
        "You looked stunning last night ✨",
        "You're such a sweetheart 💕",
        "I keep thinking about you 😘",
        "You take my breath away",
        "I can't get you out of my mind",
        "You're everything I've been looking for",
        "You make me feel so special",
        "I'm completely smitten with you 💕",
        "You're the girl of my dreams",
        "I'm falling for you hard",
        "You make my heart skip a beat",
        "I think about you all the time",
        "You're my favorite person ❤️",
        "You're the kind of person I want to text all day.",
        "Can't believe I found someone as perfect as you.",
        "I'm simping hard for you, no cap.",
        "You're my favorite person to stalk... I mean, talk to. 😉",
        "My hands are full, can I borrow your mouth? Just kidding. Unless...?",
        "Your body is a masterpiece, you're an artist.",
        "Just thinking about you makes me smile like a clown.",
        "I'd go delulu for you.",
        "You're my biggest W, for real.",
        "I hope this isn't a situationship, because I want you all to myself."
    ]
    
    extremely_flirtatious = [
        "You're the prettiest girl in the room",
        "You're the best thing that happened to me ❤️",
        "You're driving me crazy in the best way",
        "You're my sunshine ☀️",
        "You looked so hot yesterday 🔥",
        "You're drop-dead gorgeous 😍",
        "You're the reason I'm so happy",
        "That outfit is 🔥🔥🔥",
        "You're irresistible 😘",
        "You're absolutely perfect 💕",
        "You're the most beautiful woman I've ever seen",
        "I'm crazy about you 😍",
        "You're absolutely divine",
        "You're perfect in every way",
        "I'm head over heels for you",
        "You're my dream come true",
        "I worship the ground you walk on",
        "You're a goddess 👑",
        "I can't resist you",
        "You're my everything ❤️💕",
        "I'm head over heels for you, no cap.",
        "You're my everything, periodt. ❤️",
        "I'm addicted to you and I'm not looking for a cure.",
        "I want to be your sneaky link and your forever link.",
        "I'm literally weak for you.",
        "You're the only person who gives me butterflies.",
        "You're a whole snack, a whole meal, a whole buffet.",
        "I wanna be the one you catch feels for.",
        "If you were a test, I'd fail and still get a W because you're mine.",
        "My life has been a blur, but with you, it's on God."
    ]
    
    # Combine all message categories
    all_messages = {
        'neutral': neutral_professional,
        'friendly': friendly,  
        'mild': mildly_flirtatious,
        'clear': clearly_flirtatious,
        'very': very_flirtatious,
        'extreme': extremely_flirtatious
    }
    
    # Score ranges for each category
    score_ranges = {
        'neutral': (0, 15),
        'friendly': (16, 40),
        'mild': (41, 70),
        'clear': (71, 90),
        'very': (91, 96),
        'extreme': (97, 100)
    }
    
    # Generate dataset
    dataset = []
    
    for i in range(1, num_entries + 1):
        # Randomly choose a category (weighted to have variety)
        category = random.choices(
            list(all_messages.keys()),
            weights=[15, 20, 25, 20, 15, 5],  # Fewer extreme messages
            k=1
        )[0]
        
        # Select a random message from the chosen category
        message = random.choice(all_messages[category])
        
        # Generate score within the appropriate range
        min_score, max_score = score_ranges[category]
        score = random.randint(min_score, max_score)
        
        # Add some variation to make it more realistic
        if category == 'neutral' and random.random() < 0.1:  # 10% chance
            score = random.randint(0, 5)
        elif category == 'extreme' and random.random() < 0.3:  # 30% chance
            score = random.randint(95, 100)
            
        dataset.append({
            'id': i,
            'message': message,
            'label (score 0–100)': score
        })
    
    return dataset

# Generate the dataset
dataset = generate_flirtation_dataset(2000)

# Convert to DataFrame
df = pd.DataFrame(dataset)

# Display first 20 rows
print("First 20 entries of the generated dataset:")
print(df.head(20).to_string(index=False))

print(f"\nDataset generated with {len(dataset)} entries")
print(f"Score distribution:")
print(f"0-15 (Neutral): {len([d for d in dataset if d['label (score 0–100)'] <= 15])}")
print(f"16-40 (Friendly): {len([d for d in dataset if 16 <= d['label (score 0–100)'] <= 40])}")
print(f"41-70 (Mildly flirtatious): {len([d for d in dataset if 41 <= d['label (score 0–100)'] <= 70])}")
print(f"71-90 (Clearly flirtatious): {len([d for d in dataset if 71 <= d['label (score 0–100)'] <= 90])}")
print(f"91-100 (Very/Extremely flirtatious): {len([d for d in dataset if d['label (score 0–100)'] >= 91])}")

# Save to CSV
df.to_csv('flirtation_dataset.csv', index=False)
print(f"\nDataset saved to 'flirtation_dataset.csv'")