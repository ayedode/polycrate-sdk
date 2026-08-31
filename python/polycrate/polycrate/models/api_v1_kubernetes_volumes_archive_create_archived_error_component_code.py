from typing import Literal

ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_volumes_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
