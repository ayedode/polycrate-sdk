from typing import Literal

ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_condition_instances_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
