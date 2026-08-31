from typing import Literal

ApiV1HostsUpdateProviderLocationErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsUpdateProviderLocationErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_update_provider_location_error_component_code(
    value: str,
) -> ApiV1HostsUpdateProviderLocationErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
