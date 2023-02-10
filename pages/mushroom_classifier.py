import streamlit as st
import pandas as pd
from Enums import mushroom_characteristics as mc
from Models.mushroom import Mushroom
import DataCleaning.data_cleaner as dc
from Constants import strings as sc
from Classifier.mushroom_classifier import MushroomClassifier

# import and prepare data
df = pd.read_csv("mushrooms.csv")
df = dc.clean_data_set(df)
classifier = MushroomClassifier(df)

st.title("Use our Mushroom Classifier")
st.header("Tell us a little about the mushroom you found.")

odor_type = st.selectbox(sc.odor,
                         (
                             mc.Odor.NONE,
                             mc.Odor.SPICY,
                             mc.Odor.FOUL,
                             mc.Odor.PUNGENT,
                             mc.Odor.MUSTY,
                             mc.Odor.FISHY,
                             mc.Odor.CREOSOTE,
                             mc.Odor.ANISE,
                             mc.Odor.ALMOND
                         ))

stalk_root = st.selectbox(sc.stalk_root.replace("-", " "),
                          (
                              mc.StalkRoot.ROOTED,
                              mc.StalkRoot.CLUB,
                              mc.StalkRoot.EQUAL,
                              mc.StalkRoot.RHIZOMORPHS,
                              mc.StalkRoot.MISSING,
                              mc.StalkRoot.BULBOUS,
                              mc.StalkRoot.CUP
                          ))

bruises = st.selectbox(sc.bruises,
                       (
                           mc.Bruises.BRUISES,
                           mc.Bruises.NO
                       ))

stalk_surface_below = st.selectbox(sc.stalk_surface_below_ring.replace("-", " "),
                                   (
                                       mc.StalkSurface.SILKY,
                                       mc.StalkSurface.SCALY,
                                       mc.StalkSurface.SMOOTH,
                                       mc.StalkSurface.FIBROUS
                                   ))

spore_print_color = st.selectbox(sc.spore_print_color.replace("-", " "),
                                 (
                                     mc.SporePrintColor.BUFF,
                                     mc.SporePrintColor.WHITE,
                                     mc.SporePrintColor.GREEN,
                                     mc.SporePrintColor.YELLOW,
                                     mc.SporePrintColor.PURPLE,
                                     mc.SporePrintColor.ORANGE,
                                     mc.SporePrintColor.CHOCOLATE,
                                     mc.SporePrintColor.BROWN,
                                     mc.SporePrintColor.BLACK
                                 ))

ring_type = st.selectbox(sc.ring_type.replace("-", " "),
                         (
                             mc.RingType.NONE,
                             mc.RingType.PENDANT,
                             mc.RingType.ZONE,
                             mc.RingType.SHEATHING,
                             mc.RingType.LARGE,
                             mc.RingType.FLARING,
                             mc.RingType.EVANESCENT,
                             mc.RingType.COBWEBBY
                         ))

gill_spacing = st.selectbox(sc.gill_spacing.replace("-", " "),
                            (
                                mc.GillSpacing.CLOSE,
                                mc.GillSpacing.DISTANT,
                                mc.GillSpacing.CROWDED
                            ))

if st.button("classify mushroom"):
    m = Mushroom()
    m.set_odor(odor_type)
    m.set_stalk_root(stalk_root)
    m.set_bruises(bruises)
    m.set_stalk_surface_below_ring(stalk_surface_below)
    m.set_spore_print_color(spore_print_color)
    m.set_ring_type(ring_type)
    m.set_gill_spacing(gill_spacing)
    classification = classifier.classify_mushroom(m)
    message = "Your mushroom is most likely " + str(classification)
    st.write(message)

st.write("")
st.write("")
st.text("********************* Warning and Disclaimer **********************")
st.text("If you are not sure if a mushroom is poisonous, do not eat it unless")
st.text("a qualified expert has told you that it is safe. Shroomin' USA will not")
st.text("be held liable for any harm that results from consuming poisonous mushrooms.")
st.text("*******************************************************************")
