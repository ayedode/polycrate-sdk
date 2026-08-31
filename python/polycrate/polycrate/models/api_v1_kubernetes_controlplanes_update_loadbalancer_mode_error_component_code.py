from typing import Literal

ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_update_loadbalancer_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
