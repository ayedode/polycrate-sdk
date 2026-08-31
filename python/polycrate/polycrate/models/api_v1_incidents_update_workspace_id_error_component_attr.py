from typing import Literal

ApiV1IncidentsUpdateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_incidents_update_workspace_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateWorkspaceIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
