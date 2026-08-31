from typing import Literal

ApiV1BlockRolloutsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_block_rollouts_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
