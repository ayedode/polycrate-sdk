from typing import Literal

ApiV1KubernetesAppsCreateUninstallationRunningErrorComponentAttr = Literal["uninstallation_running"]

API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateUninstallationRunningErrorComponentAttr
] = {
    "uninstallation_running",
}


def check_api_v1_kubernetes_apps_create_uninstallation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateUninstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
