from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_last_backup_import_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_LAST_BACKUP_IMPORT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
