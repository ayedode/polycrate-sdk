from typing import Literal

ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_quote_workspaces_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
