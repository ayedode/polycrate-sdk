from typing import Literal

ApiV1HostsListProviderErrorComponentAttr = Literal["provider"]

API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_hosts_list_provider_error_component_attr(value: str) -> ApiV1HostsListProviderErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
