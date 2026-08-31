from typing import Literal

ApiV1AlertcategoriesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertcategories_update_labels_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateLabelsErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
