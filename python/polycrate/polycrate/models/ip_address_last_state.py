from typing import Literal

IPAddressLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IP_ADDRESS_LAST_STATE_VALUES: set[IPAddressLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_ip_address_last_state(value: str) -> IPAddressLastState:
    if value in IP_ADDRESS_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_LAST_STATE_VALUES!r}")
