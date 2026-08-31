from typing import Literal

ApiV1AlertcategoryAnalysesListAlertnameErrorComponentAttr = Literal["alertname"]

API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryAnalysesListAlertnameErrorComponentAttr
] = {
    "alertname",
}


def check_api_v1_alertcategory_analyses_list_alertname_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryAnalysesListAlertnameErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_ANALYSES_LIST_ALERTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
