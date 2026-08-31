from typing import Literal

ApiV1BlocksArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksArchiveCreateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_blocks_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
