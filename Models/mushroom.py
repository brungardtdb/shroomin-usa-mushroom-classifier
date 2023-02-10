from Constants import strings as sc


# model class for mushrooms
class Mushroom:

    def __init__(self):
        # default mushroom attributes to most common found in data set
        # user will only be able to change 7 most impactful characteristics
        self.classification = "edible"
        self.cap_shape = "convex"
        self.cap_surface = "scaly"
        self.cap_color = "brown"
        self.bruises = "no"
        self.odor = "none"
        self.gill_attachment = "free"
        self.gill_spacing = "close"
        self.gill_size = "broad"
        self.gill_color = "buff"
        self.stalk_shape = "tapering"
        self.stalk_root = "bulbous"
        self.stalk_surface_above_ring = "smooth"
        self.stalk_surface_below_ring = "smooth"
        self.stalk_color_above_ring = "white"
        self.stalk_color_below_ring = "white"
        self.veil_type = "partial"
        self.veil_color = "white"
        self.ring_number = "one"
        self.ring_type = "pedant"
        self.spore_print_color = "white"
        self.population = "several"
        self.habitat = "woods"

    # transforms mushroom class into a dictionary
    def to_dict(self):
        return {
            sc.m_class: self.classification,
            sc.cap_shape: self.cap_shape,
            sc.cap_surface: self.cap_surface,
            sc.cap_color: self.cap_color,
            sc.bruises: self.bruises,
            sc.odor: self.odor,
            sc.gill_attachment: self.gill_attachment,
            sc.gill_spacing: self.gill_spacing,
            sc.gill_size: self.gill_size,
            sc.gill_color: self.gill_color,
            sc.stalk_shape: self.stalk_shape,
            sc.stalk_root: self.stalk_root,
            sc.stalk_surface_above_ring: self.stalk_surface_above_ring,
            sc.stalk_surface_below_ring: self.stalk_surface_below_ring,
            sc.stalk_color_above_ring: self.stalk_color_above_ring,
            sc.stalk_color_below_ring: self.stalk_color_below_ring,
            sc.veil_type: self.veil_type,
            sc.veil_color: self.veil_color,
            sc.ring_number: self.ring_number,
            sc.ring_type: self.ring_type,
            sc.spore_print_color: self.spore_print_color,
            sc.population: self.population,
            sc.habitat: self.habitat
        }

    # assigns odor for mushroom
    # takes in an enum and assigns corresponding string
    def set_odor(self, odor):
        self.odor = str(odor)

    # assigns stalk root for mushroom
    # takes in an enum and assigns corresponding string
    def set_stalk_root(self, stalk_root):
        self.stalk_root = str(stalk_root)

    # assigns bruises for mushroom
    # takes in an enum and assigns corresponding string
    def set_bruises(self, bruises):
        self.bruises = str(bruises)

    # assigns stalk surface below ring for mushroom
    # takes in an enum and assigns corresponding string
    def set_stalk_surface_below_ring(self, stalk_surface):
        self.stalk_surface_below_ring = str(stalk_surface)

    # assigns spore print color for mushroom
    # takes in an enum and assigns corresponding string
    def set_spore_print_color(self, spore_print_color):
        self.spore_print_color = str(spore_print_color)

    # assigns ring type for mushroom
    # takes in an enum and assigns corresponding string
    def set_ring_type(self, ring_type):
        self.ring_type = str(ring_type)

    # assigns gill spacing for mushroom
    # takes in an enum and assigns corresponding string
    def set_gill_spacing(self, gill_spacing):
        self.gill_spacing = str(gill_spacing)
