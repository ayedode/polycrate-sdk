from typing import Literal

ApiV1AlertcategoryAnalysesListAlertnameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryAnalysesListAlertnameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_alertcategory_analyses_list_alertname_error_component_code(
    value: str,
) -> ApiV1AlertcategoryAnalysesListAlertnameErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
