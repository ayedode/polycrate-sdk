from typing import Literal

ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_kubernetes_addons_update_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateScopeExpressionsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
