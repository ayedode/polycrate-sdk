from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_block_rollout_configs_trigger_now_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
