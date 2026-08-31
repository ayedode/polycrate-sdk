from typing import Literal

ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_create_object_id_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
