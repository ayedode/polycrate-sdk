from typing import Literal

K8SVolumeVolumeMode = Literal["Block", "Filesystem"]

K8S_VOLUME_VOLUME_MODE_VALUES: set[K8SVolumeVolumeMode] = {
    "Block",
    "Filesystem",
}


def check_k8s_volume_volume_mode(value: str) -> K8SVolumeVolumeMode:
    if value in K8S_VOLUME_VOLUME_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_VOLUME_MODE_VALUES!r}")
