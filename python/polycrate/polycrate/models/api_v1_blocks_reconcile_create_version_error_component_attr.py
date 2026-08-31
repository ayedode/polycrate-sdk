from typing import Literal

ApiV1BlocksReconcileCreateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_blocks_reconcile_create_version_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
