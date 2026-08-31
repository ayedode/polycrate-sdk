from typing import Literal

ApiV1KubernetesAddonsUpdateEnforcementErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateEnforcementErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_addons_update_enforcement_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateEnforcementErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
