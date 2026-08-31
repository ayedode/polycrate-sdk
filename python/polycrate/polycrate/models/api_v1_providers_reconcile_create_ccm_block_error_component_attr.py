from typing import Literal

ApiV1ProvidersReconcileCreateCcmBlockErrorComponentAttr = Literal["ccm_block"]

API_V1_PROVIDERS_RECONCILE_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateCcmBlockErrorComponentAttr
] = {
    "ccm_block",
}


def check_api_v1_providers_reconcile_create_ccm_block_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateCcmBlockErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
