from typing import Literal

ApiV1BlockRolloutConfigsListNameExactErrorComponentAttr = Literal["name_exact"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsListNameExactErrorComponentAttr
] = {
    "name_exact",
}


def check_api_v1_block_rollout_configs_list_name_exact_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsListNameExactErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_NAME_EXACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
