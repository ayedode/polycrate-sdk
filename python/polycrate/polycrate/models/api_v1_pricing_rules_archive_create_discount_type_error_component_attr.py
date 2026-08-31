from typing import Literal

ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentAttr = Literal["discount_type"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentAttr
] = {
    "discount_type",
}


def check_api_v1_pricing_rules_archive_create_discount_type_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
