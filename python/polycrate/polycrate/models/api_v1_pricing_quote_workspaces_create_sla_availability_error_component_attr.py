from typing import Literal

ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_quote_workspaces_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
