from typing import Literal

ApiV1ApmApmstacksListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmApmstacksListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_apm_apmstacks_list_workspaces_error_component_code(
    value: str,
) -> ApiV1ApmApmstacksListWorkspacesErrorComponentCode:
    if value in API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
