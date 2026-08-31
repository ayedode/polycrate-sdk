from typing import Literal

ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_addons_partial_update_enforcement_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
