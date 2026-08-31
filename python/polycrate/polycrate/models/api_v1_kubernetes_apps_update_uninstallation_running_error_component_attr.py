from typing import Literal

ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentAttr = Literal["uninstallation_running"]

API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentAttr
] = {
    "uninstallation_running",
}


def check_api_v1_kubernetes_apps_update_uninstallation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateUninstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
