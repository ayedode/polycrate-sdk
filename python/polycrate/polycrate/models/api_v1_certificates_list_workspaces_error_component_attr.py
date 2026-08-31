from typing import Literal

ApiV1CertificatesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_CERTIFICATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_certificates_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1CertificatesListWorkspacesErrorComponentAttr:
    if value in API_V1_CERTIFICATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
