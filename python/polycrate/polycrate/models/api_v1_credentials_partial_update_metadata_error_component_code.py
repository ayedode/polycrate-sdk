from typing import Literal

ApiV1CredentialsPartialUpdateMetadataErrorComponentCode = Literal["invalid"]

API_V1_CREDENTIALS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_credentials_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1CredentialsPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
