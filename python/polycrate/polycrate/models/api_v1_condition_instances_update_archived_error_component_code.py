from typing import Literal

ApiV1ConditionInstancesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_update_archived_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesUpdateArchivedErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
