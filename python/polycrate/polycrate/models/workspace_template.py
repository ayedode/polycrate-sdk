from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="WorkspaceTemplate")


@_attrs_define
class WorkspaceTemplate:
    """Full serializer for WorkspaceTemplate - includes template content.

    Attributes:
        id (UUID):
        name (str):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        workspaces_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        url (str):
        display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
            from the name.
        description (None | str | Unset): Description of the template purpose and usage
        workspace_poly_template (None | str | Unset): Jinja2 template for workspace.poly file
        secrets_poly_template (None | str | Unset): Jinja2 template for secrets.poly file (sensitive data)
        is_default (bool | Unset): If true, this template is the default for the organization
    """

    id: UUID
    name: str
    organization: OrganizationSimple
    state: LastStateEnum
    conditions: Any
    workspaces_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    url: str
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    workspace_poly_template: None | str | Unset = UNSET
    secrets_poly_template: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization = self.organization.to_dict()

        state: str = self.state

        conditions = self.conditions

        workspaces_count = self.workspaces_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        url = self.url

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

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
                "id": id,
                "name": name,
                "organization": organization,
                "state": state,
                "conditions": conditions,
                "workspaces_count": workspaces_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "url": url,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if workspace_poly_template is not UNSET:
            field_dict["workspace_poly_template"] = workspace_poly_template
        if secrets_poly_template is not UNSET:
            field_dict["secrets_poly_template"] = secrets_poly_template
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        state = check_last_state_enum(d.pop("state"))

        conditions = d.pop("conditions")

        workspaces_count = d.pop("workspaces_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

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

        workspace_template = cls(
            id=id,
            name=name,
            organization=organization,
            state=state,
            conditions=conditions,
            workspaces_count=workspaces_count,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            display_name=display_name,
            description=description,
            workspace_poly_template=workspace_poly_template,
            secrets_poly_template=secrets_poly_template,
            is_default=is_default,
        )

        workspace_template.additional_properties = d
        return workspace_template

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
