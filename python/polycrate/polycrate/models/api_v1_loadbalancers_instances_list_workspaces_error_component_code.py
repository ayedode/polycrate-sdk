from typing import Literal

ApiV1LoadbalancersInstancesListWorkspacesErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_LOADBALANCERS_INSTANCES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_loadbalancers_instances_list_workspaces_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesListWorkspacesErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
