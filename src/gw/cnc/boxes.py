from gw.svg import *
from gw.css import *
from gw.cnc import *

# defaults
DEF_STROKE_COLOR = "black"
DEF_STROKE_WIDTH = 1
DEF_FILL = "transparent"
DEF_GUTTER = 0.25
DEF_THICK = 0.25
DEF_CUTTER = 0.125


class Box(CncObject):
    def __init__(self, params: dict):
        super().__init__(params)

        # params converted to pixel values
        self.gutter = self.get_n_px("gutter", DEF_GUTTER)
        self.mat_thickness = self.get_n_px("mat_thickness", DEF_THICK)
        self.int_length = self.get_n_px("int_length")
        self.int_height = self.get_n_px("int_height")
        self.int_width = self.get_n_px("int_width")

        # calcs
        self.ext_length = self.calc(self.int_length + (self.mat_thickness * 2))
        self.ext_height = self.calc(self.int_height + (self.mat_thickness * 2))
        self.ext_width = self.calc(self.int_width + (self.mat_thickness * 2))

    def _make(self):

        # elements = []
        # elements.extend(self._make_back())

        canvas_width = self.calc(self.gutter + self.ext_height + self.gutter + self.ext_length + self.gutter +
                                 self.ext_height + self.gutter)
        canvas_height = self.calc(self.gutter + self.ext_height + self.gutter + self.ext_width + self.gutter +
                                  self.ext_height + self.gutter)

        print(f"canvas_width: {canvas_width}")
        print(f"canvas_height: {canvas_height}")
        # print(f"elements: {elements}")

        # canvas = svg.SVG(
        #     # overall canvas
        #     width=canvas_width,
        #     height=canvas_height,
        #     elements=elements
        # )

        #         stroke=DEF_STROKE_COLOR,
        #         stroke_width=DEF_STROKE_WIDTH,
        #         fill=DEF_FILL,

        canvas = SVG().attr("width", canvas_width).attr("height", canvas_height)
        canvas.defs().style().add([
            S(".layer_1", [("stroke", "black"), ("stroke_width", 1), ("fill", "black"), ("fill-opacity", 0.5)]),
            S(".layer_2", [("stroke", "black"), ("stroke_width", 1), ("fill", "blue"), ("fill-opacity", 0.5)])
        ])
        canvas.add(self._make_back())

        return canvas

    # svg.Rect(
    #     x=60, y=10,
    #     rx=10, ry=10,
    #     width=30, height=30,
    #     stroke="black",
    #     fill="transparent",
    #     stroke_width=5,
    # ),
    # svg.Circle(
    #     cx=25, cy=75, r=20,
    #     stroke="red",
    #     fill="transparent",
    #     stroke_width=5,
    # ),
    # svg.Ellipse(
    #     cx=75, cy=75,
    #     rx=20, ry=5,
    #     stroke="red",
    #     fill="transparent",
    #     stroke_width=5,
    # ),
    # svg.Line(
    #     x1=10, x2=50,
    #     y1=110, y2=150,
    #     stroke="orange",
    #     stroke_width=5,
    # ),
    # svg.Polyline(
    #     points=[
    #         60, 110, 65, 120, 70, 115, 75, 130, 80,
    #         125, 85, 140, 90, 135, 95, 150, 100, 145,
    #     ],
    #     stroke="orange",
    #     fill="transparent",
    #     stroke_width=5,
    # ),
    # svg.Polygon(
    #     points=[
    #         50, 160, 55, 180, 70, 180, 60, 190, 65, 205,
    #         50, 195, 35, 205, 40, 190, 30, 180, 45, 180,
    #     ],
    #     stroke="green",
    #     fill="transparent",
    #     stroke_width=5,
    # ),
    # svg.Path(
    #     d=[
    #         svg.M(20, 230),
    #         svg.Q(40, 205, 50, 230),
    #         svg.T(90, 230),
    #     ],
    #     fill="none",
    #     stroke="blue",
    #     stroke_width=5,
    # ),

    def _make_back(self):
        return [
            _svg_rect(self.ext_length, self.ext_height, css_class=".layer_1"),
            _svg_rect(self.calc(self.ext_length - (self.mat_thickness * Decimal(0.2))), self.calc(self.mat_thickness / 2), css_class=".layer_2")
        ]


        # origin_x = origin_y = self.calc(self.gutter + self.ext_height + self.gutter)
        #
        # return [
        #     _svg_rect(self.ext_length, self.ext_height),
        #     svg.Rect(
        #         x=origin_x, y=origin_y,
        #         width=, height=,
        #         stroke=DEF_STROKE_COLOR,
        #         stroke_width=DEF_STROKE_WIDTH,
        #         fill=DEF_FILL,
        #     ),
        #     svg.Rect(
        #         x=origin_x, y=self.calc(origin_y + (self.mat_thickness / 2)),
        #         width=,
        #         height=,
        #         stroke=DEF_STROKE_COLOR,
        #         stroke_width=DEF_STROKE_WIDTH,
        #         fill="blue",
        #     )
        # ]


def _svg_rect(width, height, css_class=None, css_id=None) -> E:
    rect = E("rect")
    rect.attr("width", width)
    rect.attr("height", height)
    if css_id:
        rect.attr("id", css_id)
    if css_class:
        rect.attr("css_class", css_class)

    return rect
    # return svg.Rect(
    #         x=0, y=0,
    #         width=width, height=height,
    #         stroke=stroke_color,
    #         stroke_width=stroke_width_px,
    #         fill=fill_color,
    #     )
