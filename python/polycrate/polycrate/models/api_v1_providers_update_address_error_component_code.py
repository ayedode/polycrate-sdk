from typing import Literal

ApiV1ProvidersUpdateAddressErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateAddressErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_update_address_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateAddressErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ADDRESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
