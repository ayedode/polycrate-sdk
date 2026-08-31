from typing import Literal

ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_block_rollout_items_archive_create_conditions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
