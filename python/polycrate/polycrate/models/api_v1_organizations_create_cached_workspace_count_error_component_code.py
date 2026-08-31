from typing import Literal

ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_organizations_create_cached_workspace_count_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_CACHED_WORKSPACE_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
