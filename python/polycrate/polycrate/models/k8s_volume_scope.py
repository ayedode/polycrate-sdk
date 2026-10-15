from typing import Literal

K8SVolumeScope = Literal["system", "user"]

K8S_VOLUME_SCOPE_VALUES: set[K8SVolumeScope] = {
    "system",
    "user",
}


def check_k8s_volume_scope(value: str) -> K8SVolumeScope:
    if value in K8S_VOLUME_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_SCOPE_VALUES!r}")
