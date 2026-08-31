from typing import Literal

ApiV1DowntimesListSinceErrorComponentAttr = Literal["since"]

API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesListSinceErrorComponentAttr] = {
    "since",
}


def check_api_v1_downtimes_list_since_error_component_attr(value: str) -> ApiV1DowntimesListSinceErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_SINCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
