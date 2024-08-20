def mood_response(mood):
    mood = mood.lower() 
    responses = {
        "happy": "That's great! Keep smiling!",
        "sad": "I'm sorry to hear that. Hope things get better soon.",
        "excited": "Awesome! What's got you so excited?",
        "tired": "Take some rest. You deserve it.",
        "angry": "Take a deep breath. It will be okay.",
    }
    return responses.get(mood, "I don't know that mood, but I hope you feel good soon!")
