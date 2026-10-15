from typing import Literal

DeliveryControllerRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DeliveryControllerRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_delivery_controller_request_criticality_type_3_type_1(
    value: str,
) -> DeliveryControllerRequestCriticalityType3Type1:
    if value in DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
