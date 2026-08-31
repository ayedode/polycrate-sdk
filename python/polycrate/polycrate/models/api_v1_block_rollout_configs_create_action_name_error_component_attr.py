from typing import Literal

ApiV1BlockRolloutConfigsCreateActionNameErrorComponentAttr = Literal["action_name"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateActionNameErrorComponentAttr
] = {
    "action_name",
}


def check_api_v1_block_rollout_configs_create_action_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateActionNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ACTION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
