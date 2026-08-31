from typing import Literal

ApiV1ConditionInstancesUpdateObjectIdErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateObjectIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_update_object_id_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateObjectIdErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
