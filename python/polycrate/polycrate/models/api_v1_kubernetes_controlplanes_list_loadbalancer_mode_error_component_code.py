from typing import Literal

ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_controlplanes_list_loadbalancer_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesListLoadbalancerModeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
