from typing import Literal

ApiV1ConditionInstancesUpdateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_condition_instances_update_object_id_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateObjectIdErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
