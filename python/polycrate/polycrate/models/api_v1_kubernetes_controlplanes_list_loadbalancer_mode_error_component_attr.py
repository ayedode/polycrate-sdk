from typing import Literal

ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentAttr = Literal["loadbalancer_mode"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentAttr
] = {
    "loadbalancer_mode",
}


def check_api_v1_kubernetes_controlplanes_list_loadbalancer_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
