from typing import Literal

ApiV1BlocksArchiveCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_archive_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
