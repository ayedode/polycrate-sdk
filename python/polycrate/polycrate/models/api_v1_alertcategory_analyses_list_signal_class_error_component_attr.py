from typing import Literal

ApiV1AlertcategoryAnalysesListSignalClassErrorComponentAttr = Literal["signal_class"]

API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryAnalysesListSignalClassErrorComponentAttr
] = {
    "signal_class",
}


def check_api_v1_alertcategory_analyses_list_signal_class_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryAnalysesListSignalClassErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
