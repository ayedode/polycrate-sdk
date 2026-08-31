from typing import Literal

ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertcategories_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
