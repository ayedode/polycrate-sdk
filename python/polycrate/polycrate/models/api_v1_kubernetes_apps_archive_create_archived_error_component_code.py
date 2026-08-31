from typing import Literal

ApiV1KubernetesAppsArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
