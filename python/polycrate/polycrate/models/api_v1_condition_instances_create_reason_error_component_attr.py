from typing import Literal

ApiV1ConditionInstancesCreateReasonErrorComponentAttr = Literal["reason"]

API_V1_CONDITION_INSTANCES_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateReasonErrorComponentAttr
] = {
    "reason",
}


def check_api_v1_condition_instances_create_reason_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateReasonErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
