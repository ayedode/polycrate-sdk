from typing import Literal

ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_kubernetes_clusters_discover_create_credential_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateCredentialErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
