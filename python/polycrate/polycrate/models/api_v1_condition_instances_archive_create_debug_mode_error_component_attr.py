from typing import Literal

ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_condition_instances_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
