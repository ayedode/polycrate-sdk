from typing import Literal

ApiV1BlockRolloutConfigsCreateActiveErrorComponentAttr = Literal["active"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_block_rollout_configs_create_active_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateActiveErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
