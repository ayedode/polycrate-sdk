from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quote_apps_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
