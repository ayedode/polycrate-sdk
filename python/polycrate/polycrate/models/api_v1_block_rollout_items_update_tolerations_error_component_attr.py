from typing import Literal

ApiV1BlockRolloutItemsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollout_items_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
