from typing import Literal

ApiV1BlocksCheckCreateDocumentationUrlErrorComponentAttr = Literal["documentation_url"]

API_V1_BLOCKS_CHECK_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateDocumentationUrlErrorComponentAttr
] = {
    "documentation_url",
}


def check_api_v1_blocks_check_create_documentation_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateDocumentationUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
