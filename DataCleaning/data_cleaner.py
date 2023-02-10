from DataCleaning import data_mapping as dm
from Constants import strings as sc


# transform data from dataset into human readable values
def clean_data_set(df):
    df[sc.m_class] = df[sc.m_class].map(dm.classes)
    df[sc.cap_shape] = df[sc.cap_shape].map(dm.cap_shapes)
    df[sc.cap_surface] = df[sc.cap_surface].map(dm.cap_surfaces)
    df[sc.cap_color] = df[sc.cap_color].map(dm.cap_colors)
    df[sc.bruises] = df[sc.bruises].map(dm.bruises)
    df[sc.odor] = df[sc.odor].map(dm.odors)
    df[sc.gill_attachment] = df[sc.gill_attachment].map(dm.gill_attachments)
    df[sc.gill_spacing] = df[sc.gill_spacing].map(dm.gill_spacings)
    df[sc.gill_size] = df[sc.gill_size].map(dm.gill_sizes)
    df[sc.gill_color] = df[sc.gill_color].map(dm.gill_colors)
    df[sc.stalk_shape] = df[sc.stalk_shape].map(dm.stalk_shapes)
    df[sc.stalk_root] = df[sc.stalk_root].map(dm.stalk_roots)
    df[sc.stalk_surface_above_ring] = df[sc.stalk_surface_above_ring].map(dm.stalk_surfaces_above)
    df[sc.stalk_surface_below_ring] = df[sc.stalk_surface_below_ring].map(dm.stalk_surfaces_below)
    df[sc.stalk_color_above_ring] = df[sc.stalk_color_above_ring].map(dm.stalk_colors_above)
    df[sc.stalk_color_below_ring] = df[sc.stalk_color_below_ring].map(dm.stalk_colors_below)
    df[sc.veil_type] = df[sc.veil_type].map(dm.veil_types)
    df[sc.veil_color] = df[sc.veil_color].map(dm.veil_colors)
    df[sc.ring_number] = df[sc.ring_number].map(dm.ring_numbers)
    df[sc.ring_type] = df[sc.ring_type].map(dm.ring_types)
    df[sc.spore_print_color] = df[sc.spore_print_color].map(dm.spore_print_colors)
    df[sc.population] = df[sc.population].map(dm.populations)
    df[sc.habitat] = df[sc.habitat].map(dm.habitats)
    return df
