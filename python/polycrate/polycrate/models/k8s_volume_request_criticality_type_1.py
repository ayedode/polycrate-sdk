from typing import Literal

K8SVolumeRequestCriticalityType1 = Literal["", "high", "low", "medium"]

K8S_VOLUME_REQUEST_CRITICALITY_TYPE_1_VALUES: set[K8SVolumeRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_volume_request_criticality_type_1(value: str) -> K8SVolumeRequestCriticalityType1:
    if value in K8S_VOLUME_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
