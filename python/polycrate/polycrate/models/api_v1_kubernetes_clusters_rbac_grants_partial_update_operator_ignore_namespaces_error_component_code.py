from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_ignore_namespaces_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponentCode:
    if (
        value
        in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
