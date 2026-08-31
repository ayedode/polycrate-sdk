from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_block_rollout_configs_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateKindErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
