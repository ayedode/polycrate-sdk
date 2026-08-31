from typing import Literal

ApiV1BlocksArchiveCreateTemplateErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateTemplateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_archive_create_template_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateTemplateErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
