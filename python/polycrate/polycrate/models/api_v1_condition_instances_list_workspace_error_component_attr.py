from typing import Literal

ApiV1ConditionInstancesListWorkspaceErrorComponentAttr = Literal["workspace"]

API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesListWorkspaceErrorComponentAttr
] = {
    "workspace",
}


def check_api_v1_condition_instances_list_workspace_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesListWorkspaceErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
