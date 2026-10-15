from typing import Literal

PatchedK8SVolumeRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_K8S_VOLUME_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedK8SVolumeRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_k8s_volume_request_criticality_type_2_type_1(
    value: str,
) -> PatchedK8SVolumeRequestCriticalityType2Type1:
    if value in PATCHED_K8S_VOLUME_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
