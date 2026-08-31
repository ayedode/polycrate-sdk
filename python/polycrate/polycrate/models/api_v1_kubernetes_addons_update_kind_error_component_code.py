from typing import Literal

ApiV1KubernetesAddonsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_addons_update_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
