from typing import Literal

ApiV1KubernetesControlplanesUpdateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_update_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
