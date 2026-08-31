from typing import Literal

ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_update_allow_multiple_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
