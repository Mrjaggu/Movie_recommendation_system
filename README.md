# Movie_recommendation_system
Movie recommendation system using NLP technique and deploying on flask
# In this we have demonstrated Content based recommendation system by using NLP technique
# Package required 
1. Sk-learn
2. Pandas
3. Spacy
4. nltk
5. gensim

### Here we have used less data due to computation you can try with more data.
## First we used overview for content based recommendation system
### Countvectorizer
1. By using word 2 vec featurization technique like Bag of words we implemented it.
2. Here we used linear kernel which is fast and I also tried with pairwise cosine distance but the result was not that much satisfactory

### Tfidfvectorizer
1. We used tfidf vectorizer which gave good result as we know tfidf ignore the words which are more repeated it give importance to rare words.
2. Result was good as compared to countvectorizer

### Word2vec
1.We used word2vec which is text semantic based featurization and the result was not that much good as compared to tfidf featuirzation
2. We didn't used google glove vectors since it contains lots of data which was not relevant to our dataset problem

### To improve our recommendation we used overview + title + genres as our features for recommendation
1. Result was better for tfidf featurization

### Tried topic modeling features 
1. By using spacy , lda model for topic modeling where I used number of topic=20 which is hyperparameter you can go with less if you just want to know what features is it comprises of and we can go with more if we want features from corpus
2. Result was same 


### Used flask to deploy our model
