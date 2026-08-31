from typing import Literal

ApiV1ConditionInstancesPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_condition_instances_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateNameErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
