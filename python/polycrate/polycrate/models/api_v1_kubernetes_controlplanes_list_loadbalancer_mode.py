from typing import Literal

ApiV1KubernetesControlplanesListLoadbalancerMode = Literal["cluster", "external"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_VALUES: set[ApiV1KubernetesControlplanesListLoadbalancerMode] = {
    "cluster",
    "external",
}


def check_api_v1_kubernetes_controlplanes_list_loadbalancer_mode(
    value: str,
) -> ApiV1KubernetesControlplanesListLoadbalancerMode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_VALUES!r}"
    )
