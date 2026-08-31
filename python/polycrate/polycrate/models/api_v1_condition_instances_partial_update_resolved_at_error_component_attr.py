from typing import Literal

ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponentAttr = Literal["resolved_at"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponentAttr
] = {
    "resolved_at",
}


def check_api_v1_condition_instances_partial_update_resolved_at_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateResolvedAtErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
