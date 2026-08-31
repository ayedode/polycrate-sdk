from typing import Literal

ApiV1AlertcategoryAnalysesListSignalClassErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryAnalysesListSignalClassErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_alertcategory_analyses_list_signal_class_error_component_code(
    value: str,
) -> ApiV1AlertcategoryAnalysesListSignalClassErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_ANALYSES_LIST_SIGNAL_CLASS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
