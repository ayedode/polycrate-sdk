from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_block_rollout_configs_trigger_now_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
