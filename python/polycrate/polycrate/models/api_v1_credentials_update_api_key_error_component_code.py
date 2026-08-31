from typing import Literal

ApiV1CredentialsUpdateApiKeyErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CredentialsUpdateApiKeyErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_update_api_key_error_component_code(
    value: str,
) -> ApiV1CredentialsUpdateApiKeyErrorComponentCode:
    if value in API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_API_KEY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
