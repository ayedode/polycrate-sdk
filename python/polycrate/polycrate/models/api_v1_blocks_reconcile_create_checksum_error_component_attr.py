from typing import Literal

ApiV1BlocksReconcileCreateChecksumErrorComponentAttr = Literal["checksum"]

API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateChecksumErrorComponentAttr
] = {
    "checksum",
}


def check_api_v1_blocks_reconcile_create_checksum_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateChecksumErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
