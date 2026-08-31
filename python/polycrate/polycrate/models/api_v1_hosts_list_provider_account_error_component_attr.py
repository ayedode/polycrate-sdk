from typing import Literal

ApiV1HostsListProviderAccountErrorComponentAttr = Literal["provider_account"]

API_V1_HOSTS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListProviderAccountErrorComponentAttr] = {
    "provider_account",
}


def check_api_v1_hosts_list_provider_account_error_component_attr(
    value: str,
) -> ApiV1HostsListProviderAccountErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_ACCOUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
