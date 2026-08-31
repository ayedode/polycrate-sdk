from typing import Literal

ApiV1IncidentsCreateWorkspaceIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_INCIDENTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IncidentsCreateWorkspaceIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_incidents_create_workspace_id_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateWorkspaceIdErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_WORKSPACE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
