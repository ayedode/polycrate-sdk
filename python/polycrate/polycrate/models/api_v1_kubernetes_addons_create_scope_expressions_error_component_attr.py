from typing import Literal

ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponentAttr = Literal["scope_expressions"]

API_V1_KUBERNETES_ADDONS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponentAttr
] = {
    "scope_expressions",
}


def check_api_v1_kubernetes_addons_create_scope_expressions_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateScopeExpressionsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_SCOPE_EXPRESSIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
