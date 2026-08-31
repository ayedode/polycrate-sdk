from typing import Literal

ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_partial_update_is_default_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
