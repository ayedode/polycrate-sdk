from typing import Literal

ApiV1DowntimesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOWNTIMES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_downtimes_create_kind_error_component_attr(value: str) -> ApiV1DowntimesCreateKindErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
