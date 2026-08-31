from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponentAttr = Literal["alias"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_alias_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
