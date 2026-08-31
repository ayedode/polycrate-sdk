from typing import Literal

ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_condition_instances_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
