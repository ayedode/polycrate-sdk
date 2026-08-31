from typing import Literal

ApiV1BlockRolloutConfigsCreateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_block_rollout_configs_create_conditions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateConditionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
