from typing import Literal

ApiV1ConditionInstancesListConditionSeverity = Literal["critical", "info", "warning"]

API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_VALUES: set[ApiV1ConditionInstancesListConditionSeverity] = {
    "critical",
    "info",
    "warning",
}


def check_api_v1_condition_instances_list_condition_severity(
    value: str,
) -> ApiV1ConditionInstancesListConditionSeverity:
    if value in API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_CONDITION_SEVERITY_VALUES!r}"
    )
