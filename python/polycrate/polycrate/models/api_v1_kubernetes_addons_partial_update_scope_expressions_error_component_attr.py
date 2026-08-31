from typing import Literal

ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_kubernetes_addons_partial_update_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateScopeExpressionsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
