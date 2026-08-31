from typing import Literal

ApiV1HostsListProviderDatacenterErrorComponentAttr = Literal["provider_datacenter"]

API_V1_HOSTS_LIST_PROVIDER_DATACENTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsListProviderDatacenterErrorComponentAttr
] = {
    "provider_datacenter",
}


def check_api_v1_hosts_list_provider_datacenter_error_component_attr(
    value: str,
) -> ApiV1HostsListProviderDatacenterErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_PROVIDER_DATACENTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_DATACENTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
