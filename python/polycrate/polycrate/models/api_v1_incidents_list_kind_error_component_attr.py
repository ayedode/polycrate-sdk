from typing import Literal

ApiV1IncidentsListKindErrorComponentAttr = Literal["kind"]

API_V1_INCIDENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_incidents_list_kind_error_component_attr(value: str) -> ApiV1IncidentsListKindErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
