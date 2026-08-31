from typing import Literal

ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_partial_update_allow_multiple_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
