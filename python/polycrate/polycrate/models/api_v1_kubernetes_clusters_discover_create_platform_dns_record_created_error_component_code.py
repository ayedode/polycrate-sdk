from typing import Literal

ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_discover_create_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
