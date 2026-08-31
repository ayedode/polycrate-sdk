from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_quote_workspaces_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
