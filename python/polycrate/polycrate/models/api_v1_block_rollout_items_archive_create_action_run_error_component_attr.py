from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponentAttr = Literal["action_run"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponentAttr
] = {
    "action_run",
}


def check_api_v1_block_rollout_items_archive_create_action_run_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
