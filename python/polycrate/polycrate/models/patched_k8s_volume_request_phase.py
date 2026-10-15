from typing import Literal

PatchedK8SVolumeRequestPhase = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

PATCHED_K8S_VOLUME_REQUEST_PHASE_VALUES: set[PatchedK8SVolumeRequestPhase] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_patched_k8s_volume_request_phase(value: str) -> PatchedK8SVolumeRequestPhase:
    if value in PATCHED_K8S_VOLUME_REQUEST_PHASE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_PHASE_VALUES!r}")
