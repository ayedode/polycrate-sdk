from typing import Literal

ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_organization_products_update_internal_note_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
