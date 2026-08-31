from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponentAttr = Literal["source_user"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponentAttr
] = {
    "source_user",
}


def check_api_v1_block_rollout_items_archive_create_source_user_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_SOURCE_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
