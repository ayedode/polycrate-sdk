from typing import Literal

ApiV1KubernetesAppsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_APPS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_apps_update_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
