from typing import Literal

ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
