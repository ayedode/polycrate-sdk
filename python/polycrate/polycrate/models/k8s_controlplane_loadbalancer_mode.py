from typing import Literal

K8SControlplaneLoadbalancerMode = Literal["cluster", "external"]

K8S_CONTROLPLANE_LOADBALANCER_MODE_VALUES: set[K8SControlplaneLoadbalancerMode] = {
    "cluster",
    "external",
}


def check_k8s_controlplane_loadbalancer_mode(value: str) -> K8SControlplaneLoadbalancerMode:
    if value in K8S_CONTROLPLANE_LOADBALANCER_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_LOADBALANCER_MODE_VALUES!r}")
