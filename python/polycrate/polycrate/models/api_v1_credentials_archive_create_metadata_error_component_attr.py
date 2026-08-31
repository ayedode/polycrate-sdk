from typing import Literal

ApiV1CredentialsArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_credentials_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
