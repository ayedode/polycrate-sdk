from typing import Literal

ApiV1ActivitiesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_ACTIVITIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListWorkspacesErrorComponentAttr] = {
    "workspaces",
}


def check_api_v1_activities_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1ActivitiesListWorkspacesErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
