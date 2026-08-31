from typing import Literal

ApiV1KubernetesAppsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_APPS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_apps_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
