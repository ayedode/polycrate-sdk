from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_attr import (
    UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr,
    check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_attr,
)
from ..models.ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_code import (
    UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode,
    check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_code,
)

T = TypeVar("T", bound="UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent")


@_attrs_define
class UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponent:
    """
    Attributes:
        attr (UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr): *
            `last_reconciliation_duration_seconds` - last_reconciliation_duration_seconds
        code (UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode): * `invalid` - invalid
            * `max_string_length` - max_string_length
        detail (str):
    """

    attr: UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentAttr
    code: UiK8SAppsInstallCreateLastReconciliationDurationSecondsErrorComponentCode
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
        attr = check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_attr(d.pop("attr"))

        code = check_ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component_code(d.pop("code"))

        detail = d.pop("detail")

        ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component = cls(
            attr=attr,
            code=code,
            detail=detail,
        )

        ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component.additional_properties = d
        return ui_k8s_apps_install_create_last_reconciliation_duration_seconds_error_component

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
