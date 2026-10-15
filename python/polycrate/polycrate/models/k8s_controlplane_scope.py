from typing import Literal

K8SControlplaneScope = Literal["system", "user"]

K8S_CONTROLPLANE_SCOPE_VALUES: set[K8SControlplaneScope] = {
    "system",
    "user",
}


def check_k8s_controlplane_scope(value: str) -> K8SControlplaneScope:
    if value in K8S_CONTROLPLANE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_SCOPE_VALUES!r}")
