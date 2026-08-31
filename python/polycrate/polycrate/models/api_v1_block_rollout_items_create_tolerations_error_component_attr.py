from typing import Literal

ApiV1BlockRolloutItemsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollout_items_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
