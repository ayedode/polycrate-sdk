from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_organization_products_archive_create_internal_note_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_INTERNAL_NOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
