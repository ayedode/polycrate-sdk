from typing import Literal

ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_archive_create_installation_failed_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateInstallationFailedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
