from typing import Literal

ApiV1WorkspacesUpdatePopIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_WORKSPACES_UPDATE_POP_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesUpdatePopIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_workspaces_update_pop_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdatePopIdErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_POP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_POP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
