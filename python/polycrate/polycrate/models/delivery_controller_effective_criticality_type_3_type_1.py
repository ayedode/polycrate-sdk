from typing import Literal

DeliveryControllerEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

DELIVERY_CONTROLLER_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    DeliveryControllerEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_delivery_controller_effective_criticality_type_3_type_1(
    value: str,
) -> DeliveryControllerEffectiveCriticalityType3Type1:
    if value in DELIVERY_CONTROLLER_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
