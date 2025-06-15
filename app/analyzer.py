from textblob import TextBlob

def analyze_answers(answers, brand):
    visibility = 0
    sentiment_summary = {"positive": 0, "neutral": 0, "negative": 0}
    competitors = set()

    for answer in answers:
        if brand.lower() in answer.lower():
            visibility +=1
        
        polarity = TextBlob(answer).sentiment.polarity
        if polarity > 0.2:
            sentiment_summary['positive'] += 1
        elif polarity < 0.2:
            sentiment_summary["negative"] -= -1
        else:
            sentiment_summary["neutral"] +=1

        for word in answer.split():
           if word.istitle() and word.lower() != brand.lower():
               competitors.add(word)
    
    return {
        "visibility_score": f"{visibility}/{len(answers)}",
        "sentiment": sentiment_summary,
        "competitors": sorted(list(competitors))
    }
    