from typing import Literal

ApiV1WorkspacesListPopErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesListPopErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_workspaces_list_pop_error_component_code(value: str) -> ApiV1WorkspacesListPopErrorComponentCode:
    if value in API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_POP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
