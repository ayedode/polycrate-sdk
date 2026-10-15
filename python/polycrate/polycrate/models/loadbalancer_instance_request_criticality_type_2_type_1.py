from typing import Literal

LoadbalancerInstanceRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

LOADBALANCER_INSTANCE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    LoadbalancerInstanceRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_loadbalancer_instance_request_criticality_type_2_type_1(
    value: str,
) -> LoadbalancerInstanceRequestCriticalityType2Type1:
    if value in LOADBALANCER_INSTANCE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
