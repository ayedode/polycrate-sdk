from typing import Literal

ApiV1OrganizationsReconcileCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_organizations_reconcile_create_annotations_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
