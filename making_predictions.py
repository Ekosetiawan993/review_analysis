import joblib
from preprocessing_data import preprocessed_data

mlp_model_path = r'model_file/MLP_TF_Model.sav'
rfc_model_path = r'model_file/RANDOM_FOREST_TF_Model.sav'

mlp_model = joblib.load(mlp_model_path)
rfc_model = joblib.load(rfc_model_path)


def make_prediction(raw_text):
    processed_text = preprocessed_data(raw_text)

    mlp_prediction = mlp_model.predict([processed_text])
    rfc_prediction = rfc_model.predict([processed_text])

    return {'MLP prediction': mlp_prediction, 'RFC prediction': rfc_prediction}
