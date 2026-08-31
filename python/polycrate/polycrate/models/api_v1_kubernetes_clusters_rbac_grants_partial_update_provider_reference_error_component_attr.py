from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
