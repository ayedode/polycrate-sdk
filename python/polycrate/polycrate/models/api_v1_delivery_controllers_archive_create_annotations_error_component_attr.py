from typing import Literal

ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_delivery_controllers_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
