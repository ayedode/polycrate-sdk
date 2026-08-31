from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_archive_create_loadbalancer_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
