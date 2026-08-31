from typing import Literal

ApiV1BlocksArchiveCreateUserSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_ARCHIVE_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateUserSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_archive_create_user_spec_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateUserSpecErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_USER_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
