from typing import Literal

ApiV1DowntimesCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_downtimes_create_name_error_component_attr(value: str) -> ApiV1DowntimesCreateNameErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
