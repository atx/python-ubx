from ..payload import *
from ..message import *

payload_description = Fields(
    ("mask", X2),
    ("dynModel", U1),
    ("fixMode", U1),
    ("fixedAlt", I4),
    ("fixedAltVar", U4),
    ("minElev", I1),
    ("drLimit", U1),
    ("pDop", U2),
    ("tDob", U2),
    ("pAcc", U2),
    ("tAcc", U2),
    ("staticHoldThreshold", U1),
    ("dgpsTimeOut", U1),
    ("reserved2", U4),
    ("reserved3", U4),
    ("reserved4", U4)
)

description = MessageDescription(
    name="CFG_NAV5",
    message_class=b"\x06",
    message_id=b"\x24",
    payload_description=Options(
        Empty,
        payload_description,
    )
)
