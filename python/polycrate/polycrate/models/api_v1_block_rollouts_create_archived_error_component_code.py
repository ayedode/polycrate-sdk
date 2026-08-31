from typing import Literal

ApiV1BlockRolloutsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_create_archived_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateArchivedErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
