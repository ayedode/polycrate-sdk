from typing import Literal

K8SVolumePhase = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

K8S_VOLUME_PHASE_VALUES: set[K8SVolumePhase] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_k8s_volume_phase(value: str) -> K8SVolumePhase:
    if value in K8S_VOLUME_PHASE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_PHASE_VALUES!r}")
