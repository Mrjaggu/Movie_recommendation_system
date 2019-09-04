# Movie_recommendation_system
Movie recommendation system using NLP technique and deploying on flask
# In this we have demonstrated Content based recommendation system by using NLP technique
# Package required 
1. Sk-learn
2. Pandas
3. Spacy
4. nltk
5. gensim

## First we used overview for content based recommendation system
### Countvectorizer
1. By using word 2 vec featurization technique like Bag of words we implemented it.
2. Here we used linear kernel which is fast and I also tried with pairwise cosine distance but the result was not that much satisfactory

### Tfidfvectorizer
1. We used tfidf vectorizer which gave good result as we know tfidf ignore the words which are more repeated it give importance to rare words.
2. Result was good as compared to countvectorizer

### Word2vec
1.We used word2vec which text semantic based featurization and the result was not that much good
