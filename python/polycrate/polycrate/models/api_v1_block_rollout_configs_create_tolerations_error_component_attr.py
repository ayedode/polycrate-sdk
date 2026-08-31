from typing import Literal

ApiV1BlockRolloutConfigsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollout_configs_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
