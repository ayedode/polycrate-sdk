from typing import Literal

ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_delivery_controllers_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
