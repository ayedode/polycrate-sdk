from typing import Literal

ApiV1ConditionInstancesPartialUpdateReasonErrorComponentAttr = Literal["reason"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateReasonErrorComponentAttr
] = {
    "reason",
}


def check_api_v1_condition_instances_partial_update_reason_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateReasonErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
