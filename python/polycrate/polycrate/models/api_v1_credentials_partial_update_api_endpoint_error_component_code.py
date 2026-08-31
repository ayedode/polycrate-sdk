from typing import Literal

ApiV1CredentialsPartialUpdateApiEndpointErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CREDENTIALS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsPartialUpdateApiEndpointErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_credentials_partial_update_api_endpoint_error_component_code(
    value: str,
) -> ApiV1CredentialsPartialUpdateApiEndpointErrorComponentCode:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
