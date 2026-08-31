from typing import Literal

ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_controlplanes_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
