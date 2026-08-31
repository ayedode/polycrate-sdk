from typing import Literal

ApiV1PricingOrganizationProductsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_organization_products_update_kind_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateKindErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
