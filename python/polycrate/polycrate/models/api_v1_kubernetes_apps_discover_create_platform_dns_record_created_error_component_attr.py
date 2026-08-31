from typing import Literal

ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_api_v1_kubernetes_apps_discover_create_platform_dns_record_created_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
