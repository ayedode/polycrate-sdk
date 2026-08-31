from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollout_configs_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
