from typing import Literal

ApiV1WorkspacesArchiveCreateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_archive_create_urls_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateUrlsErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
