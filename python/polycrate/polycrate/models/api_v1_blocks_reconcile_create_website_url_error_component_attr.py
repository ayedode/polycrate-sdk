from typing import Literal

ApiV1BlocksReconcileCreateWebsiteUrlErrorComponentAttr = Literal["website_url"]

API_V1_BLOCKS_RECONCILE_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateWebsiteUrlErrorComponentAttr
] = {
    "website_url",
}


def check_api_v1_blocks_reconcile_create_website_url_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateWebsiteUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
