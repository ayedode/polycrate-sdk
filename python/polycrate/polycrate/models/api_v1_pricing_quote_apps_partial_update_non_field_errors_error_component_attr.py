from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_pricing_quote_apps_partial_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
