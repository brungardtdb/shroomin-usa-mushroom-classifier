from enum import Enum
from Constants import strings as sc
# these enums will be used to manage the 7 characteristics a user is allowed to select
# as well as the mushroom classification


class MushroomClass(Enum):
    EDIBLE = 0,
    POISONOUS = 1,

    def __str__(self):
        if self.value == self.EDIBLE.value:
            return "edible"
        if self.value == self.POISONOUS.value:
            return "poisonous"


class Bruises(Enum):
    BRUISES = 1,
    NO = 2

    def __str__(self):
        if self.value == self.BRUISES.value:
            return "bruises"
        if self.value == self.NO.value:
            return "no"


class GillSpacing(Enum):
    CLOSE = 1,
    CROWDED = 2,
    DISTANT = 3

    def __str__(self):
        if self.value == self.CLOSE.value:
            return "close"
        if self.value == self.CROWDED.value:
            return "crowded"
        if self.value == self.DISTANT.value:
            return "distant"


class Odor(Enum):
    ALMOND = 1,
    ANISE = 2,
    CREOSOTE = 3,
    FISHY = 4,
    FOUL = 5,
    MUSTY = 6,
    NONE = 7,
    PUNGENT = 8,
    SPICY = 9

    def __str__(self):
        if self.value == self.ALMOND.value:
            return "almond"
        if self.value == self.ANISE.value:
            return "anise"
        if self.value == self.CREOSOTE.value:
            return "creosote"
        if self.value == self.FISHY.value:
            return "fishy"
        if self.value == self.FOUL.value:
            return "foul"
        if self.value == self.MUSTY.value:
            return "musty"
        if self.value == self.NONE.value:
            return "none"
        if self.value == self.PUNGENT.value:
            return "pungent"
        if self.value == self.SPICY.value:
            return "spicy"


class RingType(Enum):
    COBWEBBY = 1,
    EVANESCENT = 2,
    FLARING = 3,
    LARGE = 4,
    NONE = 5,
    PENDANT = 6,
    SHEATHING = 7,
    ZONE = 8

    def __str__(self):
        if self.value == self.COBWEBBY.value:
            return "cobwebby"
        if self.value == self.EVANESCENT.value:
            return "evanescent"
        if self.value == self.FLARING.value:
            return "flaring"
        if self.value == self.LARGE.value:
            return "large"
        if self.value == self.NONE.value:
            return "none"
        if self.value == self.PENDANT.value:
            return "pendant"
        if self.value == self.SHEATHING.value:
            return "sheathing"
        if self.value == self.ZONE.value:
            return "zone"


class SporePrintColor(Enum):
    BLACK = 1,
    BROWN = 2,
    BUFF = 3,
    CHOCOLATE = 4,
    GREEN = 5,
    ORANGE = 6,
    PURPLE = 7,
    WHITE = 8,
    YELLOW = 9

    def __str__(self):
        if self.value == self.BLACK.value:
            return "black"
        if self.value == self.BROWN.value:
            return "brown"
        if self.value == self.BUFF.value:
            return "buff"
        if self.value == self.CHOCOLATE.value:
            return "chocolate"
        if self.value == self.GREEN.value:
            return "green"
        if self.value == self.ORANGE.value:
            return "orange"
        if self.value == self.PURPLE.value:
            return "purple"
        if self.value == self.WHITE.value:
            return "white"
        if self.value == self.YELLOW.value:
            return "yellow"


class StalkRoot(Enum):
    BULBOUS = 1,
    CLUB = 2,
    CUP = 3,
    EQUAL = 4,
    RHIZOMORPHS = 5,
    ROOTED = 6,
    MISSING = 7

    def __str__(self):
        if self.value == self.BULBOUS.value:
            return "bulbous"
        if self.value == self.CLUB.value:
            return "club"
        if self.value == self.CUP.value:
            return "cup"
        if self.value == self.EQUAL.value:
            return "equal"
        if self.value == self.RHIZOMORPHS.value:
            return "rhizomorphs"
        if self.value == self.ROOTED.value:
            return "rooted"
        if self.value == self.MISSING.value:
            return "missing"


class StalkSurface(Enum):
    FIBROUS = 1,
    SCALY = 2,
    SILKY = 3,
    SMOOTH = 4

    def __str__(self):
        if self.value == self.FIBROUS.value:
            return "fibrous"
        if self.value == self.SCALY.value:
            return "scaly"
        if self.value == self.SILKY.value:
            return "silky"
        if self.value == self.SMOOTH.value:
            return "smooth"


class Attribute(Enum):
    CLASS = 1,
    CAP_SHAPE = 2,
    CAP_SURFACE = 3,
    CAP_COLOR = 4,
    BRUISES = 5,
    ODOR = 6,
    GILL_ATTACHMENT = 7,
    GILL_SPACING = 8,
    GILL_SIZE = 9,
    GILL_COLOR = 10,
    STALK_SHAPE = 11,
    STALK_ROOT = 12,
    STALK_SURFACE_ABOVE_RING = 13,
    STALK_SURFACE_BELOW_RING = 14,
    STALK_COLOR_ABOVE_RING = 15,
    STALK_COLOR_BELOW_RING = 16,
    VEIL_TYPE = 17,
    VEIL_COLOR = 18,
    RING_NUMBER = 19,
    RING_TYPE = 20,
    SPORE_PRINT_COLOR = 21,
    POPULATION = 22,
    HABITAT = 23

    def __str__(self):
        if self.value == self.CLASS.value:
            return sc.m_class.replace("-", " ")
        if self.value == self.CAP_SHAPE.value:
            return sc.cap_shape.replace("-", " ")
        if self.value == self.CAP_SURFACE.value:
            return sc.cap_surface.replace("-", " ")
        if self.value == self.CAP_COLOR.value:
            return sc.cap_color.replace("-", " ")
        if self.value == self.BRUISES.value:
            return sc.bruises.replace("-", " ")
        if self.value == self.ODOR.value:
            return sc.odor.replace("-", " ")
        if self.value == self.GILL_ATTACHMENT.value:
            return sc.gill_attachment.replace("-", " ")
        if self.value == self.GILL_SPACING.value:
            return sc.gill_spacing.replace("-", " ")
        if self.value == self.GILL_SIZE.value:
            return sc.gill_size.replace("-", " ")
        if self.value == self.GILL_COLOR.value:
            return sc.gill_color.replace("-", " ")
        if self.value == self.STALK_SHAPE.value:
            return sc.stalk_shape.replace("-", " ")
        if self.value == self.STALK_ROOT.value:
            return sc.stalk_root.replace("-", " ")
        if self.value == self.STALK_SURFACE_ABOVE_RING.value:
            return sc.stalk_surface_above_ring.replace("-", " ")
        if self.value == self.STALK_SURFACE_BELOW_RING.value:
            return sc.stalk_surface_below_ring.replace("-", " ")
        if self.value == self.STALK_COLOR_ABOVE_RING.value:
            return sc.stalk_color_above_ring.replace("-", " ")
        if self.value == self.STALK_COLOR_BELOW_RING.value:
            return sc.stalk_color_below_ring.replace("-", " ")
        if self.value == self.VEIL_TYPE.value:
            return sc.veil_type.replace("-", " ")
        if self.value == self.VEIL_COLOR.value:
            return sc.veil_color.replace("-", " ")
        if self.value == self.RING_NUMBER.value:
            return sc.ring_number.replace("-", " ")
        if self.value == self.RING_TYPE.value:
            return sc.ring_type.replace("-", " ")
        if self.value == self.SPORE_PRINT_COLOR.value:
            return sc.spore_print_color.replace("-", " ")
        if self.value == self.POPULATION.value:
            return sc.population.replace("-", " ")
        if self.value == self.HABITAT.value:
            return sc.habitat.replace("-", " ")
