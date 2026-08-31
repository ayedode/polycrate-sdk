from typing import Literal

ApiV1CredentialsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_credentials_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
