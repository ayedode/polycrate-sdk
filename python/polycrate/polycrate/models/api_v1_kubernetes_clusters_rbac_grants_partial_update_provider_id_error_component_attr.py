from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
