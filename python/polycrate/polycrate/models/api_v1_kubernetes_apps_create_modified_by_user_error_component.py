from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_v1_kubernetes_apps_create_modified_by_user_error_component_attr import (
    ApiV1KubernetesAppsCreateModifiedByUserErrorComponentAttr,
    check_api_v1_kubernetes_apps_create_modified_by_user_error_component_attr,
)
from ..models.api_v1_kubernetes_apps_create_modified_by_user_error_component_code import (
    ApiV1KubernetesAppsCreateModifiedByUserErrorComponentCode,
    check_api_v1_kubernetes_apps_create_modified_by_user_error_component_code,
)

T = TypeVar("T", bound="ApiV1KubernetesAppsCreateModifiedByUserErrorComponent")


@_attrs_define
class ApiV1KubernetesAppsCreateModifiedByUserErrorComponent:
    """
    Attributes:
        attr (ApiV1KubernetesAppsCreateModifiedByUserErrorComponentAttr): * `modified_by_user` - modified_by_user
        code (ApiV1KubernetesAppsCreateModifiedByUserErrorComponentCode): * `does_not_exist` - does_not_exist
            * `incorrect_type` - incorrect_type
        detail (str):
    """

    attr: ApiV1KubernetesAppsCreateModifiedByUserErrorComponentAttr
    code: ApiV1KubernetesAppsCreateModifiedByUserErrorComponentCode
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attr: str = self.attr

        code: str = self.code

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attr": attr,
                "code": code,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attr = check_api_v1_kubernetes_apps_create_modified_by_user_error_component_attr(d.pop("attr"))

        code = check_api_v1_kubernetes_apps_create_modified_by_user_error_component_code(d.pop("code"))

        detail = d.pop("detail")

        api_v1_kubernetes_apps_create_modified_by_user_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        api_v1_kubernetes_apps_create_modified_by_user_error_component.additional_properties = d
        return api_v1_kubernetes_apps_create_modified_by_user_error_component

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
