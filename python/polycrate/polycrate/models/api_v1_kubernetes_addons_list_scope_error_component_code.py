from typing import Literal

ApiV1KubernetesAddonsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addons_list_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
