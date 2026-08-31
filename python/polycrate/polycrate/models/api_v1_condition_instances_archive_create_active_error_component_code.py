from typing import Literal

ApiV1ConditionInstancesArchiveCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_condition_instances_archive_create_active_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateActiveErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
