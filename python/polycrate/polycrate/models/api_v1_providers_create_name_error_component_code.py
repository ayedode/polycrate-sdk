from typing import Literal

ApiV1ProvidersCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_providers_create_name_error_component_code(value: str) -> ApiV1ProvidersCreateNameErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
