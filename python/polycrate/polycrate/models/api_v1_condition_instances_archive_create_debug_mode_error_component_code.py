from typing import Literal

ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
