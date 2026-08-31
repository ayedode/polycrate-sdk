from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_block_rollout_configs_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
