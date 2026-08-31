from typing import Literal

ApiV1BlockRolloutConfigsCreateStateReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateStateReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_configs_create_state_reason_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateStateReasonErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
