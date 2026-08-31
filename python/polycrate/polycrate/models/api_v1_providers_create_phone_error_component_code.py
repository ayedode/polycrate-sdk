from typing import Literal

ApiV1ProvidersCreatePhoneErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreatePhoneErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_create_phone_error_component_code(value: str) -> ApiV1ProvidersCreatePhoneErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_PHONE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
