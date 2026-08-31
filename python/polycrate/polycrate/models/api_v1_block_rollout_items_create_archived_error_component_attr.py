from typing import Literal

ApiV1BlockRolloutItemsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_block_rollout_items_create_archived_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateArchivedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
