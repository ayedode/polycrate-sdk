from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponentAttr = Literal["backup_schedules"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponentAttr
] = {
    "backup_schedules",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_backup_schedules_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_BACKUP_SCHEDULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
