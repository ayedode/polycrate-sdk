from typing import Literal

ApiV1BlocksArchiveCreateDocumentationUrlErrorComponentAttr = Literal["documentation_url"]

API_V1_BLOCKS_ARCHIVE_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateDocumentationUrlErrorComponentAttr
] = {
    "documentation_url",
}


def check_api_v1_blocks_archive_create_documentation_url_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateDocumentationUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
