from typing import Literal

ApiV1PopsReconcileCreateLatitudeErrorComponentAttr = Literal["latitude"]

API_V1_POPS_RECONCILE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateLatitudeErrorComponentAttr
] = {
    "latitude",
}


def check_api_v1_pops_reconcile_create_latitude_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateLatitudeErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_LATITUDE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
