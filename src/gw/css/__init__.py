from typing import Any


class S:
    def __init__(self, selector: str = None, attributes: list[tuple[str, Any]] = None):
        self._sel = selector
        self._attr: list[tuple[str, Any]] = attributes
        if self._attr is None:
            self._attr = []

    def __repr__(self):
        s = ""
        if self._sel:
            s += f"{self._sel} {{"
        for attr in self._attr:
            s += f" {attr[0]}: {str(attr[1])}; "
        if self._sel:
            s += f"}}"
        return s

    def attr(self, key: str, value):
        self._attr.append((key, value))
        return self


# class CSS:
#     def __init__(self):
#         super().__init__()
#         self._styles: list[S] = []
#
#     def __repr__(self):
#         s = ""
#         for style in self._styles:
#             s += style
#         return s
#
#     def add(self, style: S):
#         self._styles.append(style)
