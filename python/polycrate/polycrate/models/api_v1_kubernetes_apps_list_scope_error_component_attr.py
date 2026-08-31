from typing import Literal

ApiV1KubernetesAppsListScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsListScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_kubernetes_apps_list_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
