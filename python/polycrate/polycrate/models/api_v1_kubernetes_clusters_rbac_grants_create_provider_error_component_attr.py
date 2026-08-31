from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
