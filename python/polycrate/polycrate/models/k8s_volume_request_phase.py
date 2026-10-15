from typing import Literal

K8SVolumeRequestPhase = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

K8S_VOLUME_REQUEST_PHASE_VALUES: set[K8SVolumeRequestPhase] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_k8s_volume_request_phase(value: str) -> K8SVolumeRequestPhase:
    if value in K8S_VOLUME_REQUEST_PHASE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_PHASE_VALUES!r}")
