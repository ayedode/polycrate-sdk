from typing import Literal

ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_quotes_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
