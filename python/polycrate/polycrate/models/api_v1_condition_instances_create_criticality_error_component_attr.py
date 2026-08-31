from typing import Literal

ApiV1ConditionInstancesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_condition_instances_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
