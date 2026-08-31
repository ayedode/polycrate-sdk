from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceTemplateRenderRequestRequest")


@_attrs_define
class WorkspaceTemplateRenderRequestRequest:
    """
    Attributes:
        workspace_name (str): Name of the workspace
        extra_context (Any | Unset): Additional context
    """

    workspace_name: str
    extra_context: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_name = self.workspace_name

        extra_context = self.extra_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_name": workspace_name,
            }
        )
        if extra_context is not UNSET:
            field_dict["extra_context"] = extra_context

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("workspace_name", (None, str(self.workspace_name).encode(), "text/plain")))

        if not isinstance(self.extra_context, Unset):
            files.append(("extra_context", (None, str(self.extra_context).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_name = d.pop("workspace_name")

        extra_context = d.pop("extra_context", UNSET)

        workspace_template_render_request_request = cls(
            workspace_name=workspace_name,
            extra_context=extra_context,
        )

        workspace_template_render_request_request.additional_properties = d
        return workspace_template_render_request_request

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
