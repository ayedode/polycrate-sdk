from typing import Literal

K8SControlplaneRequestScope = Literal["system", "user"]

K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES: set[K8SControlplaneRequestScope] = {
    "system",
    "user",
}


def check_k8s_controlplane_request_scope(value: str) -> K8SControlplaneRequestScope:
    if value in K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_REQUEST_SCOPE_VALUES!r}")
