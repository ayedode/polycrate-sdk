from typing import Literal

ApiV1ConditionInstancesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITION_INSTANCES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_condition_instances_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
