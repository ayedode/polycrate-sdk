from typing import Literal

ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponentAttr = Literal["backup_schedules"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponentAttr
] = {
    "backup_schedules",
}


def check_api_v1_kubernetes_clusters_partial_update_backup_schedules_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateBackupSchedulesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
