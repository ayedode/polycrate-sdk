from typing import Literal

ApiV1EndpointsReconcileCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ENDPOINTS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_endpoints_reconcile_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
