from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_block_rollout_configs_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
