from typing import Literal

ApiV1KubernetesAddonsListScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_addons_list_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
