from typing import Literal

DeliveryControllerScope = Literal["system", "user"]

DELIVERY_CONTROLLER_SCOPE_VALUES: set[DeliveryControllerScope] = {
    "system",
    "user",
}


def check_delivery_controller_scope(value: str) -> DeliveryControllerScope:
    if value in DELIVERY_CONTROLLER_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_SCOPE_VALUES!r}")
