from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_kubernetes_addon_config_revisions_list_workspaces_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListWorkspacesErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
