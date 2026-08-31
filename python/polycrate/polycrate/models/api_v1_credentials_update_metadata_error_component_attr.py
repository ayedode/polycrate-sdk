from typing import Literal

ApiV1CredentialsUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_CREDENTIALS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_credentials_update_metadata_error_component_attr(
    value: str,
) -> ApiV1CredentialsUpdateMetadataErrorComponentAttr:
    if value in API_V1_CREDENTIALS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
