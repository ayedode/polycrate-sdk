from typing import Literal

ApiV1DowntimesListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_DOWNTIMES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_downtimes_list_workspaces_error_component_code(
    value: str,
) -> ApiV1DowntimesListWorkspacesErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
