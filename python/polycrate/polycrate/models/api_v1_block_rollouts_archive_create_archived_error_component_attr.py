from typing import Literal

ApiV1BlockRolloutsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_block_rollouts_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
