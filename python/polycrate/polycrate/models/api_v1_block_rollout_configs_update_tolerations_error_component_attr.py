from typing import Literal

ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollout_configs_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
