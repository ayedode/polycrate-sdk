from typing import Literal

ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_kubernetes_clusters_discover_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
