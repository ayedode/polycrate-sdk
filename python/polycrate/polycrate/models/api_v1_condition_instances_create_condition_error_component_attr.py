from typing import Literal

ApiV1ConditionInstancesCreateConditionErrorComponentAttr = Literal["condition"]

API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateConditionErrorComponentAttr
] = {
    "condition",
}


def check_api_v1_condition_instances_create_condition_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateConditionErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
