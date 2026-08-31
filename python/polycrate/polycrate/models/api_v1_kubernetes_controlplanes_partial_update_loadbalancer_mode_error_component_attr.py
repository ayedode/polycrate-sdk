from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponentAttr = Literal["loadbalancer_mode"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponentAttr
] = {
    "loadbalancer_mode",
}


def check_api_v1_kubernetes_controlplanes_partial_update_loadbalancer_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
