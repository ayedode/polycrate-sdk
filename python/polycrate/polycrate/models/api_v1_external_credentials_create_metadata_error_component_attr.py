from typing import Literal

ApiV1ExternalCredentialsCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ExternalCredentialsCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_external_credentials_create_metadata_error_component_attr(
    value: str,
) -> ApiV1ExternalCredentialsCreateMetadataErrorComponentAttr:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
