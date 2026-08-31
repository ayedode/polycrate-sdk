from typing import Literal

ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_update_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
