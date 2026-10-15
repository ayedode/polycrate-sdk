from typing import Literal

K8SVolumeKind = Literal["generic"]

K8S_VOLUME_KIND_VALUES: set[K8SVolumeKind] = {
    "generic",
}


def check_k8s_volume_kind(value: str) -> K8SVolumeKind:
    if value in K8S_VOLUME_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_KIND_VALUES!r}")
