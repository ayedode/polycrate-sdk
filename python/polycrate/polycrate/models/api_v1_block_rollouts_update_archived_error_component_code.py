from typing import Literal

ApiV1BlockRolloutsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_update_archived_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateArchivedErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
