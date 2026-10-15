from typing import Literal

DeliveryControllerCriticalityType1 = Literal["", "high", "low", "medium"]

DELIVERY_CONTROLLER_CRITICALITY_TYPE_1_VALUES: set[DeliveryControllerCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_delivery_controller_criticality_type_1(value: str) -> DeliveryControllerCriticalityType1:
    if value in DELIVERY_CONTROLLER_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_CRITICALITY_TYPE_1_VALUES!r}")
