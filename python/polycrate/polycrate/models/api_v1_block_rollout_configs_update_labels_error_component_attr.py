from typing import Literal

ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_block_rollout_configs_update_labels_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
