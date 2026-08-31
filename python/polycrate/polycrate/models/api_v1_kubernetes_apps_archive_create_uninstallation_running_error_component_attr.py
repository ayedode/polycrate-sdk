from typing import Literal

ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponentAttr = Literal["uninstallation_running"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponentAttr
] = {
    "uninstallation_running",
}


def check_api_v1_kubernetes_apps_archive_create_uninstallation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateUninstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
