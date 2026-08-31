from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_block_rollout_configs_archive_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
