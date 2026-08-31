from typing import Literal

ApiV1BlockRolloutsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_block_rollouts_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
