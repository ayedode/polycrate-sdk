from typing import Literal

ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentAttr = Literal["discount_value"]

API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentAttr
] = {
    "discount_value",
}


def check_api_v1_pricing_rules_archive_create_discount_value_error_component_attr(
    value: str,
) -> ApiV1PricingRulesArchiveCreateDiscountValueErrorComponentAttr:
    if value in API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_ARCHIVE_CREATE_DISCOUNT_VALUE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
