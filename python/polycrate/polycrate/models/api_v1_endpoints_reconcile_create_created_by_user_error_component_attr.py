from typing import Literal

ApiV1EndpointsReconcileCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_ENDPOINTS_RECONCILE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_endpoints_reconcile_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
