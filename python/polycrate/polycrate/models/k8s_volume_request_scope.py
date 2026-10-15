from typing import Literal

K8SVolumeRequestScope = Literal["system", "user"]

K8S_VOLUME_REQUEST_SCOPE_VALUES: set[K8SVolumeRequestScope] = {
    "system",
    "user",
}


def check_k8s_volume_request_scope(value: str) -> K8SVolumeRequestScope:
    if value in K8S_VOLUME_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_SCOPE_VALUES!r}")
