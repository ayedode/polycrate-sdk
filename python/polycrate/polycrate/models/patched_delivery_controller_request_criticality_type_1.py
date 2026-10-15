from typing import Literal

PatchedDeliveryControllerRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedDeliveryControllerRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_delivery_controller_request_criticality_type_1(
    value: str,
) -> PatchedDeliveryControllerRequestCriticalityType1:
    if value in PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
