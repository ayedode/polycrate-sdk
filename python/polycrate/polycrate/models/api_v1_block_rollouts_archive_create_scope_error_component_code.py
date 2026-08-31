from typing import Literal

ApiV1BlockRolloutsArchiveCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollouts_archive_create_scope_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateScopeErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
