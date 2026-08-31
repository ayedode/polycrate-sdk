from typing import Literal

ApiV1AlertcategoriesUpdateDescriptionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateDescriptionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertcategories_update_description_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateDescriptionErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
