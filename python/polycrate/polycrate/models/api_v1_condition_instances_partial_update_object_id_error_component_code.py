from typing import Literal

ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_partial_update_object_id_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateObjectIdErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
