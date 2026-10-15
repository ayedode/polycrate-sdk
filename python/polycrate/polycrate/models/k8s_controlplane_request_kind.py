from typing import Literal

K8SControlplaneRequestKind = Literal["generic"]

K8S_CONTROLPLANE_REQUEST_KIND_VALUES: set[K8SControlplaneRequestKind] = {
    "generic",
}


def check_k8s_controlplane_request_kind(value: str) -> K8SControlplaneRequestKind:
    if value in K8S_CONTROLPLANE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_REQUEST_KIND_VALUES!r}")
