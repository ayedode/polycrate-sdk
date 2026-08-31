from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentAttr
] = {
    "last_state",
}


def check_api_v1_block_rollout_configs_archive_create_last_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
