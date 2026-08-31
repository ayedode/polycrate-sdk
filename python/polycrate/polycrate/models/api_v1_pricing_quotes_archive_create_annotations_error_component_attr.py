from typing import Literal

ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_quotes_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
