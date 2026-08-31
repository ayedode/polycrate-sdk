from typing import Literal

ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_pricing_organization_products_create_object_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateObjectIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
