from typing import Literal

ApiV1ConditionInstancesListConditionErrorComponentAttr = Literal["condition"]

API_V1_CONDITION_INSTANCES_LIST_CONDITION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesListConditionErrorComponentAttr
] = {
    "condition",
}


def check_api_v1_condition_instances_list_condition_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesListConditionErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_LIST_CONDITION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_CONDITION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
