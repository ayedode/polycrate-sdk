from typing import Literal

PatchedK8SVolumeRequestVolumeMode = Literal["Block", "Filesystem"]

PATCHED_K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES: set[PatchedK8SVolumeRequestVolumeMode] = {
    "Block",
    "Filesystem",
}


def check_patched_k8s_volume_request_volume_mode(value: str) -> PatchedK8SVolumeRequestVolumeMode:
    if value in PATCHED_K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES!r}")
