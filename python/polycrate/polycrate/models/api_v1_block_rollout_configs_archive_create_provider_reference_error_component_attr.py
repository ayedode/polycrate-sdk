from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_block_rollout_configs_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
