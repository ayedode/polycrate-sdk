from typing import Literal

ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_quote_workspaces_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
