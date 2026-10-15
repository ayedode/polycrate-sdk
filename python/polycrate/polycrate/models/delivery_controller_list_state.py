from typing import Literal

DeliveryControllerListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DELIVERY_CONTROLLER_LIST_STATE_VALUES: set[DeliveryControllerListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_delivery_controller_list_state(value: str) -> DeliveryControllerListState:
    if value in DELIVERY_CONTROLLER_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_LIST_STATE_VALUES!r}")
