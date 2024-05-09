import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def wordCloud(doc):
    #In the future, I'd like to have this include multiple documents but those api requests take too long to be practical
    #as of now
    localDoc = doc
    localDoc.replace("and", "")
    localDoc.replace("of", "")
    localDoc.replace("the", "")
    localDoc.replace("its", "")
    localDoc.replace("to", "")
    localDoc.replace("which", "")

    documents = [
        localDoc
    ]
    print("In visualizer")
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Summing up the IDF scores for each term across documents
    tfidf_sum = np.sum(tfidf_matrix.toarray(), axis=0)
    word_strengths = dict(zip(vectorizer.get_feature_names_out(), tfidf_sum))

    # Generating the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_strengths)
    print("Close to plt")
    # Display the generated image:
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("./figure.png")
