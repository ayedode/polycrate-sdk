from typing import Literal

ApiV1HostsPartialUpdateProviderImageErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateProviderImageErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_partial_update_provider_image_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateProviderImageErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_IMAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
