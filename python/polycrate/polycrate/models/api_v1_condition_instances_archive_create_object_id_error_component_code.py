from typing import Literal

ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_archive_create_object_id_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateObjectIdErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
