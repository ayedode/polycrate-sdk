from typing import Literal

ApiV1IncidentsListAffectedWorkspaceErrorComponentAttr = Literal["affected_workspace"]

API_V1_INCIDENTS_LIST_AFFECTED_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsListAffectedWorkspaceErrorComponentAttr
] = {
    "affected_workspace",
}


def check_api_v1_incidents_list_affected_workspace_error_component_attr(
    value: str,
) -> ApiV1IncidentsListAffectedWorkspaceErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_AFFECTED_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_AFFECTED_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
