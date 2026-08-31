from typing import Literal

ApiV1BlockRolloutConfigsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_configs_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
