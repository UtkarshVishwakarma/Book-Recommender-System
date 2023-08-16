import pickle
import pandas as pd
import numpy as np
import sklearn

books = pickle.load(open('models/books.pkl', 'rb'))
pt = pickle.load(open('models/pt.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

books = pd.DataFrame(books)
pt = pd.DataFrame(pt)

def recommend(book):
    book_index = np.where(pt.index == book)[0][0]
    recommended_books = sorted(list(enumerate(similarity[book_index])), reverse=True, key=lambda x:x[1])[1:6]
    data = []
    for i in recommended_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))        
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)) 
        
        data.append(item)
        
    return data