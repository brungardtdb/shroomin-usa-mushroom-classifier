import streamlit as st  # Run -> Edit Configurations -> Interpreter options: -> -m streamlit run
from PIL import Image

# for model training and export
import pandas as pd
from Classifier.mushroom_classifier import ModelTrainer
import DataCleaning.data_cleaner as dc


def train_model():
    # import and prepare data
    df = pd.read_csv("mushrooms.csv")
    df = dc.clean_data_set(df)

    trainer = ModelTrainer(df, True)
    trainer.print_classification_report()
    trainer.print_feature_importance()
    trainer.export_model_to_file()


if __name__ == '__main__':

    st.title("Welcome to Shroomin' USA!")
    image = Image.open("mushroom.jpg")
    st.image(image=image, caption="Image was taken from https://www.kaggle.com/datasets/uciml/mushroom-classification")
    # train_model()
