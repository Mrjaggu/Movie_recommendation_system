from flask import Flask,jsonify,request,render_template
import pickle
import pandas as pd
import numpy as np
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
import sys
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime as dt
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")


app = Flask(__name__)

df = pd.read_csv('./processed.csv')
indextitle = pd.read_csv('./indextitle.csv')
similarity = np.load('./similarity.npy')
overview_bow = joblib.load('./overview_bow.pkl')



def bag_of_words(title):
    id = indextitle[title]
    # print("movie id",id)
    similarity_score = list(enumerate(similarity[id]))
    print(" similarity score done")
    #pair_distance = pairwise_distances(overview_bow,overview_bow[id])
    indices = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    indices = indices[1:10]

    movie_indices = [i[0] for i in indices]
#     print(movie_indices)
    df_indices = list(df.index[movie_indices])
    print("Similar movie of {} are: \n".format(df["title"].loc[id]))
    final_result=[]
    for i in range(0,len(indices)):
        final_result.append(str(df['title'].loc[df_indices[i]]))
        # print("{}".format(df['title'].loc[df_indices[i]]))
    print(final_result[0])
    return  final_result

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    input = request.form.to_dict()
    print("step 1",input)
    input = list(input.values())
    print("Step 2",input)
    res = bag_of_words(input[0])
    return render_template('index2.html',user=res)

if __name__=='__main__':
    app.run(debug=True)
