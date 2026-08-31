from typing import Literal

ApiV1ExternalCredentialsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ExternalCredentialsCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_external_credentials_create_kind_error_component_code(
    value: str,
) -> ApiV1ExternalCredentialsCreateKindErrorComponentCode:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
