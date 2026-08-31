from typing import Literal

ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addons_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
