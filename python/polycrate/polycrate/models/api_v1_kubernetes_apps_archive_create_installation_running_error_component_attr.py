from typing import Literal

ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_api_v1_kubernetes_apps_archive_create_installation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
