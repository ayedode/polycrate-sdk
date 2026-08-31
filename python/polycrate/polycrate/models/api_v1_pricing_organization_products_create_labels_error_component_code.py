from typing import Literal

ApiV1PricingOrganizationProductsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_create_labels_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateLabelsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
