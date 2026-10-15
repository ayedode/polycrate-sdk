from typing import Literal

IPAddressState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IP_ADDRESS_STATE_VALUES: set[IPAddressState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_ip_address_state(value: str) -> IPAddressState:
    if value in IP_ADDRESS_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_STATE_VALUES!r}")
