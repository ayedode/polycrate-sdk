from typing import Literal

ApiV1WorkspacesCheckCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_workspaces_check_create_archived_at_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateArchivedAtErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
