from typing import Literal

ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponentAttr = Literal["applications_out_of_sync"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponentAttr
] = {
    "applications_out_of_sync",
}


def check_api_v1_delivery_controllers_archive_create_applications_out_of_sync_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateApplicationsOutOfSyncErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_APPLICATIONS_OUT_OF_SYNC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
