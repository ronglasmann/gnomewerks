import yaml
from decimal import Decimal, ROUND_HALF_DOWN


UNITS_INCHES = "in"
UNITS_MM = "mm"
MM_PER_IN = Decimal(25.4)
REQ = "~+required+~"

# defaults
DEF_UNITS = UNITS_INCHES
DEF_DPI = 96
DEF_GUTTER = 0.25
DEF_ROUNDING_SPEC = '1.'
DEF_ROUNDING = ROUND_HALF_DOWN


class CncParams:
    def __init__(self, params_dict: dict):
        super().__init__()
        self.params = params_dict

    def get(self, __key: str, default: str) -> str:
        val = self.params.get(__key, default)
        # print(f"get({__key}, {default}): {val}")
        if val == REQ:
            raise Exception(f"'{__key}' is a required parameter")
        return val

    # def keys(self):
    #     return self.params.keys()


class CncObject:
    def __init__(self, params: dict):
        self._params = CncParams(params)
        self._units = self.get_s("units", DEF_UNITS)
        self._dpi = self.get_n("dpi", DEF_DPI)
        self._rounding_spec = self.get_s("rounding_spec", DEF_ROUNDING_SPEC)
        self._rounding = self.get_s("rounding", DEF_ROUNDING)

    def calc(self, expr):
        return self._q(expr)

    def get_n_px(self, key: str, default: float = REQ) -> Decimal:
        return self._px(self.get_n(key, default))

    def get_n_q(self, key: str, default: float = REQ) -> Decimal:
        return self._q(self.get_n(key, default))

    def get_n(self, key: str, default: float = REQ) -> Decimal:
        return Decimal(self.get_s(key, str(default)))

    def get_s(self, key: str, default: str = REQ) -> str:
        return self._params.get(key, default)

    @staticmethod
    def from_yaml(filepath):
        with open(filepath, 'r') as f:
            return CncObject(yaml.safe_load(f))

    def export_yaml(self, filepath):
        with open(filepath, 'w') as f:
            yaml.dump(self._params, f, sort_keys=False)

    def export_svg(self, filepath):
        svg_str = str(self._make())
        with open(filepath, 'w') as f:
            f.write(svg_str)

    def _make(self) -> str:
        raise Exception("not implemented")

    def _px(self, measurement_in_or_mm):
        measurement = measurement_in_or_mm
        if self._units == UNITS_MM:
            measurement = measurement_in_or_mm / MM_PER_IN
        return self._q(measurement * self._dpi)

    def _q(self, number):
        return Decimal(number).quantize(Decimal(self._rounding_spec), rounding=self._rounding)
