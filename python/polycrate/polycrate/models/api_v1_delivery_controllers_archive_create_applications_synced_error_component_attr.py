from typing import Literal

ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponentAttr = Literal["applications_synced"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponentAttr
] = {
    "applications_synced",
}


def check_api_v1_delivery_controllers_archive_create_applications_synced_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateApplicationsSyncedErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_SYNCED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
