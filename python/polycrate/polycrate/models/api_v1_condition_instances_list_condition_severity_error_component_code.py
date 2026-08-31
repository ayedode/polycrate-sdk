from typing import Literal

ApiV1ConditionInstancesListConditionSeverityErrorComponentCode = Literal["invalid_choice"]

API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesListConditionSeverityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_condition_instances_list_condition_severity_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesListConditionSeverityErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
