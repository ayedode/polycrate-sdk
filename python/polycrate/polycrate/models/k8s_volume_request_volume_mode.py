from typing import Literal

K8SVolumeRequestVolumeMode = Literal["Block", "Filesystem"]

K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES: set[K8SVolumeRequestVolumeMode] = {
    "Block",
    "Filesystem",
}


def check_k8s_volume_request_volume_mode(value: str) -> K8SVolumeRequestVolumeMode:
    if value in K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_VOLUME_MODE_VALUES!r}")
