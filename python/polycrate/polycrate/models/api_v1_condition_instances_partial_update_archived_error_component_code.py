from typing import Literal

ApiV1ConditionInstancesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
