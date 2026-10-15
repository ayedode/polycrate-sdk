from typing import Literal

K8SControlplaneKind = Literal["generic"]

K8S_CONTROLPLANE_KIND_VALUES: set[K8SControlplaneKind] = {
    "generic",
}


def check_k8s_controlplane_kind(value: str) -> K8SControlplaneKind:
    if value in K8S_CONTROLPLANE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_KIND_VALUES!r}")
