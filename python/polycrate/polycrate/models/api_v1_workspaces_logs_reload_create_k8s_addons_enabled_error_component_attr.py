from typing import Literal

ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponentAttr = Literal["k8s_addons_enabled"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponentAttr
] = {
    "k8s_addons_enabled",
}


def check_api_v1_workspaces_logs_reload_create_k8s_addons_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateK8SAddonsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_K8S_ADDONS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
