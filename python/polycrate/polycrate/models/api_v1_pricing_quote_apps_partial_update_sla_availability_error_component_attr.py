from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_quote_apps_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
