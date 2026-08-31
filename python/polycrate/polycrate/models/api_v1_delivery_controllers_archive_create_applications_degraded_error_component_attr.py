from typing import Literal

ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponentAttr = Literal["applications_degraded"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponentAttr
] = {
    "applications_degraded",
}


def check_api_v1_delivery_controllers_archive_create_applications_degraded_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateApplicationsDegradedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
