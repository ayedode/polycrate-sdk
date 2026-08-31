from typing import Literal

ApiV1ConditionInstancesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_condition_instances_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateKindErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
