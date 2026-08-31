from typing import Literal

ApiV1ConditionInstancesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CONDITION_INSTANCES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_condition_instances_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
