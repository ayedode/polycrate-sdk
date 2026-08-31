from typing import Literal

ApiV1WorkspacesArchiveCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_archive_create_scope_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateScopeErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
