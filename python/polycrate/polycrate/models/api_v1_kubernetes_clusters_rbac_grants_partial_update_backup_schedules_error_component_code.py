from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_backup_schedules_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BACKUP_SCHEDULES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
