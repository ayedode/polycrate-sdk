from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_block_rollout_configs_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
