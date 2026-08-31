from typing import Literal

ApiV1HostsDiscoverCreateProviderAccountIdErrorComponentAttr = Literal["provider_account_id"]

API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateProviderAccountIdErrorComponentAttr
] = {
    "provider_account_id",
}


def check_api_v1_hosts_discover_create_provider_account_id_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateProviderAccountIdErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
