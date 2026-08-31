from typing import Literal

ApiV1AlertroutersListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_alertrouters_list_workspaces_error_component_code(
    value: str,
) -> ApiV1AlertroutersListWorkspacesErrorComponentCode:
    if value in API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
