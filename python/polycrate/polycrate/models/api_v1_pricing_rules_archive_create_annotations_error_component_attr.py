from typing import Literal

ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_rules_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
