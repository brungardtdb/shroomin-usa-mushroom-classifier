import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from Mapper import mushroom_dataframe_mapper as mapper
from Enums.mushroom_characteristics import MushroomClass
from joblib import dump, load


# class to manage the task of classifying mushrooms as edible or poisonous
class MushroomClassifier:

    def __init__(self, df):
        # load pretrained model
        self.model = load('model.joblib')
        self.df = df
        # separate classification labels from other mushroom characteristics
        x = df.drop('class', axis=1)
        x = pd.get_dummies(x, drop_first=True)
        y = df['class']
        # separate training and test data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=100)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    # uses scikit-learn classifier to classify a given mushroom as edible or poisonous
    def classify_mushroom(self, mushroom):
        # map mushroom to dataframe
        mushroom_df = mapper.map_mushroom_to_dataframe(mushroom, self.x_test)
        # use classifier to determine if mushroom is edible or poisonous
        predictions = self.model.predict(mushroom_df)
        prediction = predictions[0]
        if prediction == str(MushroomClass.EDIBLE):
            return MushroomClass.EDIBLE
        else:
            return MushroomClass.POISONOUS


class ModelTrainer:

    def __init__(self, df, for_production):
        # separate classification labels from other mushroom characteristics
        self.x = df.drop('class', axis=1)
        self.x = pd.get_dummies(self.x, drop_first=True)
        self.y = df['class']
        # separate training and test data
        if for_production:
            x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.15, random_state=100)
        else:
            x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.15, random_state=None)
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        param_grid = {
            'n_estimators': [500],  # Gradient Boost is robust to over-fitting, large number usually means
            # better performance, the default is 100
            'learning_rate': [0.05],
            'max_depth': [None]  # expand nodes until all nodes are 'pure'
        }
        self.model = GradientBoostingClassifier()
        self.grid_search = GridSearchCV(self.model, param_grid)
        self.grid_search.fit(x_train, y_train)
        self.predictions = self.grid_search.predict(x_test)

    def print_classification_report(self):
        print(classification_report(self.y_test, self.predictions))

    def print_feature_importance(self):
        features = pd.DataFrame(index=self.x.columns,
                                data=self.grid_search.best_estimator_.feature_importances_,
                                columns=['Feature Importance'])
        features = features[features['Feature Importance'] > 0.009].sort_values('Feature Importance', ascending=False)
        print(features)

    def export_model_to_file(self):
        dump(self.grid_search, 'model.joblib')
