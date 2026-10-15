from typing import Literal

DeliveryControllerListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DELIVERY_CONTROLLER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DeliveryControllerListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_delivery_controller_list_effective_criticality_type_1(
    value: str,
) -> DeliveryControllerListEffectiveCriticalityType1:
    if value in DELIVERY_CONTROLLER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
