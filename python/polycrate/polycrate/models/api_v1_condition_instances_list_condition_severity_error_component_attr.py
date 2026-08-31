from typing import Literal

ApiV1ConditionInstancesListConditionSeverityErrorComponentAttr = Literal["condition__severity"]

API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesListConditionSeverityErrorComponentAttr
] = {
    "condition__severity",
}


def check_api_v1_condition_instances_list_condition_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesListConditionSeverityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
