from typing import Literal

ApiV1IncidentsUpdateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsUpdateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_incidents_update_workspace_id_error_component_code(
    value: str,
) -> ApiV1IncidentsUpdateWorkspaceIdErrorComponentCode:
    if value in API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
