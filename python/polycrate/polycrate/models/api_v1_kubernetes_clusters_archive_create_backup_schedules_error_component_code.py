from typing import Literal

ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_archive_create_backup_schedules_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
