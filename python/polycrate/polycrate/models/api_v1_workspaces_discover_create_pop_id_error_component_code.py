from typing import Literal

ApiV1WorkspacesDiscoverCreatePopIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_WORKSPACES_DISCOVER_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreatePopIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_workspaces_discover_create_pop_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreatePopIdErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
