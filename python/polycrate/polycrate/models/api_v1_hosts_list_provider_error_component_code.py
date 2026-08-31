from typing import Literal

ApiV1HostsListProviderErrorComponentCode = Literal["invalid_choice"]

API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsListProviderErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_hosts_list_provider_error_component_code(value: str) -> ApiV1HostsListProviderErrorComponentCode:
    if value in API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
