from typing import Literal

ApiV1KubernetesClustersCreateLastBackupImportErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_KUBERNETES_CLUSTERS_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateLastBackupImportErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_clusters_create_last_backup_import_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateLastBackupImportErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
