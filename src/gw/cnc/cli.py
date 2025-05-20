import sys
from decimal import Decimal
import yaml
import json

from gwerks.decorators import emitter
from gwerks.cli import cli, Clo

from gw.cnc.boxes import Box

"""
Box({"int_length": 9, "int_width": 6, "int_height": 1.5}).export_svg("box.svg")
"""


# --------------------------------------------------------------------------- #
# CLI entry point
# --------------------------------------------------------------------------- #
@emitter()
def cnc():

    _debug_traceback_limit = 1000
    sys.tracebacklimit = 0

    try:

        # command line arguments and default values
        clo = cli([
            {   # base args
                "make": Clo.REQUIRED,
                "spec": Clo.REQUIRED,
                "export_filepath": Clo.REQUIRED,
                "debug": None
            },
        ])

        debug = clo.get("debug") == "True"
        if debug:
            sys.tracebacklimit = _debug_traceback_limit

        make = clo.get("make")

        print(f"---------------------------------------------------------------------------------")

        globals()[f"make_{make}"](clo)

        print(f"---------------------------------------------------------------------------------")

    except Exception as e:
        msg = f"ERROR: {e}"
        print(msg)

    finally:
        pass


@emitter()
def make_box(clo: Clo):
    spec = json.loads(clo.get("spec"))
    export_filepath = clo.get("export_filepath")
    Box(spec).export_svg(export_filepath)
