from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_quote_workspaces_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
