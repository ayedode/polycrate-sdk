from typing import Literal

ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_condition_instances_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
