from typing import Literal

ApiV1CredentialsDiscoverCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_credentials_discover_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateArchivedAtErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
