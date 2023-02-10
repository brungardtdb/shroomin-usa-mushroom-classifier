import pandas as pd


# helper method to add mapping to dataframe
def add_mapping(mappings, value, value_name, mushroom_value):
    mappings.append((
        "{hvalue}_{mvalue}".format(hvalue=value_name, mvalue=value),
        int(value == mushroom_value)
    ))


# maps mushroom class to a pandas dataframe
# for predictions using a scikit-learn classifier
# pass in the x_test data
# this will allow us to make predictions about a single mushroom
def map_mushroom_to_dataframe(mushroom, df):
    mappings = []
    mushroom_dict = mushroom.to_dict()
    for category in df.items():
        segs = category[0].split("_")
        attribute = segs[0]
        value = segs[1]
        mushroom_value = mushroom_dict[attribute]
        add_mapping(mappings, value, attribute, mushroom_value)
    df_dict = {}
    for m in mappings:
        df_dict[m[0]] = m[1]
    return pd.DataFrame.from_records([df_dict])
