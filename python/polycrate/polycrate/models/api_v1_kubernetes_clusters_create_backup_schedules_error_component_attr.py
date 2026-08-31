from typing import Literal

ApiV1KubernetesClustersCreateBackupSchedulesErrorComponentAttr = Literal["backup_schedules"]

API_V1_KUBERNETES_CLUSTERS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateBackupSchedulesErrorComponentAttr
] = {
    "backup_schedules",
}


def check_api_v1_kubernetes_clusters_create_backup_schedules_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateBackupSchedulesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
