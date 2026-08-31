from typing import Literal

ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_block_rollout_configs_update_annotations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
