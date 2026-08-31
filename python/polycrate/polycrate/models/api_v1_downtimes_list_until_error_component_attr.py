from typing import Literal

ApiV1DowntimesListUntilErrorComponentAttr = Literal["until"]

API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesListUntilErrorComponentAttr] = {
    "until",
}


def check_api_v1_downtimes_list_until_error_component_attr(value: str) -> ApiV1DowntimesListUntilErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_UNTIL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
