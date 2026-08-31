from typing import Literal

ApiV1KubernetesAppsDiscoverCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
