from typing import Literal

ApiV1CredentialsCreateMetadataErrorComponentCode = Literal["invalid"]

API_V1_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsCreateMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_credentials_create_metadata_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateMetadataErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
