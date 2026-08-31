from typing import Literal

ApiV1BackupsBackupSchedulesListK8SClusterErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListK8SClusterErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_backups_backup_schedules_list_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListK8SClusterErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
