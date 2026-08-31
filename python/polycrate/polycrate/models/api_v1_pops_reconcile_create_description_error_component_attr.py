from typing import Literal

ApiV1PopsReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POPS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_pops_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1PopsReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_POPS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
