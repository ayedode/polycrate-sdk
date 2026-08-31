from typing import Literal

ApiV1ProvidersUpdatePhoneErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdatePhoneErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_update_phone_error_component_code(value: str) -> ApiV1ProvidersUpdatePhoneErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
