from typing import Literal

ApiV1ConditionInstancesCreateResolvedAtErrorComponentAttr = Literal["resolved_at"]

API_V1_CONDITION_INSTANCES_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateResolvedAtErrorComponentAttr
] = {
    "resolved_at",
}


def check_api_v1_condition_instances_create_resolved_at_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateResolvedAtErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
