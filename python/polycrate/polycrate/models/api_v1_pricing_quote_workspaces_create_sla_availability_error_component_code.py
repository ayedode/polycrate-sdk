from typing import Literal

ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_pricing_quote_workspaces_create_sla_availability_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
