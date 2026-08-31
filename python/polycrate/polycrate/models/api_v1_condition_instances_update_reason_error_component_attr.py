from typing import Literal

ApiV1ConditionInstancesUpdateReasonErrorComponentAttr = Literal["reason"]

API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateReasonErrorComponentAttr
] = {
    "reason",
}


def check_api_v1_condition_instances_update_reason_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateReasonErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
