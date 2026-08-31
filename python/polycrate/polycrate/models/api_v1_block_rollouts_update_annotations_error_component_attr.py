from typing import Literal

ApiV1BlockRolloutsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCK_ROLLOUTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_block_rollouts_update_annotations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
