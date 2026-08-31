from typing import Literal

ApiV1WorkspacesCheckCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_workspaces_check_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
