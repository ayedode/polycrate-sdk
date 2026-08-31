from typing import Literal

ApiV1ConditionInstancesUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_CONDITION_INSTANCES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_condition_instances_update_active_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateActiveErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
