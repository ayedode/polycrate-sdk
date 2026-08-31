from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponentAttr = Literal["auto_takeover"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_AUTO_TAKEOVER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponentAttr
] = {
    "auto_takeover",
}


def check_api_v1_block_rollout_configs_archive_create_auto_takeover_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_AUTO_TAKEOVER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_AUTO_TAKEOVER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
