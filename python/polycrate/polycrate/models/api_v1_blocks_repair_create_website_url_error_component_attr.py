from typing import Literal

ApiV1BlocksRepairCreateWebsiteUrlErrorComponentAttr = Literal["website_url"]

API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateWebsiteUrlErrorComponentAttr
] = {
    "website_url",
}


def check_api_v1_blocks_repair_create_website_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateWebsiteUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
