from typing import Literal

ApiV1CredentialsCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CredentialsCreateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_credentials_create_kind_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateKindErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
