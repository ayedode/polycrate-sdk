from typing import Literal

ApiV1ProvidersReconcileCreateAsnErrorComponentAttr = Literal["asn"]

API_V1_PROVIDERS_RECONCILE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateAsnErrorComponentAttr
] = {
    "asn",
}


def check_api_v1_providers_reconcile_create_asn_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateAsnErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ASN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
