from typing import Literal

PatchedDeliveryControllerRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedDeliveryControllerRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_delivery_controller_request_criticality_type_2_type_1(
    value: str,
) -> PatchedDeliveryControllerRequestCriticalityType2Type1:
    if value in PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DELIVERY_CONTROLLER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
