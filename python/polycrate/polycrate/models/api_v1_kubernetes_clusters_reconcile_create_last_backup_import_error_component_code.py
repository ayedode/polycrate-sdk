from typing import Literal

ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_clusters_reconcile_create_last_backup_import_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
