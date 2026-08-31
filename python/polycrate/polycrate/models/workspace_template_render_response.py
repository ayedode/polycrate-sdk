from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceTemplateRenderResponse")


@_attrs_define
class WorkspaceTemplateRenderResponse:
    """
    Attributes:
        success (bool):
        workspace_poly (str):
        secrets_poly (str):
    """

    success: bool
    workspace_poly: str
    secrets_poly: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        workspace_poly = self.workspace_poly

        secrets_poly = self.secrets_poly

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "workspace_poly": workspace_poly,
                "secrets_poly": secrets_poly,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        workspace_poly = d.pop("workspace_poly")

        secrets_poly = d.pop("secrets_poly")

        workspace_template_render_response = cls(
            success=success,
            workspace_poly=workspace_poly,
            secrets_poly=secrets_poly,
        )

        workspace_template_render_response.additional_properties = d
        return workspace_template_render_response

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
