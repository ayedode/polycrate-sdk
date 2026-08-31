from typing import Literal

ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentAttr = Literal["last_backup_import"]

API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentAttr
] = {
    "last_backup_import",
}


def check_api_v1_kubernetes_clusters_reconcile_create_last_backup_import_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersReconcileCreateLastBackupImportErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RECONCILE_CREATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
