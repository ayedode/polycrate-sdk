from typing import Literal

ApiV1DeliveryControllersArchiveCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_delivery_controllers_archive_create_credential_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateCredentialErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
