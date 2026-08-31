from typing import Literal

ApiV1ProjectsUpdateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsUpdateProductIdErrorComponentAttr] = {
    "product_id",
}


def check_api_v1_projects_update_product_id_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateProductIdErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
