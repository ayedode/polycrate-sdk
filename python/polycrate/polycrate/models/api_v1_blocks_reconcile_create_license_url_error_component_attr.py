from typing import Literal

ApiV1BlocksReconcileCreateLicenseUrlErrorComponentAttr = Literal["license_url"]

API_V1_BLOCKS_RECONCILE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateLicenseUrlErrorComponentAttr
] = {
    "license_url",
}


def check_api_v1_blocks_reconcile_create_license_url_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateLicenseUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_LICENSE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
