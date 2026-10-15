from typing import Literal

K8SVolumeRequestKind = Literal["generic"]

K8S_VOLUME_REQUEST_KIND_VALUES: set[K8SVolumeRequestKind] = {
    "generic",
}


def check_k8s_volume_request_kind(value: str) -> K8SVolumeRequestKind:
    if value in K8S_VOLUME_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_VOLUME_REQUEST_KIND_VALUES!r}")
