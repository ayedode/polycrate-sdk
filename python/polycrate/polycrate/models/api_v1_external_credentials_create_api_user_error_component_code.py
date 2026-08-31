from typing import Literal

ApiV1ExternalCredentialsCreateApiUserErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_EXTERNAL_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ExternalCredentialsCreateApiUserErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_external_credentials_create_api_user_error_component_code(
    value: str,
) -> ApiV1ExternalCredentialsCreateApiUserErrorComponentCode:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
