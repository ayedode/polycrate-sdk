from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_configs_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
