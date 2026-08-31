from typing import Literal

ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alertrouters_partial_update_workspace_id_error_component_code(
    value: str,
) -> ApiV1AlertroutersPartialUpdateWorkspaceIdErrorComponentCode:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
