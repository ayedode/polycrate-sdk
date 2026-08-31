from typing import Literal

ApiV1KubernetesAppsListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_KUBERNETES_APPS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_kubernetes_apps_list_workspaces_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListWorkspacesErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
