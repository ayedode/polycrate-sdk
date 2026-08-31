from typing import Literal

ApiV1BlockRolloutItemsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_block_rollout_items_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
