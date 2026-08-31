from typing import Literal

ApiV1CredentialsArchiveCreateApiEndpointErrorComponentAttr = Literal["api_endpoint"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateApiEndpointErrorComponentAttr
] = {
    "api_endpoint",
}


def check_api_v1_credentials_archive_create_api_endpoint_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateApiEndpointErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_API_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
