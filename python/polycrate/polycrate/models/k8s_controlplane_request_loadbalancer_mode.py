from typing import Literal

K8SControlplaneRequestLoadbalancerMode = Literal["cluster", "external"]

K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES: set[K8SControlplaneRequestLoadbalancerMode] = {
    "cluster",
    "external",
}


def check_k8s_controlplane_request_loadbalancer_mode(value: str) -> K8SControlplaneRequestLoadbalancerMode:
    if value in K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES!r}"
    )
