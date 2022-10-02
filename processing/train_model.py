from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd

def train_model(data_csv):
    df = pd.read_csv(f'../assets/{data_csv}.csv')

    X = df.drop(columns=['biomass'])
    y = df['biomass'].astype('int')

    model = DecisionTreeClassifier()
    model.fit(X.values, y)

    print(model)

    print(model.predict([[24.76,37.23,26,0.236]]))

    model_file = f'../models/{data_csv}.pkl'
    pickle.dump(model, open(model_file, 'wb'))

    return model

def predict_from_model(data_model, data):
    print(data_model)
    print(pickle.load(open(data_model, 'rb')))
    # return model.predict(data)

data_gots_model = train_model('data_gots')

# print(predict_from_model(data_gots_model, [24.76,37.23,26,0.236]))