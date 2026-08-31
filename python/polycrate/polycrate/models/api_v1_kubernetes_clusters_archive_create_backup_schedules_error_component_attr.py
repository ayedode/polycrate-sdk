from typing import Literal

ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentAttr = Literal["backup_schedules"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentAttr
] = {
    "backup_schedules",
}


def check_api_v1_kubernetes_clusters_archive_create_backup_schedules_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateBackupSchedulesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
