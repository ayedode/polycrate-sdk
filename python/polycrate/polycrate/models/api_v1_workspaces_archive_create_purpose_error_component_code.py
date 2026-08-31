from typing import Literal

ApiV1WorkspacesArchiveCreatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_archive_create_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
