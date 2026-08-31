from typing import Literal

ApiV1BlocksUpdateDocumentationUrlErrorComponentAttr = Literal["documentation_url"]

API_V1_BLOCKS_UPDATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksUpdateDocumentationUrlErrorComponentAttr
] = {
    "documentation_url",
}


def check_api_v1_blocks_update_documentation_url_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateDocumentationUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
