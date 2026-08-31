from typing import Literal

ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_update_scope_expressions_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
