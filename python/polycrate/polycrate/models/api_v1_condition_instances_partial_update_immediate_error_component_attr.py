from typing import Literal

ApiV1ConditionInstancesPartialUpdateImmediateErrorComponentAttr = Literal["immediate"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateImmediateErrorComponentAttr
] = {
    "immediate",
}


def check_api_v1_condition_instances_partial_update_immediate_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateImmediateErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
