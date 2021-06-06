from yake import KeywordExtractor

def Create_Blank(text, blankNum):
    wantedNumber = int(blankNum)
    kw_extractor = KeywordExtractor(lan="en", n=1, top=wantedNumber)
    keywords = kw_extractor.extract_keywords(text=text)
    keywords = [x for x, y in keywords]

    print(keywords)
    for i in keywords:
        text = text.replace(i, "__________")
    return text
