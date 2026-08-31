from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_update_cluster_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
