from typing import Literal

ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_api_v1_kubernetes_clusters_partial_update_platform_dns_record_created_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
