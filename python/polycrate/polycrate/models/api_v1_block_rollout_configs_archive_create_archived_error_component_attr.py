from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_block_rollout_configs_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
