from typing import Literal

ApiV1ConditionInstancesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_condition_instances_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateTolerationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
