from typing import Literal

ApiV1ConditionInstancesPartialUpdateConditionErrorComponentAttr = Literal["condition"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateConditionErrorComponentAttr
] = {
    "condition",
}


def check_api_v1_condition_instances_partial_update_condition_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateConditionErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
