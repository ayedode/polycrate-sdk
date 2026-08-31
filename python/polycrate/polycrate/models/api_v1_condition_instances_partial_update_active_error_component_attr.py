from typing import Literal

ApiV1ConditionInstancesPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_condition_instances_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
