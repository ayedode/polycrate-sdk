from typing import Literal

ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponentAttr = Literal["workspace"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponentAttr
] = {
    "workspace",
}


def check_api_v1_loadbalancers_instances_create_workspace_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateWorkspaceErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
