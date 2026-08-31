from typing import Literal

ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_archive_create_installation_running_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateInstallationRunningErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
