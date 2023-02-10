import streamlit as st
import pandas as pd
from Enums import visualization_types as vt
from Enums import mushroom_characteristics as mc
import DataCleaning.data_cleaner as dc
import Visualizations.data_visualizer as dv

# import and prepare data
df = pd.read_csv("mushrooms.csv")
df = dc.clean_data_set(df)
visualizer = dv.DataVisualizer(df)

st.title("Explore our Data Set")

visualization_type = st.selectbox("What type of visualization do you prefer?",
                                  (
                                    vt.VisualizationType.COUNT_PLOT,
                                    vt.VisualizationType.HEATMAP,
                                    vt.VisualizationType.PIE_CHART
                                  ))

mushroom_characteristic = st.selectbox("What mushroom characteristic are you interested in?",
                                       (
                                        mc.Attribute.CLASS,
                                        mc.Attribute.CAP_SHAPE,
                                        mc.Attribute.CAP_SURFACE,
                                        mc.Attribute.CAP_COLOR,
                                        mc.Attribute.BRUISES,
                                        mc.Attribute.ODOR,
                                        mc.Attribute.GILL_ATTACHMENT,
                                        mc.Attribute.GILL_SPACING,
                                        mc.Attribute.GILL_SIZE,
                                        mc.Attribute.GILL_COLOR,
                                        mc.Attribute.STALK_SHAPE,
                                        mc.Attribute.STALK_ROOT,
                                        mc.Attribute.STALK_SURFACE_ABOVE_RING,
                                        mc.Attribute.STALK_SURFACE_BELOW_RING,
                                        mc.Attribute.STALK_COLOR_ABOVE_RING,
                                        mc.Attribute.STALK_COLOR_BELOW_RING,
                                        mc.Attribute.VEIL_TYPE,
                                        mc.Attribute.VEIL_COLOR,
                                        mc.Attribute.RING_NUMBER,
                                        mc.Attribute.RING_TYPE,
                                        mc.Attribute.SPORE_PRINT_COLOR,
                                        mc.Attribute.POPULATION,
                                        mc.Attribute.HABITAT
                                        ))

if st.button("display visualization"):
    if visualization_type == vt.VisualizationType.COUNT_PLOT:
        vis = visualizer.get_count_plot(str(mushroom_characteristic).replace(" ", "-"))
        st.pyplot(vis)
    if visualization_type == vt.VisualizationType.HEATMAP:
        vis = visualizer.get_heatmap(str(mushroom_characteristic).replace(" ", "-"))
        st.pyplot(vis)
    if visualization_type == vt.VisualizationType.PIE_CHART:
        vis = visualizer.get_pie_chart(str(mushroom_characteristic).replace(" ", "-"))
        st.pyplot(vis)
