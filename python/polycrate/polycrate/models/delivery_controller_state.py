from typing import Literal

DeliveryControllerState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DELIVERY_CONTROLLER_STATE_VALUES: set[DeliveryControllerState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_delivery_controller_state(value: str) -> DeliveryControllerState:
    if value in DELIVERY_CONTROLLER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_STATE_VALUES!r}")
