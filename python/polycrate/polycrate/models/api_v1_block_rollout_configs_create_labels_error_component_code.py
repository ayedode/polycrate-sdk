from typing import Literal

ApiV1BlockRolloutConfigsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_create_labels_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
