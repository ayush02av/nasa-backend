import pickle
from utility import generate_dataset, resources

def gots_predict(attributes):
    dataset = generate_dataset.generate_dataset(attributes)

    with open(resources.GOTS_PREDICT_MODEL, 'rb') as file:
        print(file)
        model = pickle.load(file)
        print(model)
    # model = pickle.load(open(resources.GOTS_PREDICT_MODEL, 'rb'))

    prediction = model.predict((dataset))

    return prediction