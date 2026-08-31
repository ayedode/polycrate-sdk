from typing import Literal

ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_QUOTE_APPS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_quote_apps_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
