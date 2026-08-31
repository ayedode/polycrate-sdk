from typing import Literal

ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
