from typing import Literal

ApiV1CredentialsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_credentials_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
