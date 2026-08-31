from typing import Literal

ApiV1ConditionInstancesCreateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_CONDITION_INSTANCES_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_condition_instances_create_object_id_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateObjectIdErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
