from typing import Literal

ApiV1ConditionInstancesListWorkspaceErrorComponentCode = Literal["invalid_choice"]

API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesListWorkspaceErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_condition_instances_list_workspace_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesListWorkspaceErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
