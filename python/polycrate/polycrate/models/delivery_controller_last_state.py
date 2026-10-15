from typing import Literal

DeliveryControllerLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DELIVERY_CONTROLLER_LAST_STATE_VALUES: set[DeliveryControllerLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_delivery_controller_last_state(value: str) -> DeliveryControllerLastState:
    if value in DELIVERY_CONTROLLER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_LAST_STATE_VALUES!r}")
