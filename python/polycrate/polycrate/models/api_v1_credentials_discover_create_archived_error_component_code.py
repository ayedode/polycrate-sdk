from typing import Literal

ApiV1CredentialsDiscoverCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsDiscoverCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_credentials_discover_create_archived_error_component_code(
    value: str,
) -> ApiV1CredentialsDiscoverCreateArchivedErrorComponentCode:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
