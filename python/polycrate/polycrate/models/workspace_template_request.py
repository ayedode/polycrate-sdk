from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceTemplateRequest")


@_attrs_define
class WorkspaceTemplateRequest:
    """Full serializer for WorkspaceTemplate - includes template content.

    Attributes:
        name (str):
        display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
            from the name.
        organization_id (UUID | Unset):
        description (None | str | Unset): Description of the template purpose and usage
        workspace_poly_template (None | str | Unset): Jinja2 template for workspace.poly file
        secrets_poly_template (None | str | Unset): Jinja2 template for secrets.poly file (sensitive data)
        is_default (bool | Unset): If true, this template is the default for the organization
    """

    name: str
    display_name: None | str | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    workspace_poly_template: None | str | Unset = UNSET
    secrets_poly_template: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        workspace_poly_template: None | str | Unset
        if isinstance(self.workspace_poly_template, Unset):
            workspace_poly_template = UNSET
        else:
            workspace_poly_template = self.workspace_poly_template

        secrets_poly_template: None | str | Unset
        if isinstance(self.secrets_poly_template, Unset):
            secrets_poly_template = UNSET
        else:
            secrets_poly_template = self.secrets_poly_template

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if description is not UNSET:
            field_dict["description"] = description
        if workspace_poly_template is not UNSET:
            field_dict["workspace_poly_template"] = workspace_poly_template
        if secrets_poly_template is not UNSET:
            field_dict["secrets_poly_template"] = secrets_poly_template
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.workspace_poly_template, Unset):
            if isinstance(self.workspace_poly_template, str):
                files.append(
                    ("workspace_poly_template", (None, str(self.workspace_poly_template).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("workspace_poly_template", (None, str(self.workspace_poly_template).encode(), "text/plain"))
                )

        if not isinstance(self.secrets_poly_template, Unset):
            if isinstance(self.secrets_poly_template, str):
                files.append(("secrets_poly_template", (None, str(self.secrets_poly_template).encode(), "text/plain")))
            else:
                files.append(("secrets_poly_template", (None, str(self.secrets_poly_template).encode(), "text/plain")))

        if not isinstance(self.is_default, Unset):
            files.append(("is_default", (None, str(self.is_default).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_workspace_poly_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_poly_template = _parse_workspace_poly_template(d.pop("workspace_poly_template", UNSET))

        def _parse_secrets_poly_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secrets_poly_template = _parse_secrets_poly_template(d.pop("secrets_poly_template", UNSET))

        is_default = d.pop("is_default", UNSET)

        workspace_template_request = cls(
            name=name,
            display_name=display_name,
            organization_id=organization_id,
            description=description,
            workspace_poly_template=workspace_poly_template,
            secrets_poly_template=secrets_poly_template,
            is_default=is_default,
        )

        workspace_template_request.additional_properties = d
        return workspace_template_request

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
