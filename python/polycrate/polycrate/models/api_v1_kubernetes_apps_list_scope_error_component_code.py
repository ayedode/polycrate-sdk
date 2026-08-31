from typing import Literal

ApiV1KubernetesAppsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1KubernetesAppsListScopeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_apps_list_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
