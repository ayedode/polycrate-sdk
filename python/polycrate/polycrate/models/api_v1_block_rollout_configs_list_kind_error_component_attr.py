from typing import Literal

ApiV1BlockRolloutConfigsListKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollout_configs_list_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsListKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
