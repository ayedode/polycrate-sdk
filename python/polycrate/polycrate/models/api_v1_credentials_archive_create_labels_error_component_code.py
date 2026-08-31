from typing import Literal

ApiV1CredentialsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_credentials_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1CredentialsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
