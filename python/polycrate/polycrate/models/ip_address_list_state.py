from typing import Literal

IPAddressListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

IP_ADDRESS_LIST_STATE_VALUES: set[IPAddressListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_ip_address_list_state(value: str) -> IPAddressListState:
    if value in IP_ADDRESS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_ADDRESS_LIST_STATE_VALUES!r}")
