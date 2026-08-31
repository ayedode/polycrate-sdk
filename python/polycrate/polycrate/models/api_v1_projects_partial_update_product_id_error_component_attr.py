from typing import Literal

ApiV1ProjectsPartialUpdateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_PROJECTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_projects_partial_update_product_id_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateProductIdErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
