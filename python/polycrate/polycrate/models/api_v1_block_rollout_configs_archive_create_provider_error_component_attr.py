from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollout_configs_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
