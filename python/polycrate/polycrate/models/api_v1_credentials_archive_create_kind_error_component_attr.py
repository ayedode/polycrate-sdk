from typing import Literal

ApiV1CredentialsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_credentials_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
