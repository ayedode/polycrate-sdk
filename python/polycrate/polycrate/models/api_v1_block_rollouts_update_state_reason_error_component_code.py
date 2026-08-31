from typing import Literal

ApiV1BlockRolloutsUpdateStateReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUTS_UPDATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateStateReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollouts_update_state_reason_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateStateReasonErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_STATE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
