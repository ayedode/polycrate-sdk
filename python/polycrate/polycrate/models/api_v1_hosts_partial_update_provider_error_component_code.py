from typing import Literal

ApiV1HostsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_hosts_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
