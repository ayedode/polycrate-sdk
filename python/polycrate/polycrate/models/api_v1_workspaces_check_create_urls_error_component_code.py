from typing import Literal

ApiV1WorkspacesCheckCreateUrlsErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateUrlsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_check_create_urls_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateUrlsErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_URLS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
