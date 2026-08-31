from typing import Literal

ApiV1DowntimesCreateIsActiveErrorComponentAttr = Literal["is_active"]

API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesCreateIsActiveErrorComponentAttr] = {
    "is_active",
}


def check_api_v1_downtimes_create_is_active_error_component_attr(
    value: str,
) -> ApiV1DowntimesCreateIsActiveErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
