from typing import Literal

ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_quote_workspaces_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
