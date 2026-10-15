from typing import Literal

PatchedK8SControlplaneRequestLoadbalancerMode = Literal["cluster", "external"]

PATCHED_K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES: set[PatchedK8SControlplaneRequestLoadbalancerMode] = {
    "cluster",
    "external",
}


def check_patched_k8s_controlplane_request_loadbalancer_mode(
    value: str,
) -> PatchedK8SControlplaneRequestLoadbalancerMode:
    if value in PATCHED_K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CONTROLPLANE_REQUEST_LOADBALANCER_MODE_VALUES!r}"
    )
