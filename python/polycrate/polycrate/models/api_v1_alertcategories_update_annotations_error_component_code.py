from typing import Literal

ApiV1AlertcategoriesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertcategories_update_annotations_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
