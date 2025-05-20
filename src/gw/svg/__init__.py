

class E:
    def __init__(self, tag):
        self._tag = tag
        self._attr: list[tuple[str, ...]] = []
        self._cont: list[E] = []

    def __repr__(self):
        s = ""
        s += f"<{self._tag}"
        for attr in self._attr:
            s += f" {attr[0]}=\"{attr[1]}\""
        s += f">"
        for child in self._cont:
            s += str(child)
        s += f"</{self._tag}>"
        return s

    def attr(self, key: str, value):
        self._attr.append((key, str(value)))
        return self

    def add(self, content: ["E", list["E"]]):
        if isinstance(content, list):
            self._cont.extend(content)
        else:
            self._cont.append(content)
        return self


class SVG(E):
    def __init__(self):
        super().__init__("svg")
        self.attr("xmlns", "http://www.w3.org/2000/svg")

    def defs(self):
        e = Defs()
        self.add(e)
        return e


class Style(E):
    def __init__(self):
        super().__init__("style")

    def __repr__(self):
        s = ""
        s += f"<{self._tag}>"
        s += "<![CDATA["
        for child in self._cont:
            s += str(child)
        s += f"]]>"
        s += f"</{self._tag}>"
        return s


class Defs(E):
    def __init__(self):
        super().__init__("defs")

    def style(self):
        e = Style()
        self.add(e)
        return e
