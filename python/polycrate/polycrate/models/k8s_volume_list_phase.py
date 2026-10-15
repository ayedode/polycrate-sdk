from typing import Literal

K8SVolumeListPhase = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

K8S_VOLUME_LIST_PHASE_VALUES: set[K8SVolumeListPhase] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_k8s_volume_list_phase(value: str) -> K8SVolumeListPhase:
    if value in K8S_VOLUME_LIST_PHASE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_LIST_PHASE_VALUES!r}")
