from typing import Literal

ApiV1ProvidersArchiveCreateAddressErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateAddressErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_archive_create_address_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateAddressErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
