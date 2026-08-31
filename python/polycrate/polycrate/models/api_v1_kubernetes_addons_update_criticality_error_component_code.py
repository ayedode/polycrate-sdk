from typing import Literal

ApiV1KubernetesAddonsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addons_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
