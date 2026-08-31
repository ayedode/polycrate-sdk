from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_organization_products_partial_update_content_type_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
