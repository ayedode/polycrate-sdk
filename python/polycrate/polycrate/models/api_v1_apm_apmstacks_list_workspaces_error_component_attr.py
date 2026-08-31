from typing import Literal

ApiV1ApmApmstacksListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmApmstacksListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_apm_apmstacks_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListWorkspacesErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
