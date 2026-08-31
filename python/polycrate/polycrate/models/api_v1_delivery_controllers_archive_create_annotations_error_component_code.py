from typing import Literal

ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_delivery_controllers_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
