from typing import Literal

ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_block_rollouts_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
