from typing import Literal

ApiV1KubernetesClustersUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_kubernetes_clusters_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
