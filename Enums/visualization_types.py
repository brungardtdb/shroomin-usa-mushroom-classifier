from enum import Enum


# enum to manage type of visualization we will render
class VisualizationType(Enum):
    COUNT_PLOT = 0,
    HEATMAP = 1,
    PIE_CHART = 3

    def __str__(self):
        if self.value == self.COUNT_PLOT.value:
            return "count plot"
        if self.value == self.HEATMAP.value:
            return "heatmap"
        if self.value == self.PIE_CHART.value:
            return "pie chart"
