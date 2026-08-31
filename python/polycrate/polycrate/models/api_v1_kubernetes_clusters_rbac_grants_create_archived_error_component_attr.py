from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
